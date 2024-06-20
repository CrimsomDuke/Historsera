const user_endpoint = "http://localhost:5000/users";
const admin_endpoint = "http://localhost:5000/administrators";

async function loadUserInfo(){
    var user_id = sessionStorage.getItem('user_id');

    var response = await fetch(user_endpoint + "/get_by_id/" + user_id);
    var user = await response.json();

    let is_user_admin = await isUserAdmin();

    console.table(user);

    let username_field = document.getElementById('username-field');
    let email_field = document.getElementById('email-field');
    let points_field = document.getElementById('points-field');
    let title_field = document.getElementById('title-field');

    //asign the values to the fields
    username_field.textContent = user.username;
    email_field.textContent = user.email;
    points_field.textContent = user.points;

    //adminbuto
    let admin_mode_button = document.getElementById('admin-mode-button');

    if(user.title == null) title_field.textContent = "No title";
    else title_field.textContent = user.title;

    console.log(is_user_admin)

    if(is_user_admin){
        admin_mode_button.style.display = "block";
    }
}

function closeSession(){
    sessionStorage.clear();
    window.location.href = "../../../index.html";
}

function goToAdminMode(){
    window.location.href = "../admin_mode/admin_index.html";
}

async function isUserAdmin(){
    var user_id = sessionStorage.getItem('user_id');
    var response = await fetch(admin_endpoint + "/get_admin_by_user_id/" + user_id);
    if(response.status == 200 || response.status == 201){
        return true;
    }
    return false;
}