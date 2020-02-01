#   All actions which pertain to the settings of the bot
import configparser as CP


def updateBotName(newBotName):
    config = CP.RawConfigParser()
    config.read("config.ini")
    config.set("USER", newBotName, "Hugo is the one")
    with open("config.ini", 'w') as c:
        config.write(c)
        print("The bot is now named:", c.get("USER", "botName"))
