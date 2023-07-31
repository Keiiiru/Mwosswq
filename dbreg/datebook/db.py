import os
import sqlite3


db = sqlite3.connect(os.path.join("datebook.db"))


def _get_cursor() -> sqlite3.Cursor:
    cursor = db.cursor()
    return cursor


def _init_db():
    cursor = _get_cursor()
    stmt = """
            create table if not exists date(
                id integer primary key,
                day_of_week varchar(255),
                activity_for_the_day text,
                user_id bigint
            );
    """
    cursor.executescript(stmt)
    db.commit()


def add_mark(Day_of_week: str, Activity_for_the_day: str, user_id: int):
    cursor = _get_cursor()
    stmt = (
        "insert into date(Day_of_week, Activity_for_the_day, user_id) values (?, ? ,?)"
    )
    cursor.execute(stmt, (Day_of_week, Activity_for_the_day, user_id))
    db.commit()


def get_marks(user_id: int):
    cursor = _get_cursor()
    stmt = "select*from date where user_id = ? "
    res = cursor.execute(stmt, (user_id,))
    data = res.fetchall()
    return data
