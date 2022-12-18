from flask import Blueprint, flash, request, render_template, redirect, url_for

from app.logica.ProductoControlador import ProductoControlador

producto_controlador = ProductoControlador()
productos_bp = Blueprint("productos", __name__, url_prefix="/productos")


@productos_bp.route('/agregar', methods=['GET', 'POST'])
def agregar():
    if request.method == 'GET':
        return render_template('producto_agregar.html')
    else:
        res = producto_controlador.agregar(request)
        error = None
        if res['success']:
            flash('Producto registrado exitosamente')
        else:
            error = res['error']
        return render_template('producto_agregar.html', error=error)

