"""Module for interpreting our processed audio and execution commands.

Works in conjunction with the botState package to define behaviour in handling
responses, and the action package which houses definitions for everything the
application can do.
"""

import prototypeDeMa.botState as STATE


class ActionReader():
    """The ActionReader takes a response as a command and figures out what to
    do with it.

    The ActionReader may be created in an instance of MicrophoneStream.

    What the class decides to do with the input is determined by the 'state.'
    When LISTENING, the it is waiting for commands as normal. When ASKING,
    it is awaiting further input for the previous command; it need more info.
    SLEEPING is when it will not act on commands, except for 'wake.'
    """

    def __init__(self, state=STATE.LISTENING):
        """Create an instance of this class, LISTENING by default."""

        self.state = state

    def readAction(self, response):
        """Reads our audio 'response' as input and does something with it.

        How the 'response' is handled is determined by the state
        
        Args:
            response (string): Our processed audio as input.
        """

        self.state.interpretAction(response)
