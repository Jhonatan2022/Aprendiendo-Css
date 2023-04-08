// Api de rick and morty

// Funcion para obtener los datos de la api
const apiRick = async (pagina) => {
  // Url de la api con el parametro de la pagina
  let url = `https://rickandmortyapi.com/api/character/?page=` + pagina;
  let url2 = `https://rickandmortyapi.com/api/location`;

  // Obtener los datos de la api
  const api = await fetch(url);
  const api2 = await fetch(url2);

  // Convertir los datos a json
  const data = await api.json();
  const data2 = await api2.json();

  // Imprimir los datos en consola
  console.log(data);
  console.log(data2);

  // Imprimir los datos en cada elemento del html
  divRes = document.querySelector('#resultado');

  // Realizamos el cambia de pagina con el boton
  divRes.innerHTML = ""

  // Imprimir los datos en el html
  data.results.map (item => {

    // Buscar el nombre de la dimension en la api de locations
    const item2 = data2.results.find(l => l.url2 === item.origin.url2);
    
    // Crear un div para cada personaje
    divItem = document.createElement('div')

    // Agregarle la clase item e insertar el div en el html
    divItem.innerHTML = `

    <div class="card" style="width: 18rem;">
      <img class="card-img-top" src="${item.image}" alt="Card image cap">
      <div class="card-body">
        <h5 class="card-title"><i class="fa-solid fa-signature" ></i>--> ${item.name}</h5>
        <p class="card-text"><i class="fa-solid fa-dna" ></i>--> ${item.species}  </p>
      </div>
      <ul class="list-group list-group-flush">
        <li class="list-group-item"><i class="fa-solid fa-hashtag" ></i> Especimen: ${item.id}</li> 
        <li class="list-group-item"><i class="fa-solid fa-clock-rotate-left" ></i> Estado del especimen: ${item.status}</li>
        <li class="list-group-item"><i class="fa-solid fa-rocket" ></i> ${item2.dimension }</li>
      </ul>
    </div> 
    `
    // Insertar el div en el html por cada personaje que vaya recorriendo
    divRes.appendChild(divItem);
  });

};

// Funcion para imprimir los datos de la api
apiRick(1);