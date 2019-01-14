# blueprint 정의
from flask import Blueprint

# ~/users/
bp_users = Blueprint(
    'users_bp',
    __name__,
    template_folder='../templates',
    static_folder='../static'
)

# ~/analysis/
bp_analysis = Blueprint(
    'analysis_bp',
    __name__,
    template_folder='../templates',
    static_folder='../static'
)