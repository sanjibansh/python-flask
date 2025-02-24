# from flask import Flask, request
# from route import route


# app = Flask(__name__)


# if __name__ == "__main__":
#     app.run(debug = True)




# from flask import Flask
# from route import api_routes  # Corrected import

# app = Flask(__name__)
# app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://user:password@host/dbname'
# app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# app.register_blueprint(api_routes)  # Registering Blueprint

# if __name__ == "__main__":
#     app.run(debug=True)


from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from extension import db


def create_app():
    app = Flask(__name__)

    # Database Configuration
    app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///database.db"  # Update with PostgreSQL if needed
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    db.init_app(app)  # Bind db to app

    with app.app_context():
        from models import Leave  # Import models after app is created
        db.drop_all() 
        db.create_all()  # Auto-create tables

    from route import api_routes  # Import routes after db initialization
    app.register_blueprint(api_routes)  # Register blueprint
    print(app.url_map)  # Debugging route map

    return app

if __name__ == "__main__":
    app = create_app()
    app.run(debug=True)
