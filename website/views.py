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
    # Try to request the information, make a query and render the template
    # If anything fails it will show a 404-page
    try:
        # Requests the ordering values, or defaults them to the second value
        showing = request.args.get('show', 10)
        orderby = request.args.get('orderby', "superscore")
        order = request.args.get('order', "desc")
        order_direction = getattr(db, order)

        # Gets the class module depending on the category chosen.
        cat_que = getattr(sys.modules[__name__], category.title())
        # Query the products that needs to be shown based on ordering values
        products = db.session.query(cat_que).order_by(order_direction(orderby)).limit(showing).all()
        # Return the rendered template with the information queried
        return render_template('list_products.html', cat_list=cat_list,  products=products, category
                               =category, show=showing, orderby=orderby,
                               order=order)
    # Exception handling if anything above fails
    except Exception as e:
        # DEBUGGING: Prints the exception to the commandline
        print(str(e), file=sys.stderr)
        # Redirects/abort to decorator 404
        abort(404)


@app.route('/category/<category>/<pid>')
def show_product(category, pid):
    # Try to request the information, make a query and render the template
    # If anything fails it will show a 404-page
    try:
        # Gets the class module depending on the category chosen.
        cat_que = getattr(sys.modules[__name__], category.title())
        # Query the selected product from the table/list
        single_product = db.session.query(cat_que).filter(cat_que.id == pid).first()
        # Return the rendered template with the information queried
        return render_template('single_product.html', cat_list=cat_list, category=category.title(), product=single_product)
    # Exception handling if anything above fails
    except Exception as e:
        # DEBUGGING: Prints the exception to the commandline
        print(str(e), file=sys.stderr)
        # Redirects/abort to decorator 404
        abort(404)


# 404-page - generates a white page with the 404 error message
@app.errorhandler(404)
def page_not_found(e):
    return str(e)
