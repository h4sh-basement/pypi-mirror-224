from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, Session
from .models import Base
from contextlib import contextmanager, AbstractContextManager
from typing import Callable
import logging


def get_db_url(config: dict):
    return f"postgresql://{config['USER']}:{config['PASSWORD']}@{config['HOST']}:{config['PORT']}/{config['DB_NAME']}"


logger = logging.getLogger(__name__)


class PsqlDatabase:
    def __init__(self, db_config: dict, engine=None) -> None:
        db_url = get_db_url(db_config)
        self._engine = engine or create_engine(db_url, echo=True)
        self._session_factory = sessionmaker(
            self._engine,
        )

    def create_db(self):
        Base.metadata.create_all(self._engine)

    def drop_db(self):
        Base.metadata.drop_all(self._engine)

    @contextmanager
    def session(self) -> Callable[..., AbstractContextManager[Session]]:
        session: Session = self._session_factory()
        try:
            yield session
        except Exception:
            logger.exception("Session rollback because of exception")
            session.rollback()
            raise
        finally:
            session.close()
