from json_parser.command_line import create_argparser, parse_args
from json_parser.core import parse


def main():
    argparser = create_argparser()
    args = parse_args(argparser)

    with open(args.filename, "r", encoding="utf8") as json_file:
        json_contents = json_file.read()
        parsing_result = parse(json_contents)

    if parsing_result is False:
        exit(1)


if __name__ == "__main__":
    main()
