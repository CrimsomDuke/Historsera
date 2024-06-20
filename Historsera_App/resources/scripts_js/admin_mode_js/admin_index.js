
const user_endpoint = "http://localhost:5000/users";

async function loadAdminInfo(){
    var user_id = sessionStorage.getItem('user_id');

    var response = await fetch(user_endpoint + "/get_by_id/" + user_id);
    var user = await response.json();

    document.getElementById('username_label').textContent = user.username;

}