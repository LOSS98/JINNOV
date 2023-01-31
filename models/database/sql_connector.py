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

    def get_all_etudes(self) -> list:
        query = "SELECT e.id,e.created_at,e.created_by,e.customer_name,e.customer_link,e.body,e.image,e.attachements,CONCAT(membre.first_name, ' ', membre.last_name) FROM etude e INNER JOIN membre ON e.created_by = membre.id"
        c = self.connection.cursor(prepared=True)
        c.execute(query)
        return [Etude(*r) for r in c.fetchall()]

    def get_etude(self, id):
        query = "SELECT e.id,e.created_at,e.created_by,e.customer_name,e.customer_link,e.body,e.image,e.attachements,CONCAT(membre.first_name, ' ', membre.last_name) FROM etude e INNER JOIN membre ON e.created_by = membre.id WHERE e.id=%s LIMIT 1"
        c = self.connection.cursor(prepared=True)
        c.execute(query, (id,))
        row = c.fetchone()
        return Etude(*row) if row is not None else None

    def get_all_articles(self) -> list:
        query = "SELECT a.id,a.created_by,a.created_at,a.title,a.body,a.description,a.image,a.attachements,CONCAT(membre.first_name, ' ', membre.last_name),a.highlighted FROM article a INNER JOIN membre ON a.created_by = membre.id"
        c = self.connection.cursor(prepared=True)
        c.execute(query)
        return [Article(*r) for r in c.fetchall()]

    def get_article(self, id):
        query = "SELECT a.id,a.created_by,a.created_at,a.title,a.body,a.description,a.image,a.attachements,CONCAT(membre.first_name, ' ', membre.last_name),a.highlighted FROM article a INNER JOIN membre ON a.created_by = membre.id WHERE a.id=%s LIMIT 1"
        c = self.connection.cursor(prepared=True)
        c.execute(query, (id,))
        row = c.fetchone()
        return Article(*row) if row is not None else None

    def get_all_membres(self) -> list:
        query = "SELECT id,first_name,last_name,email,phone_number,pole,poste,picture_path,active FROM membre"
        c = self.connection.cursor(prepared=True)
        c.execute(query)
        return [Membre(*r) for r in c.fetchall()]

    def get_admins(
        self,
        id: int = None,
        full_name: str = None,
        email: str = None,
        password: str = None,
    ) -> list:
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
        query = "REPLACE INTO etude(id,created_at,created_by,customer_name,customer_link,body,image,attachements) VALUES (%s,%s,%s,%s,%s,%s,%s,%s)"
        c = self.connection.cursor(prepared=True)
        c.execute(
            query,
            (
                etude.id,
                etude.created_at,
                etude.created_by,
                etude.customer_name,
                etude.customer_link,
                etude.body,
                etude.image,
                etude.attachements,
            ),
        )
        self.connection.commit()

    def upsert_article(self, article: Article):
        query = """REPLACE INTO article(id,created_by,created_at,title,body,description,image,attachements,highlighted)
        VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s)"""
        c = self.connection.cursor(prepared=True)
        c.execute(
            query,
            (
                article.id,
                article.created_by,
                article.created_at,
                article.title,
                article.body,
                article.description,
                article.image,
                article.attachements,
                article.highlighted,
            ),
        )
        self.connection.commit()

    def upsert_admin(self, admin: Admin):
        query = "REPLACE INTO admin(id,full_name,email,password,salt) VALUES (%s,%s,%s,%s,%s)"
        c = self.connection.cursor(prepared=True)
        c.execute(
            query,
            (
                admin.id if admin.id is not None else "NULL",
                admin.full_name,
                admin.email,
                admin.password,
                admin.salt,
            ),
        )
        self.connection.commit()

    def upsert_membre(self, membre: Membre):
        query = """REPLACE INTO membre(id,first_name,last_name,email,phone_number,pole,poste,picture_path,active)
        VALUES (%s,%s,%s,%s,%s,%s,%s,%s)"""
        c = self.connection.cursor(prepared=True)
        c.execute(
            query,
            (
                membre.id,
                membre.first_name,
                membre.last_name,
                membre.email,
                membre.phone_number,
                membre.pole,
                membre.poste,
                membre.picture_path,
                membre.active,
            ),
        )
        self.connection.commit()

    def upsert_user_path(self, user_path: UserPath):
        query = "REPLACE INTO user_path(id,session_id,start_date,end_date,page) VALUES (%s,%s,%s,%s,%s)"
        c = self.connection.cursor(prepared=True)
        c.execute(
            query,
            (
                user_path.id if user_path.id is not None else "NULL",
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

    def create_where_filter(self, **kwargs) -> tuple:
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
