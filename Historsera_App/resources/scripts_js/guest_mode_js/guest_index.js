
//validacion de los campos de form de registro
function isRegisterFormValid() {
    var username_field = document.getElementById('username_field');
    var email_field = document.getElementById('email_field');
    var password_field = document.getElementById('password_field');

    // Error labels
    var username_field_error = document.getElementById("username_field_error");
    var email_field_error = document.getElementById("email_field_error");
    var password_field_error = document.getElementById("password_field_error");

    var isValid = true;

    // Reset error messages visibility
    username_field_error.style.display = 'none';
    email_field_error.style.display = 'none';
    password_field_error.style.display = 'none';

    // Validate username
    var field_val = username_field.value;
    if (field_val === "" || field_val.length < 4) {
        username_field_error.style.display = 'block';
        username_field.focus();
        isValid = false;
    }

    // Validate email
    field_val = email_field.value;
    if (field_val === "" || field_val.length < 6 || !field_val.includes("@")) {
        email_field_error.style.display = 'block';
        email_field.focus();
        isValid = false;
    }

    // Validate password
    field_val = password_field.value;
    if (field_val === "" || field_val.length < 4) {
        password_field_error.style.display = 'block';
        password_field.focus();
        isValid = false;
    }

    console.log(isValid);
    return isValid;
}

