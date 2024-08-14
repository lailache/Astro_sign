from argparse import ArgumentParser


def parse_arguments():
    parser = ArgumentParser(
        prog='AstroApp',
        description='Your personal astrologer assistant',
        epilog='Discover your destiny!'
    )
    parser.add_argument(
        '-p', '--prefill',
        action='store_true',
        help='Prefill the database.'
    )
    parser.add_argument(
        '-u', '--users',
        action='store_true',
        help='List all users.'
    )
    parser.add_argument(
        '-s', '--predictions',
        metavar='sign',
        type=str,
        help='Get predictions for a specific sign.'
    )
    arguments = parser.parse_args()
    return arguments
