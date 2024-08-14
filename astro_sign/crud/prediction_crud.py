from astro_sign.datamodel import Prediction, ZodiacSign
from astro_sign.db_utilities import AstroSession


def get_predictions_for_sign(zodiac_sign: str):
    """Retrieves predictions for the specified zodiac sign.

        sign: The name of the zodiac sign.

    Returns:
        A list of Prediction objects containing predictions for the given sign.
    """
    with AstroSession.get_session() as session:
        query = session.query(Prediction).join(ZodiacSign).filter(ZodiacSign.sign_name == zodiac_sign)
        data = query.all()
    return data
