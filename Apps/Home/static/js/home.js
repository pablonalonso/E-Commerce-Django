const gallery = new Muuri('.gallery', {
    layout: {
        rounding: false,
      }
});

window.addEventListener('load', ()=>{
    document.getElementById('gallery').classList.add('load-gallery');

    const links = document.querySelectorAll(".category");

    //Event listener for the links
    links.forEach( (link)=>{
        link.addEventListener('click', (event)=>{
            links.forEach( (link)=> link.classList.remove("active"))
            event.target.classList.add("active")
            const category = event.target.innerHTML;
            category === 'Todo' ?  gallery.filter(`[data-category]`) : gallery.filter(`[data-category=${category}]`)
        });
    } );

    //Event listener for the search bar
    document.querySelector("#search-bar").addEventListener('input', (event)=>{
        const search = event.target.value;
        gallery.filter(  (item)=> item.getElement().dataset.etiquette.includes(search) );
    })


});

// Obtener el elemento del loader
const loader = document.getElementById('loader');

// Mostrar el loader inicialmente
loader.style.display = 'block';

// Esperar 1 segundo (1000 milisegundos) y luego ocultar el loader
setTimeout(() => {
    loader.style.display = 'none';
}, 1000);