import mysql.connector
from mysql.connector import errorcode, MySQLConnection, Error

from models.database.objects import Admin, Etude, Article, Membre, UserPath


# This class is used to connect to a database and execute SQL queries.
class SQLConnector:
    def __init__(self, user: str, password: str, host: str, database: str) -> None:
        self.connection: MySQLConnection = None
        self.user: str = user
        self.password: str = password
        self.host: str = host
        self.database: str = database

    def connect(self):
        if self.connection is None:
            try:
                self.connection = mysql.connector.connect(
                    user=self.user,
                    password=self.password,
                    host=self.host,
                    database=self.database,
                )
            except Error as err:
                if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
                    print("Unable to connect to mysql : Invalid credentials")
                elif err.errno == errorcode.ER_BAD_DB_ERROR:
                    print("Unable to connect to mysql : Database does not exist")
                else:
                    print("Unable to connect to mysql : " + err)

    def disconnect(self):
        if self.connection is not None:
            self.connection.close()

    def get_all_etudes(self) -> list[Etude]:
        query = "SELECT id,created_at,customer_name,customer_link,body FROM etude"
        c = self.connection.cursor(prepared=True)
        c.execute(query)
        return [Etude(*r) for r in c.fetchall()]

    def get_etude(self, id) -> Etude:
        query = "SELECT id,created_at,customer_name,customer_link,body FROM etude WHERE id=%s"
        c = self.connection.cursor(prepared=True)
        c.execute(query, (id,))
        row = c.fetchone()
        return Etude(*row) if row is not None else None

    def get_all_articles(self) -> list[Article]:
        query = "SELECT a.id,a.created_by,a.created_at,a.title,a.body,a.attachements,admin.full_name FROM article a INNER JOIN admin ON a.created_by = admin.id"
        c = self.connection.cursor(prepared=True)
        c.execute(query)
        return [Article(*r) for r in c.fetchall()]

    def get_article(self, id):
        query = "SELECT a.id,a.created_by,a.created_at,a.title,a.body,a.attachements,admin.full_name FROM article a INNER JOIN admin ON a.created_by = admin.id WHERE a.id=%s LIMIT 1"
        c = self.connection.cursor(prepared=True)
        c.execute(query, (id,))
        row = c.fetchone()
        return Article(*row) if row is not None else None

    def get_all_membres(self) -> list[Membre]:
        query = "SELECT first_name,last_name,email,phone_number,pole,poste,picture_path FROM membre"
        c = self.connection.cursor(prepared=True)
        c.execute(query)
        return [Membre(*r) for r in c.fetchall()]

    def get_admins(
        self,
        id: int = None,
        full_name: str = None,
        email: str = None,
        password: str = None,
    ) -> list[Admin]:
        query = "SELECT id,full_name,email,password,salt FROM admin"
        where_filter, values = self.create_where_filter(
            id=id, full_name=full_name, email=email, password=password
        )
        query += where_filter
        c = self.connection.cursor(prepared=True)
        c.execute(query, values)
        return [Admin(*r) for r in c.fetchall()]

    def get_user_path(self):
        # LATER
        pass

    def upsert_etude(self, etude: Etude):
        query = "REPLACE INTO etude(id,created_at,customer_name,customer_link,body) VALUES (%s,%s,%s,%s,%s)"
        c = self.connection.cursor(prepared=True)
        c.execute(
            query,
            (
                etude.id,
                etude.created_at,
                etude.customer_name,
                etude.customer_link,
                etude.body,
            ),
        )
        self.connection.commit()

    def upsert_article(self, article: Article):
        query = """REPLACE INTO article(id,created_by,created_at,title,body,attachements)
        VALUES (%s,%s,%s,%s,%s,%s)"""
        c = self.connection.cursor(prepared=True)
        c.execute(
            query,
            (
                article.id,
                article.created_by,
                article.created_at,
                article.title,
                article.body,
                article.attachements,
            ),
        )
        self.connection.commit()

    def upsert_admin(self, admin: Admin):
        query = "REPLACE INTO admin(id,full_name,email,password,salt) VALUES (%s,%s,%s,%s,%s)"
        c = self.connection.cursor(prepared=True)
        c.execute(
            query,
            (
                admin.id,
                admin.full_name,
                admin.email,
                admin.password,
                admin.salt,
            ),
        )
        self.connection.commit()

    def upsert_membre(self, membre: Membre):
        query = """REPLACE INTO membre(first_name,last_name,email,phone_number,pole,poste,picture_path)
        VALUES (%s,%s,%s,%s,%s,%s)"""
        c = self.connection.cursor(prepared=True)
        c.execute(
            query,
            (
                membre.first_name,
                membre.last_name,
                membre.email,
                membre.phone_number,
                membre.pole,
                membre.poste,
                membre.picture_path,
            ),
        )
        self.connection.commit()

    def upsert_user_path(self, user_path: UserPath):
        query = "REPLACE INTO user_path(id,session_id,start_date,end_date,page) VALUES (%s,%s,%s,%s,%s)"
        c = self.connection.cursor(prepared=True)
        c.execute(
            query,
            (
                user_path.id,
                user_path.session_id,
                user_path.start_date,
                user_path.end_date,
                user_path.page,
            ),
        )
        self.connection.commit()

    def delete_etude(self, etude: Etude):
        query = "DELETE FROM etude WHERE id=%s"
        c = self.connection.cursor(prepared=True)
        c.execute(query, (etude.id,))
        self.connection.commit()

    def delete_article(self, article: Article):
        query = "DELETE FROM article WHERE id=%s"
        c = self.connection.cursor(prepared=True)
        c.execute(query, (article.id,))
        self.connection.commit()

    def delete_admin(self, admin: Admin):
        query = "DELETE FROM admin WHERE id=%s"
        c = self.connection.cursor(prepared=True)
        c.execute(query, (admin.id,))
        self.connection.commit()

    def delete_membre(self, membre: Membre):
        query = "DELETE FROM membre WHERE id=%s"
        c = self.connection.cursor(prepared=True)
        c.execute(query, (membre.id,))
        self.connection.commit()

    def create_where_filter(self, **kwargs) -> tuple[str, list]:
        """
        It takes a dictionary of key-value pairs, filters out the ones where the value is None, and
        returns a tuple of a string and a list.

        The string is a SQL WHERE clause, and the list is the values to be passed to the SQL query.

        The function is used like this:

        # Python
        where_filter = create_where_filter(name="John", age=None, height=180)
        sql = f"SELECT * FROM users {where_filter[0]}"
        cursor.execute(sql, where_filter[1])
        :return: A tuple of two elements.
        """
        filtered = {k: v for k, v in kwargs.items() if v is not None}
        if len(filtered) > 0:
            return (
                " WHERE " + " AND ".join([f"{k}=%s" for k in filtered.keys()]),
                list(filtered.values()),
            )
        return "", []


sql_connector: SQLConnector = None
