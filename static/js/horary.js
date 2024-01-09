window.onload = function() {
    const dateFlask = document.getElementById('dateFlask').textContent;
    console.log(dateFlask)
    const date = new Date(dateFlask);
    const dayIndex = date.getDay();

    const horarioTable = document.getElementById('horarioTable');
    const row = horarioTable.insertRow();

    const daysOfWeek = ['Lunes', 'Martes', 'Miércoles', 'Jueves', 'Viernes', 'Sábado', 'Domingo'];

    const cell = row.insertCell();
    cell.textContent = "Dia"

    daysOfWeek.forEach((day, index) => {
        const cell = row.insertCell();
        cell.textContent = day;

        if (index === dayIndex) {
            cell.classList.add('rojo');
        }
    });

    const horasDelDia = 24;
    for (let i = 0; i < horasDelDia; i++) {
        const row = horarioTable.insertRow();

        for (let j = 0; j <= daysOfWeek.length; j++) {
            const cell = row.insertCell();

            if (j === dayIndex + 1) {
                if (i >= 8 && i <= 12) {
                    cell.classList.add('rojo');
                }
            }
            
            if (j === 0) {
                cell.textContent = `${i}:00`;
            }
        }
    }
    
    const rutaActual = window.location.pathname; // Obtenemos la ruta actual

    const btnAnterior = document.querySelector('.btn-anterior');
    const btnSiguiente = document.querySelector('.btn-siguiente');

    // Lógica para el botón ANTERIOR
    btnAnterior.addEventListener('click', function(event) {
        event.preventDefault(); // Evitamos el comportamiento predeterminado del enlace
        const numeroActual = obtenerNumeroDeRuta(rutaActual);
        const rutaAnterior = `/horario/${numeroActual - 1}`;
        window.location.href = rutaAnterior; // Redirigimos al horario anterior
    });

    // Lógica para el botón SIGUIENTE
    btnSiguiente.addEventListener('click', function(event) {
        event.preventDefault(); // Evitamos el comportamiento predeterminado del enlace
        const numeroActual = obtenerNumeroDeRuta(rutaActual);
        const rutaSiguiente = `/horario/${numeroActual + 1}`;
        window.location.href = rutaSiguiente; // Redirigimos al horario siguiente
    });

    // Función para obtener el número de la ruta actual
    function obtenerNumeroDeRuta(ruta) {
        const partesRuta = ruta.split('/'); // Dividimos la ruta en partes
        return parseInt(partesRuta[partesRuta.length - 1]); // Obtenemos el último segmento de la ruta (el número)
    }
};
