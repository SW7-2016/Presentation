from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
import website.config

app = Flask(__name__,
           instance_relative_config=True,
           template_folder='templates')
db = SQLAlchemy(app)

app.config.from_object(config.DevelopmentConfig)
from website import views, models
