function IrACrear(){
    var b = document.getElementById("InterfazBusqueda");
    var f = document.getElementById("FormularioBusqueda");
    var c = document.getElementById("InterfazCrear");
    b.style.display = "none";
    f.style.display = "none";
    c.style.display = "grid";
}
function IrABuscar(){
    var b = document.getElementById("InterfazBusqueda");
    var f = document.getElementById("FormularioBusqueda");
    var c = document.getElementById("InterfazCrear");
    b.style.display = "grid";
    f.style.display = "grid";
    c.style.display = "none";
}