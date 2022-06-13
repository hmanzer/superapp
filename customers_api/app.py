from flask import Blueprint, Flask, jsonify
from flask_restx import Api
from db import db,DbConfig
from ma import ma
from resources.user import User, user_ns
from marshmallow import ValidationError

app = Flask(__name__)

bluePrint = Blueprint('api', __name__, url_prefix='/api')
api = Api(bluePrint, doc='/doc', title='customer api')

app.register_blueprint(bluePrint)
app.config["SQLALCHEMY_DATABASE_URI"] = DbConfig().getUri()
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

api.add_namespace(user_ns)


@app.before_first_request
def create_tables():
    db.create_all()

@api.errorhandler(ValidationError)
def handle_validation_error(error):
    return jsonify(error.messages), 400


user_ns.add_resource(User, '/<int:id>')
user_ns.add_resource(User, "")



if __name__ == "__main__":
    db.init_app(app)
    ma.init_app(app)
    app.run(debug=True, host="0.0.0.0")