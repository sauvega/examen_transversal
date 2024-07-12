$(document).ready(function() {
    $('#nombre').change(function() {
      var nombre = $(this).find(':selected').data('nombre');
      var image = '/media/'+$(this).find(':selected').data('imagen');
      $('#imagen_producto').attr('src', image); 
      $('#imagen_producto').attr('alt', `Imagen de ${nombre}`);
    });
  
    var select = document.querySelector('select[name="producto"]');
    if (select) {
        var defaultOption = select.querySelector('option[value=""]');
        if (defaultOption) {
            defaultOption.text = "Seleccione un producto";
        }
    }
  
    $('#bodega').validate({ 
      rules: {
          'producto': {
              required: true,
              min: 1,
          },
          'cantidad': {
              required: true,
              number: true,
          },
      },
      messages: {
          'producto': {
              required: 'Debe seleccionar el nombre del producto',
              min: 'Debe seleccionar el nombre del producto',
          },
          'cantidad': {
              required: 'Debe ingresar la cantidad',
              number: 'Debe ingresar un número',
              digits: 'Debe ingresar un número entero',
          },
      },
      errorPlacement: function(error, element) {
          error.insertAfter(element);
          error.addClass('error-message'); 
      },
    });

    $('#guardar_bodega').click(function(event) {

    });
  
  });
  