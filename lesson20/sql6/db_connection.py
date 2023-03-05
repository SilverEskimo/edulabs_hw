import psycopg2


class DBConnector:
    def __init__(self):
        self._db_name = "imdb_top"
        self._connection = psycopg2.connect(
            host="localhost",
            port=5432,
            database="edu_labs",
            user="postgres"
        )

    def check_if_movie_in_db(self, movie):
        query = f"""
            select * from {self._db_name}
            where movie_name = '{movie.title()}'
        """
        with self._connection:
            with self._connection.cursor() as cur:
                try:
                    cur.execute(query)
                    res = cur.fetchone()
                    if res:
                        return res[1], res[2]
                    return None
                except (Exception, psycopg2.DatabaseError) as e:
                    print(f"Error occurred {e}")
                finally:
                    self._connection.close()

    def return_with_min_rating(self, min_rating):
        query = f'''
            select * from {self._db_name}
            where rating >= {min_rating}
        '''
        with self._connection as conn:
            res_list = []
            with conn.cursor() as cur:
                try:
                    cur.execute(query)
                    res = cur.fetchall()
                    if res:
                        for r in res:
                            res_list.append(r[0])
                        return res_list
                    return None
                except(Exception, psycopg2.DatabaseError) as e:
                    print(e)
                finally:
                    conn.close()
