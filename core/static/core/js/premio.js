$(document).ready(function(){
  $.get('https://fakestoreapi.com/products', function(data){
      $.each(data, function(i, item){
        let html = `
        <div class="col-sm-12 col-md-6 col-lg-4 col-xl-3">
            <div class="card" style="width: 18rem;">
            <img src="${item.image}" class="card-img-top" alt="${item.title}">
            <div class="card-body">
                <h5 class="card-title">${item.title}</h5>
                <p class="card-text">${item.description}</p>
                <a href="#" class="btn btn-primary">Agregar al carrito</a>
            </div>
            </div>
        </div>
        `;
        $('#products-container').append(html);
    });
  });
});