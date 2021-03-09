URL = "sqlite:///:memory:"

class User:
    def __init__(self, username):
        self.username = username

    @classmethod
    def get_admin(cls):
        return cls("admin")

    def __str__(self):
        return self.username


class Engine:
    def __init__(self, url):
        self.url = url


class Connection:
    def __init__(self, engine):
        self.engine = engine

    def get_user(self, username):
        return User(username)

    def get_admin(self):
        return self.get_user("admin")


def get_engine(url=URL):
    return Engine(url=url)


def get_connection(engine=None):
    if engine is None:
        engine = get_engine()
    return Connection(engine=engine)


def get_user(username):
    conn = get_connection()
    return conn.get_user(username)