"""Module for version checking utility (UVC).

This module provides a utility class, UVC (Version Checker), which is used for
checking the version of a given application against a version server. It includes
methods to fetch external versions from the server and compare them with the
current version of the application.

The module consists of the following components:
- UVC class: A utility class for version checking.
  - Methods:
    - __init__: Initializes the UVC object with the version server URL, application
                name, and current version.
    - get_external_versions: Fetches external versions from the version server.
    - check_version: Compares the current version with the external versions and
                     provides feedback on the update status.

Dependencies:
- urllib: For making HTTP requests to fetch version information from the server.
- re: For regular expression matching to validate version formats.
- logging: For logging errors encountered during version checking.

Usage:
1. Initialize the UVC object with the version server URL, application name, and
   current version.
2. Call the check_version method to check the update status of the application.

Example:
    uvc = UVC('http://example.com/version_info', 'MyApp', '1.0.0.0')
    update_status = uvc.check_version()
    print(update_status)

Note: Ensure that the version server provides version information in a compatible
format that can be parsed by this utility.

Author: Lainupcomputersolution
Date: 2024
"""

__version__ = "0.1.0.0"
__author__ = 'Sandro Kalett'
__credits__ = 'Lainupcomputersolution'

from urllib import request
import re
import logging


class UVC:
    """Utility class for version checking."""
    def __init__(self, version_server: str, app_name: str, app_version: str):
        """Initialize the UVC object.

            Args:
                version_server (str): The URL of the version server.
                app_name (str): The name of the application.
                app_version (str): The current version of the application.
        """
        self.version_server = version_server
        self.app_name = app_name
        self.app_version = app_version
        self.version_names: dict = {0: "Main", 1: "Secondary", 2: "Patch", 3: "Fix"}

    def get_external_versions(self) -> list:
        """Fetch external versions from the version server.

        Returns:
            list: A list containing version information.
        """
        try:
            req = request.urlopen(self.version_server)
            data = req.read().decode('UTF-8')
            s = data.find(self.app_name + '_version==')
            return data[s:s + 20].split("==")
        except Exception as e:
            print("Error fetching version information:", e)
            return []

    def check_version(self) -> str:
        """Check if the current version is up to date.

        Returns:
            str: A message indicating the status of the version check.
        """
        if not re.match(r'^\d+(\.\d+){3}$', self.app_version):
            return "Invalid version format"

        data = self.get_external_versions()
        d_ver_s = data[1].split(".")
        v_ver_s = self.app_version.split(".")
        success = True
        success_l = False
        success_msg: str = ""

        for i in range(len(d_ver_s)):
            if d_ver_s[i] != v_ver_s[i]:
                diff = abs(int(d_ver_s[i]) - int(v_ver_s[i]))
                if diff > 2:
                    return "Version difference is too large, please update"
                else:
                    success_msg += (f"({self.app_name}) {self.version_names[i]}: remote:{d_ver_s[i]} current:{v_ver_s[i]}"
                                    f", Update recommended.\n")
                    success = False
                    success_l = True
                    break

        if success:
            success_msg += f"({self.app_name}) up to date. ({self.app_version})"
        else:
            if not success_l:
                success_msg += f"({self.app_name}) needs update to run properly. current: ({self.app_version}), remote: ({d_ver_s})"
        return success_msg



