#!/usr/bin/python3
""" API module """


from flask import Flask
from yourapplication.app_views import app_views
from models import storage
from api.v1.views import app_views


app = Flask(__name__)
app.register_blueprint(app_views)


@app_views.errorhandler(404)
def page_not_found(e):
    return '{\n"error": "Not found"\n}'


@app.teardown_appcontext
def teardown(exc):
    """Remove the current session."""
    storagee.close()


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, threaded=True)
