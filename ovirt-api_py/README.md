# Script to backup virtual machine in ovirt platform

## Start VM
    export OLVM_FQDN="manager2.oc.example"
    python3 main.py --vm_name "ol7a" --action start

## Shutdown VM
    export OLVM_FQDN="manager2.oc.example"
    python3 main.py --vm_name "ol7a" --action stop

## Snapshot VM
    export OLVM_FQDN="manager2.oc.example"
    python3 main.py --vm_name "ol7a" --action snapshot

## Delete VM
    export OLVM_FQDN="manager2.oc.example"
    python3 main.py --vm_name "ol7a" --action delete

## Print debug
    export OLVM_FQDN="manager2.oc.example"
    python3 main.py --vm_name "ol7a" --action start --debug 1
