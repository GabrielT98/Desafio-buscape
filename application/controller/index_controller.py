

from application import app
from flask import Flask, render_template, redirect,url_for
from application.model.dao.produto_dao import ProdutoDAO
from application.model.entily.produto import Produto

produtodao = ProdutoDAO()
produto_list =produtodao.listar_todos_produtos()
carrinho_list =produtodao.listar_todo_carrinho()


@app.route("/")
def index():
    return render_template("index.html",produto_list = produto_list,carrinho_list = carrinho_list)

@app.route("/adicionar/<int:id>")
def adicionar(id):

    for produto in produto_list:
        if produto.get_id() == int(id):#esse id vem como str e temos q transformar em int.
            carrinho_list.append(produto)

    return redirect(url_for('index'))
    

@app.route("/excluir/<id>")
def excluir(id):
    for produto in carrinho_list:
        if produto.get_id() == int(id):
            carrinho_list.remove(produto)
    return redirect(url_for('index'))
    
    