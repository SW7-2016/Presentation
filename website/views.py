from flask import render_template, request
from website import app, models, db
from flask_sqlalchemy import SQLAlchemy
import sys


from .models import Con, Pro, Product, Cpu, ProductRetailer, Retailer, Review, Reviewcomment
clist = ["Cpu"]

@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html', clist=clist)

@app.route('/category/<cname>')
def list_items(cname):

    # Needs a try around it, so that it returns an error/404 if the cname does
    # not match a model/class
    # Gets the class module depending on the category chosen.
    cque = getattr(sys.modules[__name__], cname)
    # Queries the given category for products
    # products = db.session.query(t_cpu).all()
    products = db.session.query(Product).join(cque)
    # cname = "cpu"

    return render_template('list_products.html', products = products, category
                        = cname.title())

@app.route('/category/<cname>/<pid>')
def show_product( cname, pid ):

    return "Hello " + cname + "    id: " + pid


