import psycopg2

try:
    conn = psycopg2.connect(user='webdb', password='webdb', host='192.168.1.48', port='5432', database='webdb')

except Exception as e:
    print(f'error: {e}')

finally:
    'conn' in locals() and conn and conn.close()

