import json
import sqlite3


def create_connection(db_file):
    conn = None
    try:
        conn = sqlite3.connect(db_file)
    except sqlite3.Error as e:
        print(e)
    return conn


def create_table(conn, create_table_sql):
    try:
        c = conn.cursor()
        c.execute(create_table_sql)
    except sqlite3.Error as e:
        print(e)


def insert_data(conn, data):
    sql = ''' INSERT INTO cinemas(name, description, address_street, address_full)
              VALUES(?,?,?,?) '''
    cur = conn.cursor()
    cur.execute(sql, data)
    return cur.lastrowid


def main():
    database = r"cinemas.db"

    create_table_sql = """ CREATE TABLE IF NOT EXISTS cinemas (
                                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                                        name TEXT NOT NULL,
                                        description TEXT,
                                        address_street TEXT,
                                        address_full TEXT
                                    ); """

    conn = create_connection(database)
    if conn is not None:
        create_table(conn, create_table_sql)
    else:
        print("Ошибка! Невозможно создать подключение к базе данных.")

    with open('data-93-structure-3.json', 'r', encoding='utf-8') as f:
        data = json.load(f)
        for item in data:
            name = item['data']['general']['name']
            description = item['data']['general'].get('description', '')
            address_street = item['data']['general']['address'].get('street', '')
            address_full = item['data']['general']['address'].get('fullAddress', '')

            cinema_data = (name, description, address_street, address_full)
            insert_data(conn, cinema_data)

        conn.commit()
        conn.close()


if __name__ == '__main__':
    main()
