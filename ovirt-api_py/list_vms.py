#!/usr/bin/env python
# -*- coding: utf-8 -*-

# https://access.redhat.com/documentation/en-us/red_hat_virtualization/4.4/html/python_sdk_guide/chap-python_examples
# dnf install python3-ovirt-engine-sdk4
# /usr/share/doc/python3-ovirt-engine-sdk4

import logging

import ovirtsdk4 as sdk
import ovirtsdk4.types as types

logging.basicConfig(level=logging.DEBUG, filename='example.log')

# This example will connect to the server and print the names and identifiers of all the virtual machines:

# Create the connection to the server:
connection = sdk.Connection(
    url='https://manager2.oc.example/ovirt-engine/api',
    username='admin@internal',
    password='password',
    ca_file='ca.pem',
    debug=True,
    log=logging.getLogger(),
)

# Get the reference to the "vms" service:
vms_service = connection.system_service().vms_service()

# Use the "list" method of the "vms" service to list all the virtual machines of the system:
vms = vms_service.list()
for v in vms:
    print(v.id)
    break

exit()
# vm_service = vms_service.vm_service(id="623393ef-1503-43b9-bf17-e69bf1e90e7f")
# disks = vm_service.disk_attachments_service().list()
# types.Backup(
#     disks=disks,
#     description="test by brian"
# )
# backups_service = vm_service.backups_service()
# backup = backups_service.add(
#     types.Backup(
#         disks=disks
#     )
# )

system_service = connection.system_service()
vm_service = system_service.vms_service().vm_service(id="623393ef-1503-43b9-bf17-e69bf1e90e7f")
# disk_attachments = vm_service.disk_attachments_service().list()

# disks = []
# for disk_attachment in disk_attachments:
#     disk_id = disk_attachment.disk.id
#     disk = system_service.disks_service().disk_service(disk_id).get()
#     disks.append(disk)
    
# backups_service = vm_service.backups_service()
# backup = backups_service.add(
#     types.Backup(
#         disks=disks,
#         description="test backup"
#     )
# )
    # system_service = connection.system_service()
    # vms_service = system_service.vms_service()
backups_service = vm_service.backups_service()
x = backups_service.backup_service(id="fc5f5bb5-ddd8-49d8-b548-561fefef88a0")

print(x.finalize())


# Close the connection to the server:
connection.close()
