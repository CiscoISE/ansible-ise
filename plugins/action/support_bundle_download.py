#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Copyright (c) 2024, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)

from __future__ import absolute_import, division, print_function

__metaclass__ = type
from ansible_collections.cisco.ise.plugins.plugin_utils.action import ActionModule as ActionBase
from ansible_collections.cisco.ise.plugins.plugin_utils.ise import (
    ISESDK,
    ise_argument_spec,
)
import os.path

# Get common arguements specification
argument_spec = ise_argument_spec()
# Add arguments specific for this module
argument_spec.update(
    dict(
        fileName=dict(type="str"),
        dirPath=dict(type="str"),
        saveFile=dict(type="bool"),
    )
)
# filename=dict(type="str"), issue #133 and sanity

required_if = []
required_one_of = []
mutually_exclusive = []
required_together = []


class ActionModule(ActionBase):
    _supports_check_mode = False

    def get_object(self, params):
        new_object = dict(
            file_name=params.get("fileName") or params.get("filename"),
            dirpath=params.get("dirPath"),
            save_file=params.get("saveFile"),
        )
        return new_object

    def run(self, tmp=None, task_vars=None):
        self._task.diff = False
        self._result = super(ActionModule, self).run(tmp, task_vars)
        self._result["changed"] = False
        _, validated_arguments = self.validate_argument_spec(
            argument_spec=argument_spec,
            mutually_exclusive=mutually_exclusive,
            required_if=required_if,
            required_one_of=required_one_of,
            required_together=required_together,
        )
        params = {k: v, for k, v in validated_arguments if k in self._task.args}

        ise = ISESDK(params=params)

        download_response = ise.exec(
            family="support_bundle_download",
            function="download_support_bundle",
            params=self.get_object(params),
        )

        # Check if the data is in binary format
        if download_response.headers.get("Content-Type") == "application/json":
            # Attempt to decode if JSON is expected
            response_data = download_response.data.decode("utf-8")
        else:
            # Save binary data to a file
            filename = (
                os.path.join(download_response.dirpath, download_response.filename)
                or "default_filename.bin"
            )
            with open(filename, "wb") as f:
                f.write(download_response.data)
            response_data = f"Data saved in: {filename}"

        response = dict(
            data=response_data,
            filename=download_response.filename,
            dirpath=download_response.dirpath,
            path=download_response.path,
        )

        self._result.update(dict(ise_response=response))
        self._result.update(ise.exit_json())
        return self._result
