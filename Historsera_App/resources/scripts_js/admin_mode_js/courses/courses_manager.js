
const courses_endpoint = 'http://localhost:5000/courses';

async function loadCourses(){
    let courses = await fetch(courses_endpoint + '/get_all', {
        method: 'GET',
        headers: {
            'Content-Type': 'application/json'
        }
    })
    courses = await courses.json()

    let courses_panel = document.getElementById('courses_panel')

    function createCourseItem(course){
        let course_item_HTML = `
            <div class="courses-item">
                <div class="course-info">
                    <p>${course.course_id}</p>
                    <p>${course.course_name}</p>
                </div>
                <div class="course-modifiers">
                    <a class="edit-course-button" href="edit_course.html?course_id=${course.course_id}">Editar</a>
                    <a class="delete-course-button" onclick="deleteCourse('${course.course_id}')">Eliminar</a>
                </div>
            </div>
        `
        return course_item_HTML;
    }

    for(let course of courses){
        courses_panel.innerHTML += createCourseItem(course);
    }
}