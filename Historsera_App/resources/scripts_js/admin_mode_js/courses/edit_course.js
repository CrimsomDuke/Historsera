const courses_endpoint = 'http://localhost:5000/courses';
const lectures_endpoint = 'http://localhost:5000/lectures';
const categories_endpoint = 'http://localhost:5000/categories';
const upload_file_endpoint = 'http://localhost:5000/upload_file';

async function loadCourse(){
    course_id = window.location.search.replaceAll('%20', ' ').replaceAll('course_id', '').replaceAll('?=', '');

    loadCategoriesOptions();

    if(course_id == 0){
        //hide lectures group
        document.getElementById('create_lecture_panel').style.display = 'none';
    }else{
        console.log('Loading course with id: ' + course_id);
        loadCourseDetails(course_id);
    }
}

async function save_course(){

    course_id = window.location.search.replaceAll('%20', ' ').replaceAll('course_id', '').replaceAll('?=', '');
    let has_error = false;

    if(course_id == 0){
        has_error =  createCourse();
    }else{
        has_error = updateCourse();
    }

    console.log(has_error);
}

async function createCourse(){   

    let formData = await getCourseInfo();

    var response = await fetch(courses_endpoint + '/create', {
        method: 'POST',
        headers : {
            'Content-Type' : 'application/json'
        },
        body: JSON.stringify(formData)
    });

    console.log(response);

    if(response.status == 200 || response.status == 201){
        alert('Curso creado con éxito');
        window.location.href = 'courses_manager.html';
        return true;
    } else {
        alert('Error creando el curso');
    }

    return false;

}

async function updateCourse(){

    let formData = await getCourseInfo();

    //remove ref_image_path field if it is empty
    if(!formData.ref_image_path){
        delete formData.ref_image_path;
    }

    var response = await fetch(courses_endpoint + '/update/' + course_id, {
        method: 'PUT',
        headers : {
            'Content-Type' : 'application/json'
        },
        body: JSON.stringify(formData)
    });

    if(response.status == 200 || response.status == 201){
        alert('Curso actualizado con éxito');
        window.location.href = 'courses_manager.html';
        return true;
    } else {
        alert('Error actualizando el curso');
    }

    return false;

}

async function loadCategoriesOptions(){
    var response = await fetch(categories_endpoint + "/get_all", {
        method: 'GET',
        headers : {
            'Content-Type' : 'application/json'
        }
    })

    let categories = await response.json();

    let category_field = document.getElementById('category_field');

    for(let i = 0; i < categories.length; i++){
        category_field.innerHTML += `
            <option value="${categories[i].category_name}">${categories[i].category_name}</option>
        `;
    }
}

async function loadCourseDetails(course_id){

    //load lectures
    loadLectures(course_id);

    var response = await fetch(courses_endpoint + '/get_by_id/' + course_id, {
        method: 'GET',
        headers : {
            'Content-Type' : 'application/json'
        }
    });

    let course = await response.json();

    let course_name_field = document.getElementById('course_name');
    let course_author_field = document.getElementById('course_author');
    let course_description_field = document.getElementById('course_description');
    let category_field = document.getElementById('category_field');

    course_name_field.value = course.course_name;
    course_author_field.value = course.author;
    course_description_field.value = course.description;
    category_field.value = course.category_name;

    if(course.ref_image_path){
        console.log('Course has image');
        document.getElementById('has_file_label').style.display = 'block';
    }
}

async function getCourseInfo(){
    let course_name_field = document.getElementById('course_name');
    let course_author_field = document.getElementById('course_author');
    let course_description_field = document.getElementById('course_description');
    let category_field = document.getElementById('category_field');


     //form validatiopns
    if(course_name_field.value == '' || course_author_field.value.length < 5){
        alert('Por favor ingrese un nombre de curso válido');
        return;
    }

    if(course_author_field.value == '' || course_author_field.value.length < 5){
        alert('Por favor ingrese un autor de curso válido');
        return;
    }

    if(course_description_field.value == '' || course_description_field.value.length < 5){
        alert('Por favor ingrese una descripción de curso válida');
        return;
    }

    //upload image
    let imagePath = await saveImageOfCourse();

    var formData = {
        course_name : course_name_field.value,
        author : course_author_field.value,
        description : course_description_field.value,
        category_name : category_field.value,
        ref_image_path : imagePath 
    }

    return formData;
}

async function loadLectures(course_id){
    var response = await fetch(lectures_endpoint + '/get_by_course_id/' + course_id, {
        method: 'GET',
        headers : {
            'Content-Type' : 'application/json'
        }
    });

    let lectures = await response.json();

    let lectures_panel = document.getElementById('lectures_panel');

    for(let i = 0; i < lectures.length; i++){
        lectures_panel.innerHTML += `
            <div class="lectures-item">
                <div class="lecture-info">
                    <p>${lectures[i].lecture_id}</p>
                    <p>${lectures[i].title}</p>
                </div>
                <div class="lecture-modifiers">
                    <a class="edit-lecture-button" href="../lectures/edit_lecture.html?lecture_id=${lectures[i].lecture_id}">Editar</a>
                    <a class="delete-lecture-button" href="../lectures/edit_lecture.html" onclick="deleteLecture(${lectures[i].lecture_id})">Eliminar</a>
                </div>
            </div>
        `;
    }

}


async function saveImageOfCourse(){
    var formData = new FormData();
    var file = document.getElementById('course_image').files[0];
    formData.append('file', file);

    var response = await fetch(upload_file_endpoint, {
        method: 'POST',
        body: formData
    });

    if(response.status == 200 || response.status == 201){
        let result = await response.json();
        return result.path; // Assuming the API returns the image path in the response
    } else {
        return null;
    }
}