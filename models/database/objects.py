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
    def __init__(self) -> None:
        pass


class Admin:
    def __init__(self) -> None:
        pass


class Membre:
    def __init__(self) -> None:
        pass


class UserPath:
    def __init__(self) -> None:
        pass
