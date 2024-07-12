$(document).ready(function() {

    
    $('#id_username').attr('placeholder', 'Ej: cgomezv, cevans, sjohasson');
    $('#id_first_name').attr('placeholder', 'Ej: Cristián, Chris, Scarlett');
    $('#id_last_name').attr('placeholder', 'Ej: Gómez Vega, Evans, Johansson');
    $('#id_email').attr('placeholder', 'Ej: cevans@marvels.com');
    $('#id_password1').attr('placeholder', '8 caracteres como mínimo');
    $('#id_password2').attr('placeholder', 'Repetir la contraseña escogida');
    $('#id_rut').attr('placeholder', 'Ej: 11111111-1 (sin puntos y con guión)');
    $('#id_direccion').attr('placeholder', 'Calle, n° casa o edificio, n° departamento o piso\n'
      + 'localidad o ciudad, código postal o de área\n'
      + 'estado o provincia, ciudad, país');
  
    // Agregar una validación por defecto para que la imagen la exija como campo obligatorio
    $.extend($.validator.messages, {
      required: "Este campo es requerido",
    });
  
    $('#form').validate({ 
        rules: {
          'username': {
            required: true,
          },
          'first_name': {
            required: true,
            soloLetras: true,
          },
          'last_name': {
            required: true,
            soloLetras: true,
          },
          'email': {
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
          'password1': {
            required: true,
            minlength: 8,
          },
          'password2': {
            required: true,
            equalTo: '#password1'
          }
        },
        messages: {
          'username': {
            required: 'Debe ingresar un nombre de usuario',
          },
          'first_name': {
            required: 'Debe ingresar su nombre',
            soloLetras: "El nombre sólo puede contener letras y espacios en blanco",
          },
          'last_name': {
            required: 'Debe ingresar sus apellidos',
            soloLetras: "Los apellidos sólo pueden contener letras y espacios en blanco",
          },
          'email': {
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
          'password1': {
            required: 'Debe ingresar una contraseña',
            minlength: 'La contraseña debe tener al menos 8 caracteres',
          },
          'password2': {
            required: 'Debe ingresar una contraseña',
            equalTo: 'Debe repetir la contraseña anterior'
          }
        },
        errorPlacement: function(error, element) {
          error.insertAfter(element); 
          error.addClass('error-message');
        },
    });
    $('#crear_usuario').click(function(event) {
      event.preventDefault();
      // submit with AJAX
      if ($('#form').valid()) {
        $('#form').submit();
        return
        $.ajax({
          url: $('#form').attr('action'),
          type: 'POST',
          data: $('#form').serialize(),
          success: function(response) {
            Swal.fire({
              title: 'Usuario creado con éxito',
              text: 'Se ha creado un nuevo usuario en la base de datos',
              icon: 'success',
              showClass: {
                popup: 'animate__animated animate__fadeInDown'
              },
              hideClass: {
                popup: 'animate__animated animate__fadeOutUp'
              }
            });
            $('#limpiar_formulario').click();
          },
          error: function(response) {
            Swal.fire({
              title: 'Error al crear el usuario',
              text: 'Ha ocurrido un error al intentar crear el usuario',
              icon: 'error',
              showClass: {
                popup: 'animate__animated animate__fadeInDown'
              },
              hideClass: {
                popup: 'animate__animated animate__fadeOutUp'
              }
            });
          }
        });
      }
    });
});