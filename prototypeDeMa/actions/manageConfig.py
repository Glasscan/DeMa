"""Module with all actions pertaining to management of settings."""

import configparser as CP


def updateBotName(newBotName):
    """Method to update the config file with a new [USER] botName.

    Args:
        newBotName (string): Name to replace the old one in the config file.
    """

    config = CP.RawConfigParser()
    config.read("config.ini")
    config.set("USER", newBotName, "Hugo is the one")
    with open("config.ini", 'w') as c:
        config.write(c)
        print("The bot is now named:", c.get("USER", "botName"))
