from flask import session
from models import cryptography
from models.database import sql_connector


def login(email: str, password: str) -> bool:
    admins = sql_connector.sql_connector.get_admins(email=email)
    if (
        len(admins) == 1
        and cryptography.hash(password, admins[0].salt) == admins[0].password
    ):
        session["account"] = admins[0].email
        return True
    return False


def logout():
    if is_connected():
        session.pop("account")


def is_connected(database_check: bool = False):
    if session.get("account") is None:
        return False
    if database_check:
        return (
            len(sql_connector.sql_connector.get_admins(email=session["account"])) == 1
        )
    return True


def get_current_user():
    if is_connected(database_check=True):
        admins = sql_connector.sql_connector.get_admins(email=session["account"])
        return admins[0] if len(admins) == 1 else None
    return None
