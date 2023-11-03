import sqlite3


class Database:
    @staticmethod
    def query(
        db: str, sql: str, args: tuple, many: bool = True
    ) -> list[tuple] or tuple:
        try:
            with sqlite3.connect(db) as connection:
                cursor = connection.cursor()
                cursor.execute(sql, args)
                if many:
                    return cursor.fetchall()
                return cursor.fetchone()
        except Exception as error:
            return error

    @staticmethod
    def create(
        db: str, table: str, columns: list[str], types: list[str]
    ) -> list[tuple] or tuple:
        return Database.query(
            db=db,
            sql="CREATE TABLE {} (id INTEGER PRIMARY KEY AUTOINCREMENT, {}) ".format(
                table,
                ", ".join([f"{col} {type}" for col, type in list(zip(columns, types))]),
            ),
            args=(),
        )

    @staticmethod
    def select(
        db: str, table: str, columns: list[str], condition: str = None, id: int = None
    ) -> list[tuple] or tuple:
        query = "SELECT id, {} FROM {} {}".format(
            ", ".join(columns), table, "WHERE " + condition if condition else None
        )
        if not id:
            return Database.query(db=db, sql=query, args=())
        return Database.query(
            db=db,
            sql=f"{query} WHERE id = ?",
            args=(id,),
            many=False,
        )

    @staticmethod
    def insert(
        db: str, table: str, columns: list[str], values: list[any]
    ) -> list[tuple]:
        return Database.query(
            db=db,
            sql="INSERT INTO {} ({}) VALUES ({})".format(
                table, ", ".join(columns), ", ".join(["?" for _ in values])
            ),
            args=values,
        )

    @staticmethod
    def update(
        db: str, table: str, columns: list[str], values: list[any], id: int
    ) -> list[tuple]:
        return Database.query(
            db=db,
            sql="UPDATE {} SET {} WHERE id = ?".format(
                table, ", ".join([f"{col} = ?" for col in columns])
            ),
            args=values + [id],
        )

    @staticmethod
    def delete(db: str, table: str, id: int) -> list[tuple]:
        return Database.query(
            db=db,
            sql="DELETE FROM {} WHERE id = ?".format(table),
            args=(id,),
        )

    @staticmethod
    def count(db: str, table: str, status: str = None) -> int:
        if status:
            query = "SELECT COUNT(*) FROM {} WHERE status = '{}'".format(table, status)
        else:
            query = "SELECT COUNT(*) FROM {}".format(table)
        return Database.query(db=db, sql=query, args=())[0][0]
