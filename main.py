import argparse
import sys    
    
def main():
    parser = argparse.ArgumentParser(
        description="Hit - A simple git clone"
    )
    subparsers = parser.add_subparsers(
        dest="command",
        help="Available commands"
    )

    # init command
    init_parser = subparsers.add_parser("init", help="Initialize a new repository")
    add_parser = subparsers.add_parser("add", help="Adding a new file to staging")

    args = parser.parse_args()

    # Shows the help message when no arguments are passed
    if not args.command:
        parser.print_help()
        return

    # When the user initialized the repository
    try:
        if args.command == "init":
            print(args.command)
    except Exception as e:
        print(f"Error: {e}")
        sys.exit(1)

main()