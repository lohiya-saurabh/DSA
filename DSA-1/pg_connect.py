import psycopg2

conn = psycopg2.connect(
    database='gurunanda_reporting',
    host='growisto-rds-in-2.cjvlpxovny5i.us-east-1.rds.amazonaws.com',
    user='admin',
    password='PfdnabaquPEiFEsvxUK4',
    port='5432'
)

cursor = conn.cursor()

print(cursor.execute(
    'select min(date) as min_date, max(date) as max_date from sp_advertised_product_view'))

print(psycopg2)
