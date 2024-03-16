# Importing BeautifulSoup class from the bs4 module
from bs4 import BeautifulSoup
import urllib.request
import re


# Opening the html file
HTMLFile = open(r"table.html", "r")

# Reading the file
index = HTMLFile.read()

# Creating a BeautifulSoup object and specifying the parser
soup = BeautifulSoup(index, 'html.parser')

a_tags = soup.find_all('a')

count = 0
for t in a_tags:
    hs = t.get('href')
    if 'mp3.php?' in hs:
        url = f'https://www.hec.org.hk{hs}'
        xxx = url.replace('桌前默想', '%E6%A1%8C%E5%89%8D%E9%BB%98%E6%83%B3').replace(' ', '%20')
        name = re.sub(r'MP3', '', t.text)
        name = re.sub(r'講員:胡恩德.*經文:','_', name)
        name = re.sub(r'^\s', '', name)
        mp3file = urllib.request.urlopen(xxx)
        print(name)
        with open(f'{name}.mp3', 'wb') as output:
            output.write(mp3file.read())
        count += 1
        # if count > 5:
        #     break

"""
https://hec.org.hk/mp3.php?mp3=100/%30%33%2d%31%39%39%30%2d%30%30%32%37%20%ae%e0%ab%65%c0%71%b7%51%20%31%30%31%2e%6d%70%33&prog=mp3&file=03-1990-0027%20%E6%A1%8C%E5%89%8D%E9%BB%98%E6%83%B3%20101.mp3&path=100
"""
