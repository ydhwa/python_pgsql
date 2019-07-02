import psycopg2

try:
    conn = psycopg2.connect(user='webdb', password='webdb', host='127.0.0.1', port='5432', database='webdb')
    # conn = psycopg2.connect(user='webdb', password='webdb', host='192.168.219.101', port='5432', database='webdb')

    cursor = conn.cursor()
    cursor.execute('select version()')
    record = cursor.fetchone()

    print('connected to -', record)

except Exception as e:
    print(f'error: {e}')

finally:
    'cursor' in locals() and cursor and cursor.close()
    'conn' in locals() and conn and conn.close()

