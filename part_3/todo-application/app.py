import os
from flask import Flask, render_template, request, redirect, url_for
#from flask_healthz import healthz, HealthError
import utils
import requests
import json

def create_app(test_config=None):
    app = Flask(__name__)
    #app.register_blueprint(healthz, url_prefix="/healthz")

    env_config = os.getenv("APP_SETTINGS", "config.DevelopmentConfig")
    app.config.from_object(env_config)
    TODO_BACKEND_URL = app.config['TODO_BACKEND_URL']

    @app.route("/todolist")
    def home():
        
        todo_list = requests.get(f'{TODO_BACKEND_URL}/todos').read()
        json.loads(todo_list.decode("utf-8"))
        image = utils.get_random_image()
        return render_template("base.html", todo_list=todo_list, image=image)
    
    @app.route("/health")
    @app.route("/")
    def health():
        try:
            requests.get(f'{TODO_BACKEND_URL}/todos')
            return "OK", 200
        except Exception as e:
            print(e)
            return "Todo Backend Not Available", 500

        
        
    print(f"Server running on port {app.config['FLASK_RUN_PORT']}")

    return app
    
    