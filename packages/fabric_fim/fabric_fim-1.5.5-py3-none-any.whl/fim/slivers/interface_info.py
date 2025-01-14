#!/usr/bin/env python3
# MIT License
#
# Copyright (c) 2020 FABRIC Testbed
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.
#
#
# Author: Komal Thareja (kthare10@renci.org)
import ipaddress
import uuid
import enum

from .base_sliver import BaseSliver
from .topology_diff import TopologyDiff
from .capacities_labels import Labels


class InterfaceType(enum.Enum):
    """
    Possible Interface/Port types in FABRIC.
    """
    AccessPort = enum.auto()
    TrunkPort = enum.auto()
    ServicePort = enum.auto()
    DedicatedPort = enum.auto()
    SharedPort = enum.auto()
    vInt = enum.auto()
    StitchPort = enum.auto()
    FacilityPort = enum.auto()

    def help(self) -> str:
        return 'An ' + self.name

    def __repr__(self):
        return self.name

    def __str__(self):
        return self.name


class InterfaceSliver(BaseSliver):

    NAME_REGEX = r'^[\w\-+_/\.\ :]{2,255}$'

    def __init__(self):
        # addresses are stored on labels, bandwidth on capacities
        super().__init__()
        # note that these are used in ASMs, not delegateable
        self.peer_labels = None

    def set_peer_labels(self, lab: Labels) -> None:
        assert(lab is None or isinstance(lab, Labels))
        self.peer_labels = lab

    def get_peer_labels(self) -> Labels:
        return self.peer_labels

    @staticmethod
    def type_from_str(ntype: str) -> InterfaceType:
        if ntype is None:
            return None
        for t in InterfaceType:
            if ntype == str(t):
                return t

    def diff(self, other_sliver) -> TopologyDiff or None:
        raise RuntimeError('Not implemented')


class InterfaceInfo:
    def __init__(self):
        self.interfaces = {}

    def add_interface(self, interface_info: InterfaceSliver):
        self.interfaces[interface_info.resource_name] = interface_info

    def remove_interface(self, name: str):
        if name in self.interfaces.keys():
            self.interfaces.pop(name)

    def get_interface(self, name: str):
        return self.interfaces.get(name, None)

    def get_interface_names(self):
        return list(self.interfaces.keys())

    def list_interfaces(self):
        return list(self.interfaces.values())
