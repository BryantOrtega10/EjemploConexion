from flask import Blueprint, Response, request, render_template, redirect, url_for

ingredientes_bp = Blueprint("ingredientes", __name__, url_prefix="/ingredientes")


@ingredientes_bp.route('/')
def ingredientes_lista():
    return render_template('ingredientes_lista.html')