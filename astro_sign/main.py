from .arguments import parse_arguments
from .crud import get_predictions_for_sign
from .crud import get_recent_users
from .db_utilities import prefill_database, print_entries, reset_db, setup_db


# noinspection PyArgumentList
def main():
    arguments = parse_arguments()

    if arguments.prefill:
        reset_db()
    setup_db()

    if arguments.prefill:
        prefill_database()

    if arguments.users:
        users = get_recent_users()
        print_entries(users)

    if arguments.predictions:
        sign = arguments.predictions
        predictions = get_predictions_for_sign(sign)
        print_entries(predictions)


if __name__ == '__main__':
    main()
