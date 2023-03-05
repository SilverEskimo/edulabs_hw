import psycopg2


if __name__ == '__main__':
    with psycopg2.connect(
        host="localhost",
        port=5432,
        database="edu_labs",
        user="postgres"
    ) as conn:
        # Access the DB with cursor (session)
        with conn.cursor() as cur:
            # Execute query
            cur.execute('SELECT version()')

            # Fetch data from the query above - can be done also with fetchmany(n) - returns list of tuples
            # another option for small tables - fetchall()
            db_version = cur.fetchone() # returns tuple
            print(db_version)

            query ='''
                select * from imdb_top;
            '''
            cur.execute(query)
            res = cur.fetchone()
            print(res)


    # Although we use 'with' we still need to close the connection as 'with' just commits the transaction
    conn.close()


