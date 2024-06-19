
const lectures_endpoint = 'http://localhost:5000/lectures';
const user_takes_lecture_endpoint = 'http://localhost:5000/user_takes_lecture';

const user_id = sessionStorage.getItem('user_id');

async function loadLectureInfo(){

    //obtenemos el parametor y chao chars innecesarios
    let lecture_id = window.location.search.replaceAll('%20', ' ')
        .replaceAll('lecture_id', '').replaceAll('?=', '');

    if(await can_take_lecture(user_id, lecture_id)) console.log('Lecture just taken');
    else console.log('Lecture was taken before');

    var response = await fetch(lectures_endpoint + '/get_by_id/' + lecture_id, {
        method: 'GET',
        headers: {
            'Content-Type' : 'application/json'
        }
    })

    //si no se encuentra la lectura, devolver al catalogo
    if(response.status == 404){
        alert('ID de la lectura invalido, redireccionando...')
        window.location.replace("../courses/courses_catalog.html");
        return;
    }

    var lecture_data = await response.json();
    console.log(lecture_data);

    let title_field = document.getElementById('title-field');
    let description_field = document.getElementById('description-field');
    let pdf_viewer = document.getElementById('pdf-viewer');
    let video_player = document.getElementById('video-player');

    //we asign the data to the fields
    title_field.textContent = lecture_data.title;
    description_field.textContent = lecture_data.description;

    if(lecture_data.file_path != null){
        pdf_viewer.style.display = 'block';
        pdf_viewer.src = lecture_data.file_path;
    }else{
        pdf_viewer.style.display = 'none';
    }

    //limpiar el id del video de YT
    if(lecture_data.link != null){
        let video_id = getYoutubeVideoID(lecture_data.link);
        video_player.src = 'https://www.youtube.com/embed/' + video_id;
    }else{
        video_player.style.display = 'none';
    }

    //ocultar boton anterior si es la primera leccion
    if(lecture_data.order_num == 1){
        document.getElementById('previous-button').style.display = 'none';
    }


}

async function next_lecture(){

    //we get the current lecture id and the user
    let user_id = sessionStorage.getItem('user_id');
    let current_lecture_id = window.location.search.replaceAll('%20', ' ')
        .replaceAll('lecture_id', '').replaceAll('?=', '');

    var response = await fetch(lectures_endpoint + '/get_next_lecture_id?lecture_id=' + current_lecture_id, {
        method: 'GET',
        headers: {
            'Content-Type' : 'application/json'
        }
    })

    if(response.status == 404){
        alert('No hay mas lecturas en este curso');
        return;
    }

    //nota: no olvidar el await NUNCA MAS, carajo
    await markLectureAsFinished();
    var next_lecture = await response.json();
    var next_lecture_id = next_lecture.next_lecture_id;

    //redirecciona a la siguiente lectura
    window.location.replace('lecture.html?lecture_id=' + next_lecture_id);
    return;
}

async function previous_lecture(){
        //we get the current lecture id and the user
        let user_id = sessionStorage.getItem('user_id');
        let current_lecture_id = window.location.search.replaceAll('%20', ' ')
            .replaceAll('lecture_id', '').replaceAll('?=', '');
    
        var response = await fetch(lectures_endpoint + '/get_previous_lecture_id?lecture_id=' + current_lecture_id, {
            method: 'GET',
            headers: {
                'Content-Type' : 'application/json'
            }
        })
    
        if(response.status == 404){
            alert('No hay mas lecturas en este curso');
            return;
        }
    
        //nota: no olvidar el await NUNCA MAS, carajo
        await markLectureAsFinished();
        var previous_lecture = await response.json();
        var previous_lecture_id = previous_lecture.previous_lecture_id;
    
        //redirecciona a la siguiente lectura
        window.location.replace('lecture.html?lecture_id=' + previous_lecture_id);
}

async function can_take_lecture(user_id, lecture_id){
    
    //if the user has not taken the lecture, we create the record and return true
    //if he did, then return false
    var response = await fetch(user_takes_lecture_endpoint + '/create' ,{
        method: 'POST',
        headers: {
            'Content-Type' : 'application/json'
        },
        body: JSON.stringify({'user_id' : user_id, 'lecture_id' : lecture_id})
    })

    if(response.status == 200 || response.status == 201){
        return true;
    }else{
        return false;
    }
}

async function markLectureAsFinished(){

    let lecture_id = window.location.search.replaceAll('%20', ' ').replaceAll('lecture_id', '').replaceAll('?=', '');
    let user_id = sessionStorage.getItem('user_id');

    var response = await fetch(user_takes_lecture_endpoint + '/complete_lecture' ,{
        method: 'PUT',
        headers: {
            'Content-Type' : 'application/json'
        },
        body: JSON.stringify({'user_id' : user_id, 'lecture_id' : lecture_id})
    })

    if(response.status != 200){
        console.log(response.json());
        console.error('Error al marcar la lectura como terminada')
        return;
    }
    
    console.log('Lecture marked as finished');

}

function getYoutubeVideoID(link){
    let video_id = link.split('v=')[1]; //me quedo con el id del video
    let ampersand_position = video_id.indexOf('&');
    if(ampersand_position != -1){
        video_id = video_id.substring(0, ampersand_position);
    }
    return video_id;
}