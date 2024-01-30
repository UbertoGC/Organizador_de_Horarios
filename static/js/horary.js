const voids = document.querySelectorAll(".td_void");
const fulls = document.querySelectorAll(".td_full");
const modal1 = document.getElementById('modal1')
const closemodal1 = document.getElementById('btn-modal1')
const id_horary = document.getElementById('infopage').getAttribute('data_id')
closemodal1.addEventListener('click', (e)=>{
    modal1.classList.remove('modal--show')
});
voids.forEach(el => el.addEventListener('click', event => {
    let first_date = document.getElementById('start_date')
    let first_time = document.getElementById('start_time')
    let day = el.getAttribute("day")
    let hour = parseInt(el.getAttribute("hour"))
    let minute = parseInt(el.getAttribute("minute"))
    first_date.value = day
    let new_hour = hour.toString()
    if(hour<10){
        new_hour = '0' + new_hour
    }
    let new_minute = minute.toString()
    if(minute<10){
        new_minute = '0' + new_minute
    }
    let new_time = new_hour + ':' + new_minute
    first_time.value = new_time
    console.log(new_time)
}));
fulls.forEach(el => el.addEventListener('click', event => {
    let id_hour = el.getAttribute('id_hour')
    let titulo = el.getAttribute('tittle')
    let start_date = el.getAttribute('start_date')
    let final_date = el.getAttribute('final_date')
    let description = el.getAttribute('description')
    document.getElementById('Titulo').innerHTML = titulo
    document.getElementById('Descripcion').innerHTML = description
    document.getElementById('FechaInicial').innerHTML = 'FECHA Y HORA DE INICIO: ' + start_date
    document.getElementById('FechaFinal').innerHTML = 'FECHA Y HORA DE FINALIZACIÓN: ' + final_date
    document.getElementById('BotonEliminarHora').setAttribute('href','/horario/'+id_horary+'/'+id_hour+'/eliminar')
    modal1.classList.add('modal--show')
}));