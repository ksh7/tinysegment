import psycopg2

rds_host = ''
db_name = ''
db_user = ''
db_password = ''
conn = psycopg2.connect(host=rds_host, database=db_name, user=db_user, password=db_password)
print(conn)

with conn.cursor() as cursor:
    print('writing sql... ')
    cursor.execute("CREATE TABLE segment logs ( event VARCHAR(255), source VARCHAR(255), id INT );")
    conn.commit()
    print('committed... ')

conn.close()
