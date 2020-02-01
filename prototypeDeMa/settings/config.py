#   for retrieving asd all configuration settings
import configparser as CP


class Config():
    def __init__(self):
        self._configFile = CP.RawConfigParser()
        self._configFile.read("prototypeDeMa/settings/config.ini")

        self.bitRate = int(self._configFile.get(
            section="USER", option="bitRate"))
        self.languageCode = self._configFile.get(
            section="USER", option="languageCode")
