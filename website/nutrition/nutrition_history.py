from flask import Blueprint, jsonify
from flask_login import login_required, current_user
from ..models import UserMeal
from .. import db
import datetime

nutrition_get_history = Blueprint('nutrition_views', __name__)


@nutrition_get_history.route('/nutrition-history')
@login_required
def get_nutrition_data():
    today = datetime.date.today()
    dates = [(today - datetime.timedelta(days=i)).isoformat() for i in range(7)]
    carbs = [50, 60, 55, 30, 75, 70, 65]
    proteins = [25, 30, 28, 15, 35, 32, 34]
    fats = [20, 22, 18, 12, 28, 26, 24]

    return jsonify({
        'dates': dates,
        'carbs': carbs,
        'proteins': proteins,
        'fats': fats
    })
