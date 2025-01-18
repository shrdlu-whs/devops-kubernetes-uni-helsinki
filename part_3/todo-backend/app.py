import os
from flask import Flask, request, redirect
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.sql import text
from database import db
from models import Todo
from json_encoder import AlchemyEncoder
import json

def create_app(test_config=None):
    app = Flask(__name__)
    app.json_encoder = AlchemyEncoder
    env_config = os.getenv("APP_SETTINGS", "config.DevelopmentConfig")
    app.config.from_object(env_config)
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    db.app = app
    try:
        db.init_app(app)
    except Exception as e:
        print(e)
        print(app.config['SQLALCHEMY_DATABASE_URI'])

    @app.route("/todos")
    def home():
        todo_list = Todo.query.order_by(Todo.id).all()
        todo_list = json.dumps(todo_list, cls=AlchemyEncoder)
        return todo_list

    @app.post("/todos/add")
    def add():
        title = request.form.get("title", type=str)
        print(f'Adding todo with title: {title}')
        if(len(title) <= 140):
            new_todo = Todo(title=title, done=False)
            db.session.add(new_todo)
            db.session.commit()
        else:
            app.logger.error(f'Error: Todo title is too long.')
        return redirect('/todolist')

    @app.post("/todos/<int:todo_id>")
    def update(todo_id):
        todo = Todo.query.filter_by(id=todo_id).first()
        todo.done = not todo.done
        db.session.commit()
        return redirect("/todolist")

    @app.post("/todos/delete/<int:todo_id>")
    def delete(todo_id):
        todo = Todo.query.filter_by(id=todo_id).first()
        db.session.delete(todo)
        db.session.commit()
        return redirect("/todolist")
    
    # Health check on routes /health and /
    @app.route("/health")
    @app.route("/")
    def health():
        try:
            db.session.execute(text('SELECT 1'))
            return "OK", 200
        except Exception as e:
            print(e)
            return "Database not ready", 500

    with app.app_context():
        try:
            db.create_all()
        except Exception as e:
            print(e)
            print(app.config['SQLALCHEMY_DATABASE_URI'])
        
    print(f"Server running on port {app.config['FLASK_RUN_PORT']}")

    return app
    
    