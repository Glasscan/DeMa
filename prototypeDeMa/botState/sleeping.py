"""The SLEEPING state.

When SLEEPING the bot should accept and handle commands, but most of these
will be ignored. Exception being those pertaining to 'waking-up.'
"""

from prototypeDeMa.botState.state import State


class Sleeping(State):
    """The class used when the bot is in the SLEEPING state."""

    def __init__(self):
        """Create an instance of this class."""
        pass

    def readAction(self, response):
        """Interpret 'responses' according to SLEEPING behaviour and execute
        an appropriate action(s).

        Args:
            response (string): Text retrieved from processed voice input.
        Returns:
            ret (string): A generic return value; may be None
        """

        print("Receiving: [ ", response, " ] while SLEEPING")
        return

    def changeState(self, state):
        """Change the current state.

        Args:
            state (string): The state to change into.

        Returns:
            state (string): A string depicting the state to change into.
        """

        return super().changeState(state)

    def wakeup(self):
        """Wake up; shift into the LISTENING state"""

        self.changeState("LISTENING")
