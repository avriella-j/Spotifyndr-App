from flask import Blueprint, render_template
from flask_login import login_required

fyp_bp = Blueprint('fyp', __name__)


@fyp_bp.route('/')
@login_required
def fyp():
    """For You Page."""
    return render_template('fyp.html')
