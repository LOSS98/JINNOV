import uuid
import time
from flask import session
from models.database import objects, sql_connector


class Track:
    def __init__(self, session_id: str) -> None:
        self.session_id: str = session_id
        self.paths: list[objects.UserPath] = []

    def register_page_enter(self, page: str):
        if len(self.paths) == 0 or self.path[-1].page != page:
            now = int(time.time())
            path = objects.UserPath(None, self.session_id, now, None, page)
            sql_connector.sql_connector.upsert_user_path(path)
            if len(self.paths) > 0 and self.paths[-1].end_date is None:
                self.paths[-1].end_date = now
                sql_connector.sql_connector.upsert_user_path(self.paths[-1])
            self.paths.append(path)


tracks: dict[str, Track] = {}


def get_or_create_current_track() -> Track:
    session_id = session.get("track")
    if session_id is not None and session_id in tracks:
        return tracks[session_id]
    else:
        session_id = uuid.uuid4()
        session["track"] = session_id
        return Track(session_id)
