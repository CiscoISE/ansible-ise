#!/usr/bin/env python
from __future__ import (absolute_import, division, print_function)
__metaclass__ = type


class AnsibleISEException(Exception):
    """Base class for all Ansible ISE package exceptions."""
    pass


class InconsistentParameters(AnsibleISEException):
    """Provided parameters are not consistent."""
    pass


class PrimaryNodeNotUnique(AnsibleISEException):
    """More than one node has the 'PPAN' attribute"""
    pass


class ISEAPIError(AnsibleISEException):
    """An API error was received from the ISE node"""
    pass

class NodeNotStandalone(AnsibleISEException):
    """The node is not in standalone state"""

