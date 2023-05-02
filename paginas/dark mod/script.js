// Código para activar el modo oscuro

// Creamos una constante para el botón de modo oscuro
// Usamos querySelector para seleccionar el elemento con el id "modo"
const modo = document.querySelector("#modo");


// Creamos una función flecha con un evento click para el botón de modo oscuro
modo.addEventListener("click", () => {

    // Agregamos la clase "dark" al body
    // Con classList.toggle agregamos o quitamos la clase "dark" al body
    document.body.classList.toggle("dark");

    // Agregamos la clase "on" al botón de modo oscuro
    modo.classList.toggle("encendido");



    // Guardamos el modo en localstorage para que se mantenga al actualizar
    // Creamos una condición para saber si el body tiene la clase "dark"
    // Usamos contains para saber si el body tiene la clase "dark"
    if (document.body.classList.contains("dark")) {

        // LOCALSTORAGE se refiere a una base de datos que se guarda en el navegador
        // Si el body tiene la clase "dark" guardamos el modo en localstorage como true
        localStorage.setItem("dark-mode", "true");
    } else {

        // Si el body no tiene la clase "dark" guardamos el modo en localstorage como false
        localStorage.setItem("dark-mode", "false");
    }
})


// Obtenemos el modo actual en localstorage
// Creamos una condición para saber si el modo actual es "true"
if (localStorage.getItem("dark-mode") === "true") {

    // Si el modo actual es "true" agregamos la clase "dark" al body
    document.body.classList.add("dark");

    // Agregamos la clase "on" al botón de modo oscuro
    modo.classList.add("encendido");
} else {

    // Si el modo actual es "false" quitamos la clase "dark" al body
    // Con classList.remove quitamos la clase "dark" al body
    document.body.classList.remove("dark");
}