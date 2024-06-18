
const user_endpoint = "http://localhost:5000/users";

async function isLoginFormValid(event){

    event.preventDefault();

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

    if(isValid){
        var formData = {
            username : username_field.value,
            user_password : password_field.value
        }

        var response = await fetch(user_endpoint + "/login", {
            method : 'POST',
            headers : {
                'Content-Type' : 'application/json'
            },
            body : JSON.stringify(formData)
        })

        if(response.status === 200){
            console.log("Usuario encontrado");
            user = await response.json();
            console.table(user);

            sessionStorage.setItem('user_id', user.id);
            //lanzar modo usuario registrado
            window.location.href = "../../../modules/user_mode/user_home.html";
        }else if(response.status == 400){
            login_field_error.textContent = 'Contraseña invalida';
            isValid = false;
        }else{
            login_field_error.textContent = 'Usuario no encontrado';
            isValid = false;
        }
    }

    //mensajit
    if(!isValid) login_field_error.style.display = 'block';

    return isValid;
}