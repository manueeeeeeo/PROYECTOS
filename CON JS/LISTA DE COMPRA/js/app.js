// ****** Selección de elementos **********

// Seleccionamos el formulario con la clase .grocery-form
const formElement = document.querySelector(".grocery-form");
// Seleccionamos el elemento de alerta con la clase .alert
const alertElement = document.querySelector(".alert");
// Seleccionamos el campo de entrada de texto por su ID grocery
const groceryInput = document.getElementById("grocery");
// Seleccionamos el botón de enviar con la clase .submit-btn
const submitButton = document.querySelector(".submit-btn");
// Seleccionamos el contenedor de la lista de compras con la clase .grocery-container
const containerElement = document.querySelector(".grocery-container");
// Seleccionamos la lista de compras con la clase .grocery-list
const listElement = document.querySelector(".grocery-list");
// Seleccionamos el botón de limpiar con la clase .clear-btn
const clearButton = document.querySelector(".clear-btn");

// Variables para la opción de edición
let currentEditElement;
let isEditing = false;
let currentEditID = "";

// ****** Escuchadores de eventos **********

// Evento para enviar el formulario
formElement.addEventListener("submit", handleAddItem);
// Evento para limpiar la lista
clearButton.addEventListener("click", handleClearItems);
// Evento para mostrar los elementos al cargar la página
window.addEventListener("DOMContentLoaded", initializeItems);

// ****** Funciones **********

// Función para añadir un elemento a la lista
function handleAddItem(event) {
  event.preventDefault(); // Prevenir el comportamiento por defecto del formulario
  const inputValue = groceryInput.value; // Obtener el valor del campo de entrada
  const uniqueID = new Date().getTime().toString(); // Generar un ID único

  // Si el valor no está vacío y no estamos en modo edición
  if (inputValue !== "" && !isEditing) {
    // Crear un nuevo elemento de la lista
    const newElement = document.createElement("article");
    let dataAttribute = document.createAttribute("data-id");
    dataAttribute.value = uniqueID;
    newElement.setAttributeNode(dataAttribute);
    newElement.classList.add("grocery-item");
    newElement.innerHTML = `<p class="title">${inputValue}</p>
            <div class="btn-container">
              <!-- Botón de editar -->
              <button type="button" class="edit-btn">
                <i class="fas fa-edit"></i>
              </button>
              <!-- Botón de eliminar -->
              <button type="button" class="delete-btn">
                <i class="fas fa-trash"></i>
              </button>
            </div>
          `;

    // Añadir los escuchadores de eventos a los botones de editar y eliminar
    const deleteButton = newElement.querySelector(".delete-btn");
    deleteButton.addEventListener("click", handleDeleteItem);
    const editButton = newElement.querySelector(".edit-btn");
    editButton.addEventListener("click", handleEditItem);

    // Añadir el nuevo elemento a la lista
    listElement.appendChild(newElement);
    // Mostrar una alerta de éxito
    showAlert("Elemento añadido a la lista", "success");
    // Mostrar el contenedor de la lista
    containerElement.classList.add("show-container");
    // Añadir el elemento al almacenamiento local
    addToLocalStorage(uniqueID, inputValue);
    // Restablecer los valores por defecto
    resetToDefault();
  } else if (inputValue !== "" && isEditing) {
    // Si estamos en modo edición, actualizar el elemento
    currentEditElement.innerHTML = inputValue;
    showAlert("Valor cambiado", "success");

    // Actualizar el almacenamiento local
    updateLocalStorage(currentEditID, inputValue);
    resetToDefault();
  } else {
    showAlert("Por favor, ingrese un valor", "danger");
  }
}

// Función para mostrar alertas
function showAlert(message, action) {
  alertElement.textContent = message;
  alertElement.classList.add(`alert-${action}`);
  // Remover la alerta después de 1 segundo
  setTimeout(function () {
    alertElement.textContent = "";
    alertElement.classList.remove(`alert-${action}`);
  }, 1000);
}

