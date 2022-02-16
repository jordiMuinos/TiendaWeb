window.onload=function(){


    function cargarDatos(){
        ajax=new XMLHttpRequest();
        ajax.onreadystatechange=()=>{
            if(ajax.readyState==4){
                if(ajax.status==200){
                    productos=JSON.parse(ajax.responseText)
                    mostrarProductos(productos)
                }
            }else{
                console.log(ajax.readyState)
            }
            
        }
        ajax.open('GET','http://localhost:8080/getproducts',true);
        ajax.send(null);
    }
    
    function mostrarProductos(productos){
        let contenido=""
        for (let i = 0; i < productos.length; i++){
            contenido += `<div class="producto">
            <img src="static/img/${productos[i].img}" alt="">
            <div class= "tituloProducto"><h4>${productos[i].nombre}</h4>
            <p>${productos[i.descripcion]}</p></div>
            <div><label>Precio:</label><span>${productos[i].precio}</span><label>Cantidad:</label><span>${productos[i].cantidad}</span>
            <div><img src="static/img/borrar.jpg" id="Borrar${productos[i].id}"class="btnBorrar"</div></div>`

        }
        document.getElementById("listaProductos").innerHTML = contenido
        asociarEventos();
            
    }
    setTimeout(cargarDatos,3000);

    function asociarEventos(){
        let papeleras = document.getElementsByClassName("btnBorrar")
        for (let i = 0; i < papeleras.lengt; i++) {
            const papelera = papeleras[i];
            papelera.onclick=(evt)=>{
                let idProducto=evt.currentTarget.id.substring(11);
                ajax = new XMLHttpRequest();
                ajax.onreadystatechange=()=>{
                    if(ajax.readyState==4){
                        if(ajax.status==200){
                            productos=JSON.parse(ajax.responseText)
                            mostrarProductos(productos)
                        }
                    if(ajax.status==500){
                        alert("Error del servidor")
                    }
                    }
                }
            let url = `http://localhost:8080/eliminarproducto?idproducto=${idProducto}`
            ajax.open('GET',url,true);
            ajax.send(null);
        }
       
   }
}

}