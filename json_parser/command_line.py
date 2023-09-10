import argparse


def create_argparser() -> argparse.ArgumentParser:
    argparser = argparse.ArgumentParser(description="A JSON parser")
    argparser.add_argument(
        "filename", type=str, help="Path to the JSON file to be parsed"
    )

    return argparser


def parse_args(argparser: argparse.ArgumentParser) -> argparse.Namespace:
    args = argparser.parse_args()
    return args
