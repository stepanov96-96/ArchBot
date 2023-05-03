from . import engine, models
from sqlalchemy.orm import Session


def add_user(telegram_id, fio, flat, account_number):
    with Session(engine) as session:
        session.add(models.User(
            telegram_id=telegram_id,
            fio=fio,
            flat=flat,
            account_number=account_number
        ))
        session.commit()