import psycopg2

conn = psycopg2.connect(dbname='productDb', user='admin', password='admin1234', host='postgresql_database')
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
