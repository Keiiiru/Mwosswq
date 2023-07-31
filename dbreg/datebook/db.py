<<<<<<< HEAD
import os
import sqlite3


db = sqlite3.connect(os.path.join("datebook.db"))

=======
import os 
import sqlite3 


db = sqlite3.connect(os.path.join('datebook.db'))
>>>>>>> 60c7b1199ae79e6c72f22cdce19fa8d8f77d16ee

def _get_cursor() -> sqlite3.Cursor:
    cursor = db.cursor()
    return cursor

<<<<<<< HEAD

=======
>>>>>>> 60c7b1199ae79e6c72f22cdce19fa8d8f77d16ee
def _init_db():
    cursor = _get_cursor()
    stmt = """
            create table if not exists date(
                id integer primary key,
<<<<<<< HEAD
                day_of_week varchar(255),
                activity_for_the_day text,
=======
                Day_of_week varchar(255),
                Activity_for_the_day text,
>>>>>>> 60c7b1199ae79e6c72f22cdce19fa8d8f77d16ee
                user_id bigint
            );
    """
    cursor.executescript(stmt)
    db.commit()

<<<<<<< HEAD

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
=======
def add_mark(Day_of_week: str, Activity_for_the_day: str, user_id: int):
    cursor = _get_cursor()
    stmt = "insert into date(Day_of_week, Activity_for_the_day, user_id) values (?, ? ,?)"
    cursor.execute(stmt, (Day_of_week,Activity_for_the_day,user_id))
    db.commit()

def get_marks(user_id: int):
    cursor = _get_cursor()
    stmt = "select*from date where user_id = ? " 
    res = cursor.execute(stmt, (user_id, ))
    data = res.fetchall() 
    return data
>>>>>>> 60c7b1199ae79e6c72f22cdce19fa8d8f77d16ee
