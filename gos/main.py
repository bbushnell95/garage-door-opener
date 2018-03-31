from flask import Flask
from flask_restful import Api
from .models import DoorState
from .api.Status import Status

if __name__ == '__main__':
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:password@localhost:3306/Garage'
    DoorState.db.init_app(app)
    api = Api(app)
    api.add_resource(Status, '/status')
    app.run(host='0.0.0.0', port=5000)
