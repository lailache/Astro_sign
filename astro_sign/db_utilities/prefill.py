from astro_sign.datamodel import AppUser, Prediction, UserPreference, ZodiacSign
from .session import AstroSession


def prefill_database():
    with AstroSession.get_session() as session:
        user1 = AppUser(user_name='John Doe', birth_date='1980-05-22',
                        birth_time='10:30:00', birth_place='Moscow')
        user2 = AppUser(user_name='Jane Smith', birth_date='1990-12-15',
                        birth_time='15:45:00', birth_place='New York')
        preference1 = UserPreference(user_id=1, language='English', theme='Dark')
        preference2 = UserPreference(user_id=2, language='Russian', theme='Light')
        sign1 = ZodiacSign(sign_id=1, sign_name='Aries', start_date='2024-03-21', end_date='2024-04-19')
        sign2 = ZodiacSign(sign_id=2, sign_name='Taurus', start_date='2024-04-20', end_date='2024-05-20')
        prediction1 = Prediction(prediction_id=1, sign_id=1, prediction_date='2024-07-01',
                                 prediction='Today is a good day for Aries.')
        prediction2 = Prediction(prediction_id=2, sign_id=2, prediction_date='2024-07-01',
                                 prediction='Taurus should avoid any financial risks today.')
        all_items = [user1, user2, preference1, preference2, sign1, sign2, prediction1, prediction2]
        session.add_all(all_items)
        session.commit()
