categories_endpoint = 'http://localhost:5000/categories';

async function loadCategories(){
    var response = await fetch(categories_endpoint + '/get_all');
    var categories = await response.json();

    let categories_panel = document.getElementById('categories_panel');

    function createCategoryItem(category){
        let categories_item_HTML = `
            <div class="category-item">
                <p>${category.category_name}</p>
                <button type="button" onclick="deleteCategory('${category.category_name}')">Borrar</button>
            </div>
        `
        return categories_item_HTML;
    }

    for(let category of categories){
        categories_panel.innerHTML += createCategoryItem(category);
    }

}

async function deleteCategory(category_name){
    var response = await fetch(categories_endpoint + '/delete/' + category_name, {
        method: 'DELETE',
        headers: {
            'Content-Type': 'application/json'
        }
    });

    if(response.status == 200){
        location.reload();
    }else if(response.status == 400){
        alert('La categoria no existe o no se puede eliminar porque tiene cursos asociados');
    }else{
        alert('Error al eliminar la categoria');
    }
}

async function createCategory(){

    let category_name = document.getElementById('category_field').value;

    //validations
    if(category_name.length > 50){
        alert('El nombre de la categoria no puede tener mas de 50 caracteres');
        return;
    }

    if(category_name.length < 5){
        alert('El nombre de la categoria no puede tener menos de 5 caracteres');
        return;
    }

    var response = await fetch(categories_endpoint + '/create', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({
            category_name: category_name
        })
    });

    console.log(response.status);
    if(response.status == 200 || response.status == 201){
        location.reload();
    }else{
        alert('Error al crear la categoria');
    }
}