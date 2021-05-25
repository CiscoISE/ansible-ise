import unittest
from plugins.action.network_device_group import NetworkDeviceGroup
from .testutils import FakeISESDK
import sys
import yaml

# playbook_file = "playbooks/network_device_group.yml"

# with open(playbook_file, 'r') as stream:
#     try:
#         playbook = yaml.safe_load(stream)
#         tasks = playbook[0]["tasks"]
#         for task in tasks:
#             print(task)
#     except yaml.YAMLError as exc:
#         print(exc)


def object_present_absent(obj, state, ise):
    if state == "present":
        if obj.exists():
            response = obj.update()
            ise.object_updated()
        else:
            response = obj.create()
            ise.object_created()

    elif state == "absent":
        if obj.exists():
            response = obj.delete()
            ise.object_deleted()
        else:
            ise.object_already_absent()


class TestNetworkDeviceGroup(unittest.TestCase):

    # def test_get_object(self):
    #     obj = NetworkDeviceGroup(params, ise)

    def test_object_exists(self):
        existing_object = dict(
                name="existing_object",
                description="Existing object",
                othername="other_name",
            )
        ise = FakeISESDK("NetworkDeviceGroup")
        ise.add_object(existing_object)
        new_object = existing_object

        object_present_absent(
                NetworkDeviceGroup(new_object, ise),
                "present",
                ise
            )
        
        ise_object = ise.get_object()

        self.assertDictEqual(new_object, ise_object)


    def test_object_doesnt_exist(self):
        existing_object = dict(
                name="existing_object",
                description="Existing object",
                othername="other_name",
            )
        ise = FakeISESDK("NetworkDeviceGroup")
        ise.add_object(existing_object)
        new_object = dict(
                name="new_object",
                description="New object",
                othername="other_name",
            )
        object_present_absent(
                NetworkDeviceGroup(new_object, ise),
                "present",
                ise
            )
        
        ise_object = ise.get_object()

        self.assertDictEqual(new_object, ise_object)

