
const courses_endpoint = 'http://localhost:5000/courses';
const lectures_endpoint = 'http://localhost:5000/lectures';
const user_enrolled_in_course_endpoint = 'http://localhost:5000/user_enrolled_in_course';

async function loadCourseInfo(){

    user_id = sessionStorage.getItem('user_id');

    let course_id_search = window.location.search.replaceAll('%20', ' ')
        .replaceAll('course_id', '').replaceAll('?=', '');

    var response = await fetch(courses_endpoint + '/get_by_id/' + course_id_search, {
        method: 'GET',
        headers: {
            'Content-Type' : 'application/json'
        }
    })

    //si no se encuentra el curso, devolver al catalogo
    if(response.status == 404){
        alert('ID del curso invalido, redireccionando...')
        window.location.replace("courses_catalog.html");
        return;
    }

    var course_data = await response.json();

    let course_image = document.getElementById('course_image');
    let course_name_label = document.getElementById('course_name_label');
    let course_author_label = document.getElementById('course_author_label');
    let course_description_label = document.getElementById('course_description_label');
    
    //modificar los campos del header   
    course_image.src = course_data.ref_image_path;
    course_name_label.textContent = course_data.course_name;
    course_author_label.textContent = course_data.author;
    course_description_label.textContent = course_data.description;

    loadCourseLectures(course_id_search);

    //logica de mostrar controlles dependiendo de si ya esta inscrito
    if(await isEnrolled(user_id, course_id_search)){
        document.getElementById('join-button').style.display = 'none';
        document.getElementById('progress-bar').style.display = 'block';
    }else{
        document.getElementById('join-button').style.display = 'block';
        document.getElementById('progress-bar').style.display = 'none';
    }

    
}

async function loadCourseLectures(course_id){
    var response = await fetch(lectures_endpoint + '/get_by_course_id/' + course_id, {
        method: 'GET',
        headers: {
            'Content-Type' : 'application/json'
        }
    })

    function createLecturesItem(lecture){
        //redirige al login al estar en modo visitante
        let lecture_item_html = `
            <div class="lectureItem">
                <a class="stylish_link" href="../lectures/lecture.html?lecture_id=${lecture.lecture_id}">
                    <h3>${lecture.title}</h3>
                </a>
            </div>
        `

        return lecture_item_html;
    }

    if(response.status == 200 || response.status == 201){
        var lectures = await response.json();
        var lectures_group = document.getElementById('lectures_group');

        for(let i = 0; i < lectures.length; i++){
            lectures_group.innerHTML += createLecturesItem(lectures[i]);
        }
    }
}

async function isEnrolled(user_id, course_id){
    var response = await fetch(user_enrolled_in_course_endpoint + '/get_by_user_course?user=' + user_id + '&course=' + course_id, {
        method: 'GET',
        headers: {
            'Content-Type' : 'application/json'
        }
    })

    if(response.status == 200 || response.status == 201){
        return true;
        
    }else{
        return false;
    }

}