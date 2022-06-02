import psycopg2

conn = psycopg2.connect(dbname='postgres', user='postgres', password='admin1234', host='localhost')
cursor = conn.cursor()

create_table_query = """
CREATE TABLE facew (
        o_id integer,
        class text,
        bbox_coords_xmin integer,
        bbox_coords_ymin integer,
        bbox_coords_xmax integer,
        bbox_coords_ymax integer
); 
"""
cursor.execute(create_table_query)
conn.commit()
print("Таблица успешно создана в PostgreSQL")

#cursor.execute("SELECT * FROM facew")
#print(cursor.fetchall())

