import psycopg2


def read(filename: str) -> list[tuple]:
    with open(file=filename, mode="r", encoding="utf-8") as file:
        return eval(file.read())


def write(filename: str, data: str):
    with open(file=filename, mode="w", encoding="utf-8") as file:
        file.write(str(data))


def query(query_str: str) -> list[tuple]:
    with psycopg2.connect(
        dbname="file_data",
        host="localhost",
        user="postgres",
        password="admin",
        port="5432",
    ) as connection:
        with connection.cursor() as cursor:
            cursor.execute(query=query_str)
            try:
                return cursor.fetchall()
            except Exception:
                cursor.execute("SELECT id, name FROM public.data")
                return cursor.fetchall()


if __name__ == "__main__":
    # Запись данных из БД в текстовый файл.
    write(filename="less12/data.txt", data=query("SELECT id, name FROM public.data"))

    # Запись данных из текстового файла в БД.
    for i in read("less12/data.txt"):
        print(
            query(
                query_str=f"INSERT INTO public.data (id, name) VALUES ('{i[0]}', '{i[1]}')"
            )
        )
