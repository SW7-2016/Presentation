from flask import render_template, request, abort
from website import app, models, db
from flask_sqlalchemy import SQLAlchemy
import sys


from .models import Product, cpu, gpu
cat_list = ["cpu", "gpu"]


@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html', cat_list=cat_list)


@app.route('/category/<category>')
def list_items(category):

    no_to_show = request.args.get('show', 10, type=int)
    # Needs a try around it, so that it returns an error/404 if the cname does
    # not match a model/class
    # Gets the class module depending on the category chosen.
    try:
        cat_que = getattr(sys.modules[__name__], category)
        products = db.session.query(Product).join(cat_que).limit(no_to_show).all()
        return render_template('list_products.html', products=products, category
                               =category.title())
    except Exception as e:
        abort(404)


@app.route('/category/<category>/<pid>')
def show_product(category, pid):
    # return "Hello " + category + "    id: " + pid
    # return render_template('single_product.html', category=category, pid=pid, product=product)

    cat_que = getattr(sys.modules[__name__], category)
    single_product = db.session.query(Product).join(cat_que).filter(Product.ProductID == pid, cpu.c.ProductID == pid).all()
    return render_template('single_product.html', category=category.lower(), product=single_product[0])


@app.errorhandler(404)
def page_not_found(e):
    return str(e)
