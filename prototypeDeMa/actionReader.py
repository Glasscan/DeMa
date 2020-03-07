"""Module for interpreting our processed audio and execution commands.

Works in conjunction with the botState package to define behaviour in handling
responses, and the action package which houses definitions for everything the
application can do.
"""

import prototypeDeMa.botState.asking as ASKING
import prototypeDeMa.botState.listening as LISTENING
import prototypeDeMa.botState.sleeping as SLEEPING


class ActionReader():
    """The ActionReader takes a response as a command and figures out what to
    do with it.

    The ActionReader may be created in an instance of MicrophoneStream.

    What the class decides to do with the input is determined by the 'state.'
    When LISTENING, the it is waiting for commands as normal. When ASKING,
    it is awaiting further input for the previous command; it need more info.
    SLEEPING is when it will not act on commands, except for 'wake.'

    Attributes:
        _LISTENING (State): An instance of a LISTENING state.
        _SLEEPING (State): An instance of a SLEEPING state.
        _ASKING (State): An instance of an ASKING state.
        states (dictionary): A dictionary with the available states.
        currentState (State): The current state, accessed from the dictionary.
    """

    def __init__(self):
        """Create an instance of this class that is LISTENING by default."""

        self._LISTENING = LISTENING.Listening()
        self._SLEEPING = SLEEPING.Sleeping()
        self._ASKING = ASKING.Asking()
        self.states = {"LISTENING": self._LISTENING,
                       "ASKING": self._ASKING,
                       "SLEEPING": self._SLEEPING}
        self.currentState = self.states["LISTENING"]

    def readAction(self, input):
        """Reads our audio as input and does something with it.

        How the input is handled is determined by the state.

        Args:
            input (string): Our processed audio as input.
        """

        ret = self.currentState.readAction(input)
        if(ret in self.states):
            self.changeState(ret)

    def changeState(self, state):
        self.currentState = self.states[state]
