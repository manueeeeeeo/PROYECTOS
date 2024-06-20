const canvas = document.getElementById('drawingCanvas');
const ctx = canvas.getContext('2d');
const colorPicker = document.getElementById('colorPicker');
const lineWidth = document.getElementById('lineWidth');
const clearBtn = document.getElementById('clearBtn');
const saveBtn = document.getElementById('saveBtn');

// Ajustar el tamaño del canvas al tamaño de la ventana
canvas.width = window.innerWidth;
canvas.height = window.innerHeight - 80; // Dejar espacio para la barra de herramientas

// Variables para controlar el dibujo
let drawing = false;
let currentX = 0;
let currentY = 0;

// Funciones para manejar el dibujo
const startDrawing = (e) => {
    drawing = true;
    [currentX, currentY] = [e.offsetX, e.offsetY];
};

const draw = (e) => {
    if (!drawing) return;

    ctx.strokeStyle = colorPicker.value;
    ctx.lineWidth = lineWidth.value;
    ctx.lineCap = 'round';

    ctx.beginPath();
    ctx.moveTo(currentX, currentY);
    ctx.lineTo(e.offsetX, e.offsetY);
    ctx.stroke();

    [currentX, currentY] = [e.offsetX, e.offsetY];
};

const stopDrawing = () => {
    drawing = false;
    ctx.beginPath();
};

// Event listeners para el dibujo
canvas.addEventListener('mousedown', startDrawing);
canvas.addEventListener('mousemove', draw);
canvas.addEventListener('mouseup', stopDrawing);
canvas.addEventListener('mouseout', stopDrawing);

// Función para borrar el dibujo
const clearCanvas = () => {
    ctx.clearRect(0, 0, canvas.width, canvas.height);
};

// Función para guardar el dibujo como una imagen
const saveCanvas = () => {
    const link = document.createElement('a');
    link.download = 'drawing.png';
    link.href = canvas.toDataURL();
    link.click();
};

// Event listeners para los botones de la barra de herramientas
clearBtn.addEventListener('click', clearCanvas);
saveBtn.addEventListener('click', saveCanvas);

// Event listeners para dispositivos táctiles
canvas.addEventListener('touchstart', (e) => {
    const touch = e.touches[0];
    const mouseEvent = new MouseEvent('mousedown', {
        clientX: touch.clientX,
        clientY: touch.clientY
    });
    canvas.dispatchEvent(mouseEvent);
});

canvas.addEventListener('touchmove', (e) => {
    const touch = e.touches[0];
    const mouseEvent = new MouseEvent('mousemove', {
        clientX: touch.clientX,
        clientY: touch.clientY
    });
    canvas.dispatchEvent(mouseEvent);
});

canvas.addEventListener('touchend', () => {
    const mouseEvent = new MouseEvent('mouseup', {});
    canvas.dispatchEvent(mouseEvent);
});
