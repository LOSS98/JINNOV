from time import time
import uuid
from flask import session
from models import cryptography
from models.database import sql_connector
from models.database.objects import Admin

TOKEN_TIMEOUT = 30  # minutes
auth_tokens: dict[str, tuple[Admin, int]] = {}


def login(email: str, password: str) -> bool:
    admins = sql_connector.sql_connector.get_admins(email=email)
    if (
        len(admins) == 1
        and cryptography.hash(password, admins[0].salt) == admins[0].password
    ):
        token = str(uuid.uuid4())
        session["account"] = token
        auth_tokens[token] = (admins[0], int(time()) + TOKEN_TIMEOUT * 60)
        return True
    return False


def logout():
    if is_connected():
        auth_tokens.pop(session["account"])
        session.pop("account")


def is_connected():
    if session.get("account") is not None and session["account"] in auth_tokens:
        if auth_tokens[session["account"]][1] > int(time()):
            return True
        auth_tokens.pop(session["account"])
        session.pop("account")
    return False


def get_current_user():
    if is_connected():
        return auth_tokens[session["account"]][0]
    return None
