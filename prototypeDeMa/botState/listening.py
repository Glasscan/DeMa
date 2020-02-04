"""The LISTENING state.

When LISTENING the bot should handle commands as normal.
"""


def interpretAction(response) -> None:
    """Interpret 'responses' according to LISTENING behaviour and execute
    an appropriate action(s).

    Args:
        response (string): Text retrieved from processed voice input.
    """

    print("Receiving: [ ", response, " ] while LISTENING")
