from astro_sign.datamodel import SqlAlchemyBase
from .session import AstroSession


def reset_db():
    SqlAlchemyBase.metadata.drop_all(AstroSession.engine)


def setup_db():
    SqlAlchemyBase.metadata.create_all(AstroSession.engine)
