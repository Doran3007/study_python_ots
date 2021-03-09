from db_helper import User, Engine, Connection, get_connection, get_user
from unittest import mock


class TestUser:
    def test_init(self):
        username = "username"
        user = User(username)
        assert user.username == username


def test_get_connection():
    conn = get_connection()
    assert isinstance(conn, Connection)
    assert isinstance(conn.engine, Engine)


@mock.patch("db_helper.get_connection")
def test_get_user(mocked_get_connection):
    username = "username"
    res = get_user(username=username)
    mocked_conn_get_user = mocked_get_connection.return_value.get_user
    expected_res = mocked_conn_get_user.return_value
    assert res is expected_res
    mocked_conn_get_user.assert_called()
    mocked_conn_get_user.assert_called_once()
    mocked_conn_get_user.assert_called_once_with(username)


