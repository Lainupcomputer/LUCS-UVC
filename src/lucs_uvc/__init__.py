from urllib import request, error
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
        self.version_names = {0: "Main", 1: "Secondary", 2: "Patch", 3: "Fix"}
        self.logger = logging.getLogger(__name__)
        logging.basicConfig(level=logging.INFO)

    def get_external_versions(self) -> list:
        """Fetch external versions from the version server.

        Returns:
            list: A list containing version information.
        """
        try:
            with request.urlopen(self.version_server) as req:
                data = req.read().decode('UTF-8')
                match = re.search(f'{self.app_name}_version==([\d.]+)', data)
                if match:
                    return match.group(1).split('.')
                else:
                    self.logger.error("Version information not found in server response.")
                    return []
        except error.URLError as e:
            self.logger.error("Error fetching version information: %s", e)
            return []

    def check_version(self) -> str:
        """Check if the current version is up to date.

        Returns:
            str: A message indicating the status of the version check.
        """
        if not re.match(r'^\d+(\.\d+){3}$', self.app_version):
            return "Invalid version format"

        data = self.get_external_versions()
        if not data:
            return "Failed to retrieve external versions."

        d_ver_s = data
        v_ver_s = self.app_version.split(".")

        if len(d_ver_s) != len(v_ver_s):
            return "Version format mismatch between local and external versions."

        success_msg = ""
        update_needed = False

        for i in range(len(d_ver_s)):
            if d_ver_s[i] != v_ver_s[i]:
                diff = abs(int(d_ver_s[i]) - int(v_ver_s[i]))
                if diff > 2:
                    return "Version difference is too large, please update"
                else:
                    success_msg += (f"({self.app_name}) {self.version_names[i]}: remote:{d_ver_s[i]} current:{v_ver_s[i]}"
                                    f", Update recommended.\n")
                    update_needed = True
                    break

        if not update_needed:
            success_msg = f"({self.app_name}) is up to date. ({self.app_version})"
        self.logger.info(success_msg)
        return success_msg
