

def test_carrito_calcular_valor(carritos):
    carrito = carritos["carrito1"]
    assert carrito.calcularValor() == 122100