import argparse
import os


def handle_args():
    """Handle arguments for script."""
    parser = argparse.ArgumentParser(description="Write a range of numbers to a file")

    parser.add_argument("path", help="Path to store file.")

    parser.add_argument(
        "-s", "--start", help="Start of range to print to file", type=int, default=1
    )
    parser.add_argument(
        "-f",
        "--finish",
        help="Finish of range to print to file.",
        type=int,
        default=100,
    )
    # The store_true is default to argument parser. If argument provided, it will set
    # The value of this argument to true. The reverse option exists: 'store_false'.
    parser.add_argument(
        "-d",
        "--create_dirs",
        help="Create directores for file output",
        action="store_true",
    )

    # Takes all inputs, run it through our parser and return an arguments object.
    return parser.parse_args()


def main():
    """Entrypoint to script."""
    args = handle_args()

    # python usable_scripts/write_file.py output/numbers/numbers.txt -s 5 -f 10 -d
    # if -d argument is present, the following if statement will pass.
    if args.create_dirs:
        # os.path.dirname(args.path) strips the filename at the end of the string,
        # leaving the directory only.
        dir_path = os.path.dirname(args.path)
        os.makedirs(dir_path, exist_ok=True)

    with open(args.path, "w") as f:
        for x in range(args.start, args.finish):
            f.write(f"{str(x)} \n")


if __name__ == "__main__":
    main()