// Función para limpiar todos los elementos de la lista
function handleClearItems() {
  const allItems = document.querySelectorAll(".grocery-item");
  if (allItems.length > 0) {
    allItems.forEach(function (item) {
      listElement.removeChild(item);
    });
  }
  containerElement.classList.remove("show-container");
  showAlert("Lista vacía", "danger");
  resetToDefault();
  localStorage.removeItem("list");
}

// Función para eliminar un elemento de la lista
function handleDeleteItem(event) {
  const elementToDelete = event.currentTarget.parentElement.parentElement;
  const elementID = elementToDelete.dataset.id;

  listElement.removeChild(elementToDelete);

  if (listElement.children.length === 0) {
    containerElement.classList.remove("show-container");
  }
  showAlert("Elemento eliminado", "danger");

  resetToDefault();
  // Eliminar del almacenamiento local
  removeFromLocalStorage(elementID);
}

// Función para editar un elemento de la lista
function handleEditItem(event) {
  const elementToEdit = event.currentTarget.parentElement.parentElement;
  // Establecer el elemento a editar
  currentEditElement = event.currentTarget.parentElement.previousElementSibling;
  // Establecer el valor del formulario
  groceryInput.value = currentEditElement.innerHTML;
  isEditing = true;
  currentEditID = elementToEdit.dataset.id;
  submitButton.textContent = "Editar";
}

// Función para restablecer los valores por defecto
function resetToDefault() {
  groceryInput.value = "";
  isEditing = false;
  currentEditID = "";
  submitButton.textContent = "Enviar";
}

// ****** Almacenamiento local **********

// Función para añadir un elemento al almacenamiento local
function addToLocalStorage(id, value) {
  const groceryItem = { id, value };
  let items = getLocalStorage();
  items.push(groceryItem);
  localStorage.setItem("list", JSON.stringify(items));
}

// Función para obtener los elementos del almacenamiento local
function getLocalStorage() {
  return localStorage.getItem("list")
    ? JSON.parse(localStorage.getItem("list"))
    : [];
}

// Función para eliminar un elemento del almacenamiento local
function removeFromLocalStorage(id) {
  let items = getLocalStorage();

  items = items.filter(function (item) {
    return item.id !== id;
  });

  localStorage.setItem("list", JSON.stringify(items));
}

// Función para actualizar un elemento en el almacenamiento local
function updateLocalStorage(id, value) {
  let items = getLocalStorage();

  items = items.map(function (item) {
    if (item.id === id) {
      item.value = value;
    }
    return item;
  });
  localStorage.setItem("list", JSON.stringify(items));
}

// ****** Configuración inicial **********

// Función para inicializar los elementos al cargar la página
function initializeItems() {
  let items = getLocalStorage();

  if (items.length > 0) {
    items.forEach(function (item) {
      createListItem(item.id, item.value);
    });
    containerElement.classList.add("show-container");
  }
}

// Función para crear un nuevo elemento de la lista
function createListItem(id, value) {
  const newElement = document.createElement("article");
  let dataAttribute = document.createAttribute("data-id");
  dataAttribute.value = id;
  newElement.setAttributeNode(dataAttribute);
  newElement.classList.add("grocery-item");
  newElement.innerHTML = `<p class="title">${value}</p>
            <div class="btn-container">
              <!-- Botón de editar -->
              <button type="button" class="edit-btn">
                <i class="fas fa-edit"></i>
              </button>
              <!-- Botón de eliminar -->
              <button type="button" class="delete-btn">
                <i class="fas fa-trash"></i>
              </button>
            </div>
          `;
  // Añadir los escuchadores de eventos a los botones de editar y eliminar
  const deleteButton = newElement.querySelector(".delete-btn");
  deleteButton.addEventListener("click", handleDeleteItem);
  const editButton = newElement.querySelector(".edit-btn");
  editButton.addEventListener("click", handleEditItem);

  // Añadir el nuevo elemento a la lista
  listElement.appendChild(newElement);
}
