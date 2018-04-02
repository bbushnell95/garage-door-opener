from flask import Flask
from flask_restful import Api
from flask_sqlalchemy import SQLAlchemy
from .models import DoorState
from .api.Status import Status
from .api.Home import Home

if __name__ == '__main__':
    db_url = 'mysql+pymysql://root:password@0.0.0.0:3306/Garage'
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = db_url
    DoorState.db.init_app(app)
    api = Api(app)
    api.add_resource(Status, '/status')
    api.add_resource(Home, '/')
    engine = DoorState.db.get_engine(app=app)
    DoorState.db.create_all(app=app)
    app.run(host='192.168.0.10', port=5000)
