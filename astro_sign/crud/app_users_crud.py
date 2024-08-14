from astro_sign.datamodel import AppUser
from astro_sign.db_utilities import AstroSession
from astro_sign.config import PRINT_ITEMS_PER_PAGE


def get_recent_users(limit=PRINT_ITEMS_PER_PAGE, offset=0):
    with AstroSession.get_session() as session:
        query = session.query(AppUser).order_by(AppUser.user_id)
        if limit:
            query = query.limit(limit).offset(offset)
        data = query.all()
    return data
