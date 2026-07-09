import sqlite3


DB_NAME = "news.db"



def init_db():

    conn = sqlite3.connect(DB_NAME)

    cursor = conn.cursor()


    cursor.execute("""
    CREATE TABLE IF NOT EXISTS news(

        link TEXT PRIMARY KEY

    )
    """)


    conn.commit()

    conn.close()



def is_duplicate(link):

    conn = sqlite3.connect(DB_NAME)

    cursor = conn.cursor()


    cursor.execute(

        "SELECT link FROM news WHERE link=?",

        (link,)

    )


    result = cursor.fetchone()


    conn.close()


    return result is not None




def save_news(link):

    conn = sqlite3.connect(DB_NAME)

    cursor = conn.cursor()


    cursor.execute(

        "INSERT OR IGNORE INTO news(link) VALUES(?)",

        (link,)

    )


    conn.commit()

    conn.close()
