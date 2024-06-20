
const courses_endpoint = 'http://localhost:5000/courses';

async function searchCourses(){

    let search_field = document.getElementById('search_field');
    let search_value = search_field.value.trim();
    
    //si no hay info en el form de busqueda, usa la search query del buscador
    console.log(search_value)
    if(search_value.length < 0 || search_value === ""){
        search_value = window.location.search.replaceAll('%20', ' ').replaceAll('search_field', '').replaceAll('?=', '');
        console.log(search_value);
    }

    //si no se busca nada
    if(search_value.length < 0 || search_value === null || search_value === undefined){
        search_value = '1 = 1'; //por convencion, en mi API esta validado
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
        loadCoursesComponents(courses) //cargar los components
    }else{
        console.log(await response.text);
    }
}

async function loadCoursesComponents(courses){
    let courses_panel = document.getElementById('courses_panel');

    //limpiar los componentes existentes
    let current_components = document.querySelectorAll('#courses_panel > *');
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
                    <a class="stylish_link" href="course.html?course_id=${course.course_id}">
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

    //si no hay cursos, me muestra el mensajito
    if(courses.length == 0){
        document.getElementById('no_courses_message').style.display = 'block';
    }else{
        document.getElementById('no_courses_message').style.display = 'none';
    }

    for(var i = 0; i < courses.length; i++){
        let current_courseHTML = createCourseComponent(courses[i]);
        courses_panel.innerHTML += current_courseHTML;
    }

}