$(document).ready(function() {

  // Asignar placeholders para ayudar a los usuarios
  $('#id_username').attr('placeholder', 'ingresa tu usuario');
  $('#id_password').attr('placeholder', 'Ingesa tu contraseña');
  $.extend($.validator.messages, {
    required: "Este campo es requerido",
  });
  $('#form').validate({ 
    errorPlacement: function(error, element) {
        error.insertAfter(element);
    },
    submitHandler: function(form) {
        form.submit();
    }
  });

  $('#user-select').change(function() {
    var username = $(this).val();
    var password = 'Duoc@123';
    if ('cevans eolsen tholland sjohansson cpratt mruffalo super'.includes(username)) {
      password = '123';
    };
    $('#id_username').val(username);
    $('#id_password').val(password);
  });

});
