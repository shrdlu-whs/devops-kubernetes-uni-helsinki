import random
import string
from flask import Flask, jsonify
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.sql import text
from database import db
from models import PingpongCounter
from json_encoder import AlchemyEncoder
import os

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

    @app.route('/pingpong', methods=['GET'])
    def pingpong():
        counter = PingpongCounter.query.first()
        counter.count += 1
        db.session.commit()

        return "Pong " + str(counter.count)

    @app.route('/counter', methods=['GET'])
    def status():
        counter = PingpongCounter.query.first()
        return  str(counter.count)
    
    # Health check
    @app.route("/health")
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
        
        
            # Create a new counter if it doesn't exist
            counter = PingpongCounter.query.first()
            if counter is None:
                counter = PingpongCounter()
                db.session.add(counter)
                db.session.commit()
        except Exception as e:
            print(e)
            print(app.config['SQLALCHEMY_DATABASE_URI'])

    return app
