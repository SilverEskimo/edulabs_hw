import psycopg2


class DBConnector:
    def __init__(self):
        self._connection = psycopg2.connect(
            host="localhost",
            port=5432,
            database="bank",
            user="postgres"
        )

    def get_accounts(self, filters: bool | dict = False):
        res_to_return = []
        if filters:
            query_list = []
            for f in filters.keys():
                if f.startswith("from_"):
                    query_list.append(f"{f.replace('from_', '')} >= %s")
                elif f.startswith("to_"):
                    query_list.append(f"{f.replace('to_', '')} <= %s")
                else:
                    query_list.append(f"{f} = %s")
            query = f"""
                        select * from accounts
                        where {" AND ".join(query_list)}
                    """
        else:
            query = '''
                        SELECT * from accounts ;
                    '''
        with self._connection as conn:
            with conn.cursor() as cur:
                cur.execute(query, tuple(filters.values()) if filters else None)
                res = cur.fetchall()
                if res:
                    print(res)
                    for r in res:
                        res_to_return.append(
                            {
                                "account_id": r[0],
                                "balance": r[1],
                                "max_limit": r[2]
                            }
                        )
                else:
                    return None
        return res_to_return
