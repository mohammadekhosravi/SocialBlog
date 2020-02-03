from flask import Flask

app = Flask(__name__)

from blog.core.views import core
from blog.error_handler.handlers import errors

app.register_blueprint(core)
app.register_blueprint(errors)
