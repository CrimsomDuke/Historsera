
function isLoginFormValid(){
    var username_field = document.getElementById('username_field');
    var password_field = document.getElementById('password_field');
    // Error labels
    var login_field_error = document.getElementById("login_field_error");

    var field_val;
    var isValid = true;

    // Reset error messages visibility

    //validaciones en cliente
    //username
    field_val = username_field.value;
    if(field_val == "") {
        username_field.focus();
        isValid = false;
    }
    //password
    field_val = password_field.value;
    if(field_val == ""){
        password_field.focus();
        isValid = false;
    }
    
    //mensajit
    if(!isValid) login_field_error.style.display = 'block';

    return isValid;
}