
const lectures_endpoint = 'http://localhost:5000/lectures';
const courses_endpoint = 'http://localhost:5000/courses';
const upload_file_endpoint = 'http://localhost:5000/upload_file';

let course_id = 0;
let lecture_id = 0;

async function loadLecture(){

    //obtener los ids
    let ampersand_index = window.location.search.indexOf('&');
    course_id = window.location.search.substring(1, ampersand_index).replaceAll('%20', ' ').replaceAll('course_id', '').replaceAll('=', '');
    lecture_id = window.location.search.substring(ampersand_index + 1).replaceAll('%20', ' ').replaceAll('lecture_id', '').replaceAll('=', '');

    console.log(course_id);
    console.log(lecture_id);

    if(lecture_id == 0){
        //deshabilitar el campo de seleeccion de orden
        document.getElementById('order_num_label').style.display = 'none';
        document.getElementById('order_num_field').style.display = 'none';
    }else{
        console.log('Loading lecture with id: ' + lecture_id);

        //cargar detalles del curso
        await load_order_nums();
        let lecture_data = await getLecturesDetails(lecture_id);

        let lecture_name_field = document.getElementById('lecture_name');
        let lecture_link_field = document.getElementById('lecture_link');
        let lecture_description_field = document.getElementById('lecture_description');
        let order_num_field = document.getElementById('order_num_field');

        if(lecture_data.file_path != null){
            document.getElementById('no_file_label').style.display = 'block';
        }

        lecture_name_field.value = lecture_data.title;
        lecture_link_field.value = lecture_data.link;
        lecture_description_field.value = lecture_data.description;
        order_num_field.value = lecture_data.order_num;

    }
}

async function save_lecture(){

    let is_ok = false;
    
    if(lecture_id == 0){
        is_ok =  await createLecture();
    }else{
        is_ok = await updateLecture();
    }

    console.log('save pressed');
    if(is_ok){
        console.log('guardado')
        window.location.href = '../courses/edit_course.html?course_id=' + course_id;
    }
}

async function createLecture(){

    let lecture_name_field = document.getElementById('lecture_name');
    let lecture_link_field = document.getElementById('lecture_link');
    let lecture_description_field = document.getElementById('lecture_description');

    //limpiar los error labels
    document.getElementById('lecture_title_error').style.display = 'none';
    document.getElementById('lecture_link_error').style.display = 'none';
    document.getElementById('lecture_description_error').style.display = 'none';

    //validar
    if(lecture_name_field.value.length < 6 || lecture_name_field.value.length >  40){
        document.getElementById('lecture_title_error').style.display = 'block';
        return false;
    }

    if(lecture_link_field.value.lecture_data < 20){
        document.getElementById('lecture_link_error').style.display = 'block';
        return false;
    }

    if(lecture_description_field.value.length < 5){
        document.getElementById('lecture_description_error').style.display = 'block';
        return false;
    }

    let lecture_path = await save_file();

    let formData = {
        'title' : lecture_name_field.value,
        'description' : lecture_description_field.value,
        'is_video' : lecture_link.value == null ? false : true,
        'file_path' : lecture_path,
        'link' : lecture_link_field.value,
        'course_id' : course_id
    }

    var response = await fetch(lectures_endpoint + '/create', {
        method: 'POST',
        headers : {
            'Content-Type' : 'application/json'
        },
        body: JSON.stringify(formData)
    });

    if(response.status == 200 || response.status == 201){
        return true;
    }else{
        alert('Error creando la leccion');
    }
    return false;
}

async function updateLecture(){

    let lecture_name_field = document.getElementById('lecture_name');
    let lecture_link_field = document.getElementById('lecture_link');
    let lecture_description_field = document.getElementById('lecture_description');

    let lecture_path = await save_file();

    //cambiar el orden
    let order_num_field = document.getElementById('order_num_field');
    let new_lecture_order = await change_order_num(lecture_id, order_num_field.value);

    let formData = {
        'title' : lecture_name_field.value,
        'description' : lecture_description_field.value,
        'is_video' : lecture_link.value == null ? false : true,
        'file_path' : lecture_path,
        'link' : lecture_link_field.value,
        'course_id' : course_id
    }

    var response = await fetch(lectures_endpoint + '/update/' + lecture_id, {
        method: 'PUT',
        headers : {
            'Content-Type' : 'application/json'
        },
        body: JSON.stringify(formData)
    });

    if(response.status == 200 || response.status == 201){
    }else{
        alert('Error actualizando la leccion');
    }

    return false;

}

async function getLecturesDetails(lecture_id){
    var response = await fetch(lectures_endpoint + '/get_by_id/' + lecture_id, {
        method: 'GET',
        headers : {
            'Content-Type' : 'application/json'
        }
    });

    let lecture_data = await response.json();

    return lecture_data;
}

async function load_order_nums(){
    let response = await fetch(courses_endpoint + '/get_order_nums/' + course_id, {
        method: 'GET',
        headers : {
            'Content-Type' : 'application/json'
        }
    });

    let order_nums = await response.json();

    let order_num_field = document.getElementById('order_num_field');
    for(let i = 0; i < order_nums.order_nums_list.length; i++){
        let option_string = '<option value="' + order_nums.order_nums_list[i] + '">' + order_nums.order_nums_list[i] + '</option>';
        order_num_field.innerHTML += option_string;
    }
}

async function change_order_num(lecture_id, new_order_num){
    let formData = {
        'lecture_id' : lecture_id,
        'new_order_num' : new_order_num
    }

    var response = await fetch(lectures_endpoint + '/change_order/' + lecture_id + "/" + new_order_num, {
        method: 'PUT',
        headers : {
            'Content-Type' : 'application/json'
        },
        body: JSON.stringify(formData)
    });

    let result = await response.json();
    return result;
}

async function save_file(){
    let formData = new FormData();
    let file = document.getElementById('lecture_file').files[0];

    formData.append('file', file);

    var response = await fetch(upload_file_endpoint, {
        method : 'POST',
        body : formData
    })

    console.log(response)

    if(response.status == 200){
        let result = await response.json();
        return result.path;
    }else{
        return null;
    }
}

function cancel(){
    window.location.href = '../courses/edit_course.html?course_id=' + course_id;
}