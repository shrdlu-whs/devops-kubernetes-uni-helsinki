import os
from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from flask_healthz import healthz, HealthError
from database import db
from models import Todo

def create_app(test_config=None):
    app = Flask(__name__)
    app.register_blueprint(healthz, url_prefix="/healthz")

    env_config = os.getenv("APP_SETTINGS", "config.DevelopmentConfig")
    app.config.from_object(env_config)
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    db.app = app
    db.init_app(app)

    



    @app.route("/")
    def home():
        todo_list = Todo.query.order_by(Todo.id).all()
        return render_template("base.html", todo_list=todo_list)


    @app.route("/todos/add", methods=["POST"])
    def add():
        title = request.form.get("title")
        new_todo = Todo(title=title, done=False)
        db.session.add(new_todo)
        db.session.commit()
        return redirect(url_for("home"))

    @app.route("/todos/update/<int:todo_id>")
    def update(todo_id):
        todo = Todo.query.filter_by(id=todo_id).first()
        todo.done = not todo.done
        db.session.commit()
        return redirect(url_for("home"))

    @app.route("/todos/delete/<int:todo_id>")
    def delete(todo_id):
        todo = Todo.query.filter_by(id=todo_id).first()
        db.session.delete(todo)
        db.session.commit()
        return redirect(url_for("home"))
    
    # Health check
    def liveness():
        pass

    def readiness():
        try:
            db.session.execute('SELECT 1')
        except Exception:
            raise HealthError("Can't connect to the database")

#if __name__ == "__main__":
    with app.app_context():
        db.create_all()
        
    print(f"Server running on port {app.config['FLASK_RUN_PORT']}")

    return app
    
    