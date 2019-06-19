import psycopg2

import config


def test_insert():
    try:
        conn = psycopg2.connect(**config.db)
        cursor = conn.cursor()

        cursor.execute("insert into pet values('까비', '동화', 'dog', 'm', '2003-01-02', null);")

    except Exception as e:
        print('error: {0}'.format(e))
    finally:
        cursor and cursor.close()
        conn and (conn.commit() or conn.close())


def test_select():
    try:
        conn = psycopg2.connect(**config.db)
        cursor = conn.cursor()

        cursor.execute("select * from pet;")
        records = cursor.fetchall()

        for record in records:
            print(record, type(record))

    except Exception as e:
        print('error: {0}'.format(e))
    finally:
        cursor and cursor.close()
        conn and conn.close()


def test_delete():
    try:
        conn = psycopg2.connect(**config.db)
        cursor = conn.cursor()

        cursor.execute("delete from pet where name = '까비';")

    except Exception as e:
        print('error: {0}'.format(e))
    finally:
        cursor and cursor.close()
        conn and (conn.commit() or conn.close())


def test_update():
    try:
        conn = psycopg2.connect(**config.db)
        cursor = conn.cursor()

        cursor.execute("update pet set owner = '양동화' where name = '까비';")

    except Exception as e:
        print('error: {0}'.format(e))
    finally:
        cursor and cursor.close()
        conn and (conn.commit() or conn.close())


def main():
    test_insert()
    test_select()
    print('========================')
    test_update()
    test_select()
    print('========================')
    test_delete()
    test_select()


__name__ == '__main__' and main()