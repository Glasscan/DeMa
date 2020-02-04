"""The ASKING state.

When ASKING, the bot is looking for additional input so it can execute the
previously given command.
"""


def interpretAction(response) -> None:
    """Interpret 'responses' according to ASKING behaviour and execute
    an appropriate action(s).

    Args:
        response (string): Text retrieved from processed voice input.
    """

    print("Receiving: [ ", response, " ] while ASKING")
