import argparse

greetings = {
    "english": "Hello",
    "french": "Bonjour",
    "german": "Hallo",
    "italian": "Ciao",
    "spanish": "Kiuvas",
}


def handle_args():
    """Parse and return arguments"""
    # These following lines add arguments and help text showed when user runs
    # python greet.py --help
    parser = argparse.ArgumentParser(description="Generate a greeting.")
    parser.add_argument("first_name", help="First name of person to greet")
    parser.add_argument("last_name", help="Last name of person to greet")
    # The following line adds an optional argument. Also limits the choices to
    # those pre-defined in the dictionary above. Different choices error out.
    # If user does not provide value, it defaults to english.
    parser.add_argument(
        "-l",
        "--language",
        help="Language of greeting",
        choices=greetings.keys(),
        default="english",
    )

    return parser.parse_args()


def main():
    """Entrypoint to script."""
    # User will need to enter the following prompt:
    # python greet.py Joe Black
    args = handle_args()
    # Setting greeting message to the appropriate language.
    greeting = greetings[args.language]
    print(f"{greeting}, {args.first_name} {args.last_name}.")


if __name__ == "__main__":
    main()
