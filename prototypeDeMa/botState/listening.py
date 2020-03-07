"""The LISTENING state.

When LISTENING the bot should handle commands as normal.
"""

from prototypeDeMa.botState.state import State


class Listening(State):
    """The class used when the bot is in the LISTENING state."""

    def __init__(self):
        """Create an instance of this class."""
        pass

    def readAction(self, response):
        """Interpret 'responses' according to LISTENING behaviour and execute
        an appropriate action(s).

        Args:
            response (string): Text retrieved from processed voice input.

        Returns:
            ret (string): A generic return value; may be None
        """

        print("Receiving: [ ", response, " ] while LISTENING")
        return

    def changeState(self, state):
        """Change the current state.

        Args:
            state (string): The state to change into.

        Returns:
            state (string): A string depicting the state to change into.
        """

        return super().changeState(state)
