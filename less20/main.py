import psycopg2


def query(query_str: str, args=(), many=True) -> list | None:
    with psycopg2.connect(
        dbname="shop",
        host="localhost",
        user="postgres",
        password="admin",
        port="5432",
    ) as connection:
        with connection.cursor() as cursor:
            cursor.execute(query_str, args)
            try:
                if many:
                    return cursor.fetchall()
                return cursor.fetchone()
            except Exception as error:
                return error


def select_db() -> list[tuple[any]] | None:
    return query("SELECT id, name, count, price FROM books", many=True)


def insert_db(name: str, count: int, price: float) -> None:
    query(
        "INSERT INTO books (name, count, price) VALUES (%s, %s, %s);",
        (name, count, price),
    )


if __name__ == "__main__":
    insert_db("test", 10, 10.0)
    print(select_db())
