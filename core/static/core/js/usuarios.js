$(document).ready(function() {
  
    $('#form').validate({ 
        rules: {
          'username': {
            required: true,
          },
          'nombre': {
            required: true,
            soloLetras: true,
          },
          'apellido': {
            required: true,
            soloLetras: true,
          },
          'correo': {
            required: true,
            emailCompleto: true,
          },
          'rut': {
            required: true,
            rutChileno: true,
          },
          'direccion': {
            required: true,
          },
          'imagen': {
            required: false,
          },
        },
        messages: {
          imagen: {
            required: "Campo obligatorio",
          },
          'username': {
            required: 'Debe ingresar un nombre de usuario',
          },
          'nombre': {
            required: 'Debe ingresar su nombre',
            soloLetras: "El nombre sólo puede contener letras y espacios en blanco",
          },
          'apellido': {
            required: 'Debe ingresar sus apellidos',
            soloLetras: "Los apellidos sólo pueden contener letras y espacios en blanco",
          },
          'correo': {
            required: 'Debe ingresar su correo',
            emailCompleto: 'El formato del correo no es válido',
          },
          'rut': {
            required: 'Debe ingresar su RUT',
            rutChileno: 'El formato del RUT no es válido',
          },
          'direccion': {
            required: 'Debe ingresar su dirección',
          },
        },
        errorPlacement: function(error, element) {
          error.insertAfter(element); 
          error.addClass('error-message');
        },
    });
    $('#actualizar_usuario').click(function(event) {
      event.preventDefault();
      // submit with AJAX
      if ($('#form').valid()) {
        $('#form').submit();
        return
      }
    });
});