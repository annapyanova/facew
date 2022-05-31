import psycopg2

def test_database():
    conn = psycopg2.connect(dbname='productDb', user='admin', password='admin1234', host='postgresql_database')
    cursor = conn.cursor()
    cursor.execute("select * from facew limit 1")
    assert conn != None
    assert cursor != None
    assert cursor.fetchall() != []
    
