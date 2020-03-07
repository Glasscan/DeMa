"""A module for controlling the bot's state"""


class State():
    """A class for handling the various states."""

    def __init__(self):
        """Create an instance of this class that is LISTENING by default."""
        pass

    def changeState(self, state):
        """Change the current state.

        Args:
            state (string): The state to change into.

        Returns:
            state (string): A string depicting the state to change into.
        """

        return str(state)

    def readAction(self, input):
        """A function to read user actions.

        This takes the input from actionReader and passes it on to one of the
        state classes to handle.

        Args:
            input (string): A string containing a command to interpret.
        """
        return 0
