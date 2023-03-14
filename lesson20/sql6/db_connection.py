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
        movie_name = movie.title()
        query = f"""
            select * from {self._db_name}
            where movie_name ilike %s
        """
        try:
            with self._connection:
                with self._connection.cursor() as cur:
                    cur.execute(query, (movie_name,))
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
            where rating >= %s
            order by rating 
        '''
        try:
            with self._connection as conn:
                res_list = []
                with conn.cursor() as cur:
                    cur.execute(query, (min_rating,))
                    res = cur.fetchall()
                    if res:
                        for r in res:
                            res_list.append((r[0], r[2]))
                        return res_list
                    return None
        except(Exception, psycopg2.DatabaseError) as e:
            print(e)
        finally:
            conn.close()
