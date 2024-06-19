
user_endpoint = 'http://localhost:5000/users'
user_enrolled_in_course_endpoint = 'http://localhost:5000/user_enrolled_in_course';

async function loadUserInfo(){
    user_id = sessionStorage.getItem('user_id')

    var response = await fetch(user_endpoint + '/get_by_id/' + user_id, {
        method : 'GET',
        headers : {
            'Content-Type' : 'application/json'
        }
    });

    if(response.status === 400 || response.status === 404){
        alert('Error al cargar la informacion del usuario');
        window.location.replace('../../../index.html');
        return;
    }

    var user = await response.json();

    //cargar username
    document.getElementById('username-label').textContent = user.username;

    //cargar cursos
    loadUserCourses();


}

async function loadUserCourses(){
    user_id = sessionStorage.getItem('user_id')

    var response = await fetch(user_enrolled_in_course_endpoint + '/get_by_user_id/' + user_id, {
        method : 'GET',
        headers : {
            'Content-Type' : 'application/json'
        }
    });

    if(response.status === 400 || response.status === 404){
        return;
    }

    var courses = await response.json();

    if(courses.length === 0){
        document.getElementById('no_courses_label').style.display = 'block';
    }else{
        document.getElementById('no_courses_label').style.display = 'none';
    }

    console.log(courses);

    //cargar cursos
    loadCoursesComponents(courses);
}

async function loadCoursesComponents(courses){
    let my_courses_panel = document.getElementById('my_courses_panel');

    //limpiar los componentes existentes
    let current_components = document.querySelectorAll('#my_courses_panel > *');
    console.log(current_components);
    if(current_components != null) {
        for(let i = 0; i < current_components.length; i++){
            current_components[i].remove(); 
        }
    }

    function createCourseComponent(course){
        let current_courseHTML = "";
        current_courseHTML = `
                <div class="courseComponent">
                    <a class="stylish_link" href="courses/course.html?course_id=${course.course_id}">
                        <img src="${course.ref_image_path}" alt="imagen">
                        <div class="textDivisor">
                            <h4>${course.course_name}</h4>
                            <p>${course.author}</p>
                            <p>${course.category_name}</p>
                            <p>
                                ${course.description}
                            </p>  
                        </div>
                    </a>
                </div>
            `
        return current_courseHTML;
    }

    for(var i = 0; i < courses.length; i++){
        my_courses_panel.innerHTML += createCourseComponent(courses[i]);
    }


}