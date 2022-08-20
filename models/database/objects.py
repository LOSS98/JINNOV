from datetime import datetime


class Etude:
    def __init__(
        self,
        id: int,
        created_at: int,
        customer_name: str,
        customer_link: str,
        body: str,
    ) -> None:
        self.id = id
        self.created_at = created_at
        self.customer_name = customer_name
        self.customer_link = customer_link
        self.body = body


class Article:
    def __init__(
        self,
        id: int,
        created_by: int,
        created_at: int,
        title: str,
        body: str,
        image: str,
        attachements: str,
        author_name: str,
    ) -> None:
        self.id = id
        self.created_by = created_by
        self.created_at = created_at
        self.title = title
        self.body = body
        self.image = image
        self.attachements = attachements
        self.author_name = author_name

    def strDate(self):
        return datetime.fromtimestamp(self.created_at).strftime("%d/%m/%Y")


class Admin:
    def __init__(
        self, id: int, full_name: str, email: str, password: str, salt: str
    ) -> None:
        self.id = id
        self.full_name = full_name
        self.email = email
        self.password = password
        self.salt = salt


class Membre:
    def __init__(
        self,
        id: int,
        first_name: str,
        last_name: str,
        email: str,
        phone_number: str,
        pole: str,
        poste: str,
        picture_path: str,
    ) -> None:
        self.id = id
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.phone_number = phone_number
        self.pole = pole
        self.poste = poste
        self.picture_path = picture_path


class UserPath:
    def __init__(
        self, id: int, session_id: str, start_date: int, end_date: int, page: str
    ) -> None:
        self.id = id
        self.session_id = session_id
        self.start_date = start_date
        self.end_date = end_date
        self.page = page
