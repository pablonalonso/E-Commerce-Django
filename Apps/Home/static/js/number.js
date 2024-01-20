// Obtén referencias al span y al botón
const cartCount = document.getElementById('number');
const addButtons = document.querySelectorAll(".add-button")
const clearButton = document.getElementById('clear-button');


clearButton.addEventListener('click', function () {
  // Establece el valor del contador en 0
  cartCount.textContent = '0';

  // Guarda el nuevo valor (0) en el localStorage
  localStorage.setItem('cartCount', '0');
});


// Verifica si ya hay un valor en el localStorage
const storedCount = localStorage.getItem('cartCount');

// Si hay un valor en el localStorage, actualiza el contador con ese valor
if (storedCount) {
  cartCount.textContent = storedCount;
}

// Agrega un evento click al botón
addButtons.forEach(  button=>{
    button.addEventListener('click', ()=>{
        // Obtén el valor actual del contador y conviértelo a un número
          let currentCount = parseInt(cartCount.textContent);

          // Incrementa el contador en 1
          currentCount++;

          // Actualiza el valor en el span
          cartCount.innerHTML = currentCount;

          // Guarda el nuevo valor en el localStorage
          localStorage.setItem('cartCount', currentCount);
    })
    }
)


