
const user_endpoint = 'http://localhost:5000/users';
const categories_endpoint = 'http://localhost:5000/categories';
const courses_endpoint = 'http://localhost:5000/courses';

async function login_while_creation(my_username, my_password){
    var formData = {
        username : my_username,
        user_password : my_password
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
        window.location.href = "resources/modules/user_mode/user_home.html";
    }
}   

//validacion de los campos de form de registro
async function isRegisterFormValid(event) {

    event.preventDefault();

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

    if(isValid){
        var formData = {
            username: username_field.value,
            email: email_field.value,
            user_password: password_field.value
        };

        var response = await fetch(user_endpoint + "/create", {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify(formData)
        })

        if(response.status === 200 || response.status === 201){
            alert("Usuario creado correctamente");
            //logea automaticamente al user
            login_while_creation(formData.username, formData.user_password)
        }else if(response.status === 400){
            username_field_error.textContent = 'El usuario ya existe';
            username_field_error.style.display = 'block';
            username_field.focus();
            isValid = false;

        }else{
            alert("Error al crear el usuario");
            isValid = false;
        }
    }

    return isValid;
}


async function loadCategories(){
    var response = await fetch(categories_endpoint + "/get_all", {
        method: 'GET',
        headers: {
            'Content-Type' : 'application/json'
        }
    });

    var data = await response.json();
    console.log(data);

    let categories_list = document.getElementById("categories_list");

    function createCategoryItem(category){
        let li = document.createElement('li');
        let a = document.createElement('a');
        a.id = category.category_name;
        a.href = "resources/modules/guest_mode/courses/courses_catalog.html?search_field=" + category.category_name;
        a.innerHTML = category.category_name;
        li.appendChild(a);
        return li;
    }

    if(data != null){
        for(var i = 0; i < 4; i++){ //solo 4 categorias de muesstra
            let current_category = createCategoryItem(data[i]);
            categories_list.appendChild(current_category);
        }
    }
}

async function loadHomeCourses(){
    var response = await fetch(courses_endpoint + "/get_all", {
        method: 'GET',
        headers: {
            'Content-Type' : 'application/json'
        }
    })

    var data  = await response.json();

    var courses_panel = document.getElementById('courses_panel');

    function createCourseComponent(course){
        let courseComponentHTML = `
            <div class="courseHomeComponent">
                <a class="stylish_link" href="resources/modules/guest_mode/courses/course.html?course_id=${course.course_id}">
                    <img src="${course.ref_image_path}" alt="imagen">
                    <p>${course.course_name}</p>
                </a>
            </div>
        `
        console.log(course.ref_image_path);
        return courseComponentHTML;
    }

    for(var i = 0; i < 4; i++){
        let current_courseHTML = createCourseComponent(data[i]);
        courses_panel.innerHTML += current_courseHTML;
    }
}

loadCategories();
loadHomeCourses();