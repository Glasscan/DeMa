"""The SLEEPING state.

When SLEEPING the bot should accept and handle commands, but most of these
will be ignored. Exception being those pertaining to 'waking-up.'
"""


def interpretAction(response) -> None:
    """Interpret 'responses' according to SLEEPING behaviour and execute
    an appropriate action(s).

    Args:
        response (string): Text retrieved from processed voice input.
    """
    print("Receiving: [ ", response, " ] while SLEEPING")
