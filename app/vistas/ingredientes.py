from flask import Blueprint, Response, request, render_template, redirect, url_for
from app.logica.ingredientesControlador import IngredienteControlador

controlador = IngredienteControlador()
ingredientes_bp = Blueprint("ingredientes", __name__, url_prefix="/ingredientes")


@ingredientes_bp.route('/')
def ingredientes_lista():
    lista_ingredientes = controlador.lista_ingredientes()
    return render_template('ingredientes_lista.html', ingredientes=lista_ingredientes)

@ingredientes_bp.route('/agregar')
def ingredientes_agregar():
    return render_template('ingredientes_agregar.html')