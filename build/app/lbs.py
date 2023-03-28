#!/usr/bin/python3

from common.base import Base, engine
from common.configs import SECRET_KEY

from flask import Flask
Base.metadata.create_all(engine)

def create_app():
    app = Flask(__name__)
    app.secret_key = SECRET_KEY

    from blueprints.main import main
    app.register_blueprint(main)

    from blueprints.user import user_blueprint
    app.register_blueprint(user_blueprint)

    from blueprints.librarian_bp import librarian_blueprint
    app.register_blueprint(librarian_blueprint)

    from blueprints.issued_blueprint import issued_blueprint
    app.register_blueprint(issued_blueprint)

    return app

if __name__ == "__main__":
    app = create_app()
    app.run(host='0.0.0.0', port='5000', debug=True)
