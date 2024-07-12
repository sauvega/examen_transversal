

function editar(boolean) {
  $('#editar').prop('checked', boolean);
}
$(document).ready(function() {
  $("#productos").validate({
    rules: {
      id: {
        required: true,
      },
      categoria: {
        required: true
      },
      nombre: {
        required: true,
        letrasYEspacios: false,
      },
      descripcion: {
        required: true
      },
      precio: {
        required: true,
        minlength: 4,
          
      },
      descuento_subscriptor: {
        required: true,
      },
      descuento_oferta: {
        required: true,
      }
    },
    messages: {
      id: {
        required: "Campo obligatorio",
      },
      categoria: {
        required: "Campo obligatorio"
      },
      nombre: {
        required: "Campo obligatorio"
      },
      descripcion: {
        required: "Campo obligatorio"
      },
      precio: {
        required: "Campo obligatorio",
        minlength: "El precio debe tener un mínimo de 4 caracteres",
      },
      descuento_subscriptor: {
        required: "Campo obligatorio",
      },
      descuento_oferta: {
        required: "Campo obligatorio",
      }
    },
    errorPlacement: function(error, element) {
      error.insertAfter(element);
    },
    submitHandler: function(form) {
      form.submit();
    }
  });
  $('#guardar_producto').click(function(event) {
    event.preventDefault();
    $('#editar').prop('checked', true);

    $('#productos').submit();
  });
  $('#nuevo_producto').click(function(event) {  
    event.preventDefault();
    editar(false);
    $('#productos').submit();
  });
});