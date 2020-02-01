#   import os
import prototypeDeMa.botState as STATE


class ActionReader():
    def __init__(self, state=STATE.LISTENING):
        self.state = state

    def readAction(self, response):
        self.state.interpretAction(response)
