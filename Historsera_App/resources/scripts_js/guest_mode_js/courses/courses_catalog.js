
const courses_endpoint = 'http://localhost:5000/courses';

async function searchCourses(event){
    event.preventDefault();
    console.log("xd")

    var isValid = true;

    let search_field = document.getElementById('search_field');
    let search_value = search_field.value.trim();
    
    if(search_value.length < 0 || search_value === null || search_value === undefined){
        search_value = '1 = 1';
    }

    var formData = {
        'search' : search_value
    }

    var response = await fetch(courses_endpoint + '/search', {
        method : 'POST',
        headers : {
            'Content-Type' : 'application/json'
        },
        body : JSON.stringify(formData)
    })

    if(response.status === 200 || response.status === 201){
        var courses = await response.json()
        console.table(courses);
        loadCourses(courses)
    }else{
        console.log(await response.text);
    }
}

async function loadCourses(courses){
    let courses_panel = document.getElementById('courses-panel');

    function createCourseComponent(course){
        let current_courseHTML = "";
        if(course != null){
            current_courseHTML = `
                <div class="courseComponent">
                    <a class="stylish_link" href="course.html?course_id=${course.course_id}">
                        <img src="${course.ref_image_path}" alt="imagen">
                        <div class="textDivisor">
                            <h4>${course.course_name}</h4>
                            <p>
                                ${course.description}
                            </p>  
                        </div>
                    </a>
                </div>
            `
        }

        return current_courseHTML;
    }

    for(var i = 0; i < courses.length; i++){
        let current_courseHTML = createCourseComponent(courses[i]);
        courses_panel.innerHTML += current_courseHTML;
    }

}