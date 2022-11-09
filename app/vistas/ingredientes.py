from flask import Blueprint, flash, request, render_template, redirect, url_for
from app.logica.IngredienteControlador import IngredienteControlador

controlador = IngredienteControlador()
ingredientes_bp = Blueprint("ingredientes", __name__, url_prefix="/ingredientes")


@ingredientes_bp.route('/')
def ingredientes_lista():
    lista_ingredientes = controlador.lista()
    
    return render_template('ingredientes_lista.html', ingredientes=lista_ingredientes)

@ingredientes_bp.route('/agregar')
def ingredientes_agregar():
    return render_template('ingredientes_agregar.html')


@ingredientes_bp.route('/agregar', methods=['POST'])
def agregar():    
    resp = controlador.agregar(request)
    if resp["success"]:
        flash('Ingrediente creado correctamente', 'success')
        return redirect(url_for('ingredientes.ingredientes_lista'))
    else:
        flash(resp["error"], 'danger')
        return redirect(url_for('ingredientes.ingredientes_agregar'))


@ingredientes_bp.route('/modificar/<int:id>')
def ingredientes_modificar(id):
    resp = controlador.obtener_x_id(id)
    if len(resp) > 0:
        return render_template('ingredientes_modificar.html', ingrediente=resp[0])
    else:
        flash("No se encontró un ingrediente con ese id", 'danger')
        return redirect(url_for('ingredientes.ingredientes_lista'))


@ingredientes_bp.route('/modificar/<int:id>', methods=['POST'])
def modificar(id):
    resp = controlador.modificar(id,request)
    if resp["success"]:
        flash('Ingrediente modificado correctamente', 'success')
        return redirect(url_for('ingredientes.ingredientes_lista'))
    else:
        flash(resp["error"], 'danger')
        return redirect(url_for('ingredientes.ingredientes_modificar',id=id))


@ingredientes_bp.route('/eliminar/<int:id>')
def ingredientes_eliminar(id):
    resp = controlador.obtener_x_id(id)
    if len(resp) > 0:
        return render_template('ingredientes_eliminar.html', ingrediente=resp[0])
    else:
        flash("No se encontró un ingrediente con ese id", 'danger')
        return redirect(url_for('ingredientes.ingredientes_lista'))


@ingredientes_bp.route('/eliminar/<int:id>', methods=['POST'])
def eliminar(id):
    resp = controlador.eliminar(id)
    if resp["success"]:
        flash('Ingrediente eliminado correctamente', 'success')
        return redirect(url_for('ingredientes.ingredientes_lista'))
    else:
        flash(resp["error"], 'danger')
        return redirect(url_for('ingredientes.ingredientes_eliminar',id=id))