"""Module for managing configuration settings."""

import configparser as CP


class Config():
    """Class made to handle everything related to settings and configuration.

    Attributes:
        _configFile(RawConfigParser): For retrieving the settings in config.ini
        bitRate (int): The retreived bit rate.
        languageCode (string): The retreived language to use.
    """

    def __init__(self):
        """Create an instance of Config"""

        self._configFile = CP.RawConfigParser()
        self._configFile.read("prototypeDeMa/settings/config.ini")

        self.bitRate = int(self._configFile.get(
            section="USER", option="bitRate"))
        self.languageCode = self._configFile.get(
            section="USER", option="languageCode")
