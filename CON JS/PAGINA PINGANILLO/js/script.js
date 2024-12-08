// Asegurarse de que el contenido se muestra después de la carga
document.addEventListener("DOMContentLoaded", () => {
    const loader = document.getElementById('loader');
    const mainContent = document.getElementById('main-content');

    // Simular un tiempo de carga
    setTimeout(() => {
        // Ocultar el loader
        loader.style.display = 'none';
        // Mostrar el contenido principal
        mainContent.classList.remove('hidden');
    }, 2000); // Tiempo en milisegundos (2 segundos)
});
