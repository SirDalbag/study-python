from flask import Flask, render_template, request, redirect, url_for
from utilites import Database

app = Flask(
    __name__,
    static_url_path="/static",
    static_folder="static",
    template_folder="templates",
)

db = "database/tasks.db"
table = "tasks"
columns = ["task", "date", "status"]


class Views:
    class Base:
        @staticmethod
        @app.route("/", methods=["GET", "POST"])
        def home():
            if request.method == "POST":
                task_filter = request.form.get("task_filter")
                tasks = Database.select(
                    db=db,
                    table=table,
                    columns=columns,
                    condition="status = '{}'".format(task_filter),
                )
            else:
                tasks = Database.select(
                    db=db,
                    table=table,
                    columns=columns,
                    condition="status = 'uncompleted'",
                )
            total_tasks = Database.count(db=db, table=table)
            completed_tasks = Database.count(db=db, table=table, status="completed")
            uncompleted_tasks = Database.count(db=db, table=table, status="uncompleted")
            return render_template(
                "home.html",
                page="home",
                tasks=tasks,
                total=total_tasks,
                completed=completed_tasks,
                uncompleted=uncompleted_tasks,
                task_filter=task_filter,
            )

        @app.route("/add_task", methods=["POST"])
        def add_task():
            task = request.form["task"]
            date = request.form["date"]

            if task and date:
                Database.insert(
                    db=db,
                    table=table,
                    columns=columns,
                    values=[task, date, "uncompleted"],
                )

            return redirect(url_for("home"))

        @app.route("/complete_task/<int:task_id>", methods=["POST"])
        def complete_task(task_id):
            Database.update(
                db=db, table=table, columns=["status"], values=["completed"], id=task_id
            )
            return redirect(url_for("home"))

        @app.route("/delete_task/<int:task_id>", methods=["POST"])
        def delete_task(task_id):
            Database.delete(db=db, table=table, id=task_id)
            return redirect(url_for("home"))


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=8000)  # http://127.0.0.1:8000/
