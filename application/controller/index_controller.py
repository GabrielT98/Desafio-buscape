
from application import app
from flask import Flask, render_template, request
from application.model.dao.produto_dao import ProdutoDAO
from application.model.entily.produto import Produto

@app.route("/")
def index():
    produto_list =ProdutoDAO().listar_todos_produtos()
    return render_template("index.html",produto_list = produto_list)