from flask import Blueprint, flash, request, render_template, redirect, url_for, session
from app.logica.RestauranteControlador import RestauranteControlador
from app.logica.MenuControlador import MenuControlador
from app.logica.ProductoControlador import ProductoControlador

pagina_bp = Blueprint("pagina", __name__, url_prefix="/")
restControlador = RestauranteControlador()
menuControlador = MenuControlador()
prodControlador = ProductoControlador()

@pagina_bp.route('/')
def pagina_inicio():
    lista_restaurantes = restControlador.lista()    
    return render_template('pagina_inicio.html', lista_restaurantes=lista_restaurantes)

@pagina_bp.route('/iniciar_sesion')
def iniciar_sesion():
    session['usuario'] = 'Bryant';
    return redirect(url_for("pagina.pagina_inicio"))


@pagina_bp.route('/cerrar_sesion')
def cerrar_sesion():
    session['usuario'] = None;
    flash('Ha cerrado sesion correctamente', 'success')
    return redirect(url_for("pagina.pagina_inicio"))


@pagina_bp.route('/restaurante/menu/<id>')
def pagina_menu_restaurante(id):
    lista_menus = menuControlador.lista_por_restaurante(id)
    restaurante = restControlador.obtener_x_id(id)[0]
    return render_template('pagina_menu_restaurante.html', lista_menus=lista_menus, restaurante=restaurante)

@pagina_bp.route('/restaurante/producto/<id>')
def pagina_producto_restaurante(id):
    lista_productos = prodControlador.lista_por_restaurante(id)
    restaurante = restControlador.obtener_x_id(id)[0]
    return render_template('pagina_producto_restaurante.html', lista_productos=lista_productos, restaurante=restaurante)

@pagina_bp.route('/restaurante/producto/<id>/<id_p>')
def pagina_producto(id, id_p):
    producto = prodControlador.obtener_x_id(id_p)
    restaurante = restControlador.obtener_x_id(id)[0]
    return render_template('pagina_producto.html', 
            producto=producto,
            restaurante=restaurante)


@pagina_bp.route('/restaurante/menu/<id>/<id_m>')
def pagina_menu(id, id_m):
    menu = menuControlador.obtener_x_id(id_m)
    total = 0
    for prod in menu["productos"]:
        if prod["tipo"] == 0:
            menu['entrada'] = prodControlador.obtener_x_id(prod['fk_producto'])
            total += menu['entrada']["producto"]["precio"]
        elif prod["tipo"] == 1:
            menu['platoFuerte'] = prodControlador.obtener_x_id(prod['fk_producto'])
            total += menu['platoFuerte']["producto"]["precio"]
        elif prod["tipo"] == 2:
            menu['postre'] = prodControlador.obtener_x_id(prod['fk_producto'])
            total += menu['postre']["producto"]["precio"]
        elif prod["tipo"] == 3:
            menu['bebida'] = prodControlador.obtener_x_id(prod['fk_producto'])
            total += menu['bebida']["producto"]["precio"]
        elif prod == 4:
            menu['acompanamiento'] = prodControlador.obtener_x_id(prod['fk_producto'])
            total += menu['acompanamiento']["producto"]["precio"]
    
    menu['total'] = total
    menu['tipo'] = 1
    
    restaurante = restControlador.obtener_x_id(id)[0]
    return render_template('pagina_menu.html', 
            menu=menu,
            restaurante=restaurante)