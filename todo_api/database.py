from todo_api.database_connection import get_database


def get_db():

    return get_database()


def get_users():

    return get_db().users


def get_todos():

    return get_db().todos