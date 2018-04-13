import pandas as pd
import psycopg2


DATA_LOCATION = "/Users/jalijuhola/git/test_app/test_data/tieliikenne_5_1.csv"

def get_vehicle_data():
    df = pd.read_csv(DATA_LOCATION, error_bad_lines=False, sep=";", low_memory=False)
    return df


def insert_data_to_postgress(table, data):
    insert_str = "INSERT INTO vehicles(ajoneuvoluokka, ajoneuvonkaytto, ensirekisterointipvm)VALUES(%s, %s, %s);"
    conn = psycopg2.connect("dbname='testdb' user='testuser' host='127.0.0.1' password='passwordi'")
    cur = conn.cursor()
    cur.execute("CREATE TABLE vehicles(ajoneuvoluokka VARCHAR(255), ajoneuvonkaytto VARCHAR(255),ensirekisterointipvm VARCHAR(255)) );")
    conn.commit()
    for index, item in data.iterrows():
        # Bulk insert with https://stackoverflow.com/questions/48683563/what-is-the-fastest-way-to-insert-rows-into-a-postgresql-database-with-geokettle might be wiser to use.
        print(index)
        cur = conn.cursor()
        cur.execute(insert_str, (item.ajoneuvoluokka, item.ajoneuvonkaytto, item.ensirekisterointipvm))
        conn.commit()
        cur.close()
