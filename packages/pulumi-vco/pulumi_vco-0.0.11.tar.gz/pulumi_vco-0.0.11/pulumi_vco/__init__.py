# coding=utf-8
# *** WARNING: this file was generated by pulumi. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

from . import _utilities
import typing
# Export this package's modules as members:
from .provider import *

# Make subpackages available:
if typing.TYPE_CHECKING:
    import pulumi_vco.resources as __resources
    resources = __resources
else:
    resources = _utilities.lazy_import('pulumi_vco.resources')

_utilities.register(
    resource_modules="""
[
 {
  "pkg": "vco",
  "mod": "resources",
  "fqn": "pulumi_vco.resources",
  "classes": {
   "vco:resources:AntiAffinityGroup": "AntiAffinityGroup",
   "vco:resources:AntiAffinityGroupVM": "AntiAffinityGroupVM",
   "vco:resources:Cloudspace": "Cloudspace",
   "vco:resources:ConnectedCloudspace": "ConnectedCloudspace",
   "vco:resources:Disk": "Disk",
   "vco:resources:ExposedDisk": "ExposedDisk",
   "vco:resources:ExternalNetwork": "ExternalNetwork",
   "vco:resources:Host": "Host",
   "vco:resources:LoadBalancer": "LoadBalancer",
   "vco:resources:ObjectSpaceLink": "ObjectSpaceLink",
   "vco:resources:PortForward": "PortForward",
   "vco:resources:ReverseProxy": "ReverseProxy",
   "vco:resources:ServerPool": "ServerPool",
   "vco:resources:VirtualMachine": "VirtualMachine",
   "vco:resources:VirtualMachineCD": "VirtualMachineCD",
   "vco:resources:VirtualMachineDisk": "VirtualMachineDisk",
   "vco:resources:VirtualMachineNIC": "VirtualMachineNIC"
  }
 }
]
""",
    resource_packages="""
[
 {
  "pkg": "vco",
  "token": "pulumi:providers:vco",
  "fqn": "pulumi_vco",
  "class": "Provider"
 }
]
"""
)
