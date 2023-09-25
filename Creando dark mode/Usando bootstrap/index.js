const themaC = () => {
  // Usamos setAttribute para agregar un atributo al body y le pasamos el nombre del atributo y el valor
  document.querySelector("body").setAttribute("data-bs-theme", "light");

  // Seleccionamos el boton y su id para cambiar también el icono
  document.querySelector("#modo").setAttribute("class", "fas fa-moon");
};

const themaO = () => {
  // Seleccionamos el body y le agregamos el tema que recibimos por props
  document.querySelector("body").setAttribute("data-bs-theme", "dark");

  // Seleccionamos el boton y su id para cambiar también el icono
  document.querySelector("#modo").setAttribute("class", "fas fa-sun");
};

const alternarTema = () => {
  // Usamos getAttribute para obtener el valor del atributo que le pasamos
  document.querySelector("body").getAttribute("data-bs-theme") === "dark"
    ? themaC()
    : themaO();
};