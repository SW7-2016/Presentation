from __future__ import print_function
from flask import render_template, request, abort
from website import app, models, db
import sys

from .models import Cpu, Gpu, Review
cat_list = ["Cpu", "Gpu"]


@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html', cat_list=cat_list)


@app.route('/category/<category>')
def list_items(category):

    showing = request.args.get('show', 10)
    orderby = request.args.get('orderby', "superscore")
    order = request.args.get('order', "desc")
    order_direction = getattr(db, order)
    try:
        # Gets the class module depending on the category chosen.
        cat_que = getattr(sys.modules[__name__], category.title())
        products = db.session.query(cat_que).order_by(order_direction(orderby)).limit(showing).all()
        return render_template('list_products.html', products=products, category
                               =category, show=showing, orderby=orderby,
                               order=order)
    except Exception as e:
        print(str(e), file=sys.stderr)
        abort(404)


@app.route('/category/<category>/<pid>')
def show_product(category, pid):

    cat_que = getattr(sys.modules[__name__], category.title())
    single_product = db.session.query(cat_que).filter(cat_que.id == pid).first()
    return render_template('single_product.html', category=category.title(), product=single_product)


@app.errorhandler(404)
def page_not_found(e):
    return str(e)
