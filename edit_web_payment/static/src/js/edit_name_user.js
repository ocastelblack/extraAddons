function changesNameLabel() {
    var selectElement = document.getElementById("identification_type_id");
    var selectValue = selectElement.value;

    // Obtener el label existente
    var existingLabel = document.querySelector('label[for="name"]');

    // Crear una nueva etiqueta con el texto deseado
    var newLabel = document.createElement('label');
    newLabel.setAttribute('class', 'col-form-label');
    newLabel.setAttribute('for', 'name');

    if (selectValue == "NIT") {
        newLabel.textContent = "Nombre empresa";
    } else {
        newLabel.textContent = "Nombres y Apellidos";
    }

    // Reemplazar la etiqueta existente con la nueva etiqueta
    existingLabel.parentNode.replaceChild(newLabel, existingLabel);
}
