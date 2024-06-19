// Variables para manejar el tiempo y el estado del cronómetro
let startTime
let updatedTime
let difference
let tInterval
let savedTime;
let running = false;

// Elementos del DOM
const timeDisplay = document.getElementById('time-display');
const startBtn = document.getElementById('start-btn');
const pauseBtn = document.getElementById('pause-btn');
const resetBtn = document.getElementById('reset-btn');

// Cargar el tiempo guardado desde localStorage al iniciar la página
if (localStorage.getItem('savedTime')) {
    savedTime = parseInt(localStorage.getItem('savedTime'));
    updateTimeDisplay(savedTime);
} else {
    savedTime = 0;
}

// Añadir eventos a los botones
startBtn.addEventListener('click', startTimer);
pauseBtn.addEventListener('click', pauseTimer);
resetBtn.addEventListener('click', resetTimer);

// Función para iniciar el cronómetro
function startTimer() {
    if (!running) {
        // Registrar el tiempo actual menos el tiempo guardado para continuar desde donde se pausó
        startTime = new Date().getTime() - savedTime;
        // Configurar el intervalo para actualizar el cronómetro cada milisegundo
        tInterval = setInterval(getShowTime, 1);
        running = true;
    }
}

// Función para pausar el cronómetro
function pauseTimer() {
    if (running) {
        clearInterval(tInterval); // Detener el intervalo
        savedTime = difference; // Guardar el tiempo actual en savedTime
        localStorage.setItem('savedTime', savedTime); // Guardar el tiempo en localStorage
        running = false;
    }
}

// Función para reiniciar el cronómetro
function resetTimer() {
    clearInterval(tInterval); // Detener el intervalo
    running = false;
    savedTime = 0; // Reiniciar el tiempo guardado
    localStorage.setItem('savedTime', savedTime); // Actualizar localStorage
    updateTimeDisplay(0); // Actualizar la pantalla del cronómetro
}

// Función que se llama cada milisegundo para actualizar el cronómetro
function getShowTime() {
    updatedTime = new Date().getTime(); // Obtener el tiempo actual
    difference = updatedTime - startTime; // Calcular la diferencia con el tiempo de inicio
    updateTimeDisplay(difference); // Actualizar la pantalla del cronómetro
}

// Función para actualizar la pantalla del cronómetro
function updateTimeDisplay(time) {
    // Calcular horas, minutos y segundos a partir del tiempo en milisegundos
    const hours = Math.floor((time % (1000 * 60 * 60 * 24)) / (1000 * 60 * 60));
    const minutes = Math.floor((time % (1000 * 60 * 60)) / (1000 * 60));
    const seconds = Math.floor((time % (1000 * 60)) / 1000);

    // Formatear los valores para que siempre tengan dos dígitos
    const displayHours = hours.toString().padStart(2, '0');
    const displayMinutes = minutes.toString().padStart(2, '0');
    const displaySeconds = seconds.toString().padStart(2, '0');

    // Actualizar el contenido del elemento del DOM con el tiempo formateado
    timeDisplay.innerHTML = `${displayHours}:${displayMinutes}:${displaySeconds}`;
}
