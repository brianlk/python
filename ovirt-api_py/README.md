# Script to backup virtual machine in ovirt platform

## Start VM

python3 main.py --vm_name "ol7a" --action start

## Shutdown VM

python3 main.py --vm_name "ol7a" --action stop

## Snapshot VM

python3 main.py --vm_name "ol7a" --action snapshot

## Print debug

python3 main.py --vm_name "ol7a" --action start --debug 1
