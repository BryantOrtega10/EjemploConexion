function addIngreBase() {
    var contenedor = document.getElementById("ingredientesContainer")
    var contador = contenedor.childElementCount
    contenedor.innerHTML += ` 
                            <div class="row">
                                <div class="col">
                                    <div class="form-floating mb-3">
                                      <input type="hidden" name="ingresBase[]">  
                                      <input type="number" class="form-control"  name="id_ingrediente_base${contador}" id="id_ingrediente_base${contador}" placeholder="123">
                                      <label for="id_ingrediente_base${contador}">Id</label>
                                    </div>
                                </div>
                                <div class="col">
                                    <div class="form-check">  
                                        <input class="form-check-input" type="checkbox" value="1" name="auto_select${contador}" id="auto_select${contador}">
                                        <label class="form-check-label" for="auto_select${contador}">¿Es primordial?</label>
                                    </div>
                                </div>
                            </div>
                          `
}

function addAdicion() {
    var contenedor = document.getElementById("adicionesContainer")
    var contador = contenedor.childElementCount
    contenedor.innerHTML += ` 
                            <div class="row">
                                <div class="col">
                                    <div class="form-floating mb-3">
                                      <input type="hidden" name="adiciones[]">
                                      <input type="number" class="form-control" name="id_adicion${contador}"  id="id_adicion${contador}" placeholder="123">
                                      <label for="id_adicion${contador}">Id</label>
                                    </div>
                                </div>
                                <div class="col">
                                    <div class="form-floating mb-3">
                                        <input type="number" class="form-control" name="precio${contador}" id="precio${contador}" placeholder="123">
                                        <label for="precio${contador}">Precio</label>
                                    </div>
                                </div>
                            </div>
                          `
}

