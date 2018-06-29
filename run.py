# =============================================================================
# This will run the up on the server to which we deployed
# =============================================================================
from app import app
from db import db

db.init_app(app)

@app.before_first_request
def create_tables():
    db.create_all()