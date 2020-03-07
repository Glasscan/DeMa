"""The ASKING state.

When ASKING, the bot is looking for additional input so it can execute the
previously given command. It does NOT need to recognize its name in this state.
"""

from prototypeDeMa.botState.state import State


class Asking(State):
    """The class used when the bot is in the ASKING state."""

    def __init__(self):
        """Create an instance of this class."""
        pass

    def readAction(self, response):
        """Interpret 'responses' according to ASKING behaviour and execute
        an appropriate action(s).

        Args:
            response (string): Text retrieved from processed voice input.
        Returns:
            ret (string): A generic return value; may be None
        """

        print("Receiving: [ ", response, " ] while ASKING")
        return

    def changeState(self, state):
        """Change the current state.

        Args:
            state (string): The state to change into.

        Returns:
            state (string): A string depicting the state to change into.
        """

        return super().changeState(state)
