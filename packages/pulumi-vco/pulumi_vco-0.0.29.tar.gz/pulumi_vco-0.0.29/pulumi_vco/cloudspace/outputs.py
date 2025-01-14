# coding=utf-8
# *** WARNING: this file was generated by pulumi. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import copy
import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from .. import _utilities

__all__ = [
    'CpuTopology',
    'NetworkInterface',
    'OsAccount',
    'VmDisk',
]

@pulumi.output_type
class CpuTopology(dict):
    def __init__(__self__, *,
                 cores: int,
                 sockets: int,
                 threads: int):
        pulumi.set(__self__, "cores", cores)
        pulumi.set(__self__, "sockets", sockets)
        pulumi.set(__self__, "threads", threads)

    @property
    @pulumi.getter
    def cores(self) -> int:
        return pulumi.get(self, "cores")

    @property
    @pulumi.getter
    def sockets(self) -> int:
        return pulumi.get(self, "sockets")

    @property
    @pulumi.getter
    def threads(self) -> int:
        return pulumi.get(self, "threads")


@pulumi.output_type
class NetworkInterface(dict):
    def __init__(__self__, *,
                 device_name: str,
                 external_cloudspace_id: str,
                 ip_address: str,
                 mac_address: str,
                 model: str,
                 network_id: int,
                 nic_type: str):
        pulumi.set(__self__, "device_name", device_name)
        pulumi.set(__self__, "external_cloudspace_id", external_cloudspace_id)
        pulumi.set(__self__, "ip_address", ip_address)
        pulumi.set(__self__, "mac_address", mac_address)
        pulumi.set(__self__, "model", model)
        pulumi.set(__self__, "network_id", network_id)
        pulumi.set(__self__, "nic_type", nic_type)

    @property
    @pulumi.getter
    def device_name(self) -> str:
        return pulumi.get(self, "device_name")

    @property
    @pulumi.getter
    def external_cloudspace_id(self) -> str:
        return pulumi.get(self, "external_cloudspace_id")

    @property
    @pulumi.getter
    def ip_address(self) -> str:
        return pulumi.get(self, "ip_address")

    @property
    @pulumi.getter
    def mac_address(self) -> str:
        return pulumi.get(self, "mac_address")

    @property
    @pulumi.getter
    def model(self) -> str:
        return pulumi.get(self, "model")

    @property
    @pulumi.getter
    def network_id(self) -> int:
        return pulumi.get(self, "network_id")

    @property
    @pulumi.getter
    def nic_type(self) -> str:
        return pulumi.get(self, "nic_type")


@pulumi.output_type
class OsAccount(dict):
    def __init__(__self__, *,
                 login: str,
                 password: str):
        pulumi.set(__self__, "login", login)
        pulumi.set(__self__, "password", password)

    @property
    @pulumi.getter
    def login(self) -> str:
        return pulumi.get(self, "login")

    @property
    @pulumi.getter
    def password(self) -> str:
        return pulumi.get(self, "password")


@pulumi.output_type
class VmDisk(dict):
    def __init__(__self__, *,
                 description: str,
                 disk_id: int,
                 disk_name: str,
                 disk_size: int,
                 disk_type: str,
                 exposed: bool,
                 order: str,
                 pci_bus: int,
                 pci_slot: int,
                 status: str):
        pulumi.set(__self__, "description", description)
        pulumi.set(__self__, "disk_id", disk_id)
        pulumi.set(__self__, "disk_name", disk_name)
        pulumi.set(__self__, "disk_size", disk_size)
        pulumi.set(__self__, "disk_type", disk_type)
        pulumi.set(__self__, "exposed", exposed)
        pulumi.set(__self__, "order", order)
        pulumi.set(__self__, "pci_bus", pci_bus)
        pulumi.set(__self__, "pci_slot", pci_slot)
        pulumi.set(__self__, "status", status)

    @property
    @pulumi.getter
    def description(self) -> str:
        return pulumi.get(self, "description")

    @property
    @pulumi.getter
    def disk_id(self) -> int:
        return pulumi.get(self, "disk_id")

    @property
    @pulumi.getter
    def disk_name(self) -> str:
        return pulumi.get(self, "disk_name")

    @property
    @pulumi.getter
    def disk_size(self) -> int:
        return pulumi.get(self, "disk_size")

    @property
    @pulumi.getter
    def disk_type(self) -> str:
        return pulumi.get(self, "disk_type")

    @property
    @pulumi.getter
    def exposed(self) -> bool:
        return pulumi.get(self, "exposed")

    @property
    @pulumi.getter
    def order(self) -> str:
        return pulumi.get(self, "order")

    @property
    @pulumi.getter
    def pci_bus(self) -> int:
        return pulumi.get(self, "pci_bus")

    @property
    @pulumi.getter
    def pci_slot(self) -> int:
        return pulumi.get(self, "pci_slot")

    @property
    @pulumi.getter
    def status(self) -> str:
        return pulumi.get(self, "status")


