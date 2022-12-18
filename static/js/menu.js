document.querySelectorAll(".mas_adicion").forEach(element => {
    element.addEventListener("click", (e) => {
        let id = e.target.dataset.id;
        if(typeof(id) == "undefined"){
            id = e.target.parentElement.dataset.id;
        }
        const elmento_grafico = document.querySelector(`#adicion${id}`);
        const elmento_hidden = document.querySelector(`#valAdicion${id}`);
        const maximo = document.querySelector(`#maxAdicion${id}`);
        
        
        if(parseInt(elmento_hidden.value) < parseInt(maximo.value)){
            elmento_hidden.value = parseInt(elmento_hidden.value) + 1;
            elmento_grafico.innerHTML = elmento_hidden.value;
        }
        if(parseInt(elmento_hidden.value) >= 1){
            document.querySelector(`#menos_adicion${id}`).classList.remove("disabled");
        }
        const precioAd = document.querySelector(`#precioAdicion${id}`);



        let total = 0;
        if(document.querySelector("#tipoMenu").value == 1){
            total += parseInt(document.querySelector("#precioMenu").value);
        }
        else{
            document.querySelectorAll(".precioProducto").forEach(element => {
                total += parseInt(element.value);
            });
        }
        
        total += (parseInt(precioAd.value) * parseInt(elmento_hidden.value)); 
        document.querySelector(".total").innerHTML = "$ " + total.toLocaleString('es-CO');
        

    });
});


document.querySelectorAll(".menos_adicion").forEach(element => {
    element.addEventListener("click", (e) => {
        let id = e.target.dataset.id;
        if(typeof(id) == "undefined"){
            id = e.target.parentElement.dataset.id;
        }
        const elmento_grafico = document.querySelector(`#adicion${id}`);
        const elmento_hidden = document.querySelector(`#valAdicion${id}`);

        console.log(elmento_hidden, `#valAdicion${id}`)
        if(parseInt(elmento_hidden.value) > 0){
            elmento_hidden.value = parseInt(elmento_hidden.value) - 1;
            elmento_grafico.innerHTML = elmento_hidden.value;
        }
        if(parseInt(elmento_hidden.value) == 0){
            document.querySelector(`#menos_adicion${id}`).classList.add("disabled");
        }
        const precioAd = document.querySelector(`#precioAdicion${id}`);
        let total = 0;
        if(document.querySelector("#tipoMenu").value == 1){
            total += parseInt(document.querySelector("#precioMenu").value);
        }
        else{
            document.querySelectorAll(".precioProducto").forEach(element => {
                total += parseInt(element.value);
            });
        }
        
        total += (parseInt(precioAd.value) * parseInt(elmento_hidden.value)); 

        document.querySelector(".total").innerHTML = "$ " + total.toLocaleString('es-CO');
    });
});
