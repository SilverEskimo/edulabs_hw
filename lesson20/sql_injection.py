import psycopg2

if __name__ == '__main__':

    table_name = "important_data"
    with psycopg2.connect(
        host="localhost",
        port=5432,
        database="edu_labs",
        user="postgres"
    ) as conn:

        user_input = "slava'; DROP TABLE important_data; SELECT * from imdb_top WHERE movie_name = 'tony"
        with conn.cursor() as cur:
            cur.execute(f"SELECT * from {table_name} where name = '{user_input}'")
            # cur.execute(f"SELECT * from {table_name}")
            res = cur.fetchall()
            print(res)
    conn.close()


