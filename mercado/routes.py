
from flask import render_template
from mercado.model import Item
from mercado import app
from mercado import routes

@app.route('/')
def page_home():
    return render_template('home.html')

@app.route('/produtos')
def page_produtos():
    itens = Item.query.all()
    return render_template('produtos.html', itens=itens)

