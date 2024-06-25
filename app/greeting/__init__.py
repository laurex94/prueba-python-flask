from flask import Blueprint

bp = Blueprint('saludos', __name__)

from app.greeting import routes
