//obtenemos la url para identificar el addrees de la pagina
inFormPage=window.location.href.includes("address");
if (inFormPage){
    // Obtener elementos HTML
    var nameInput = document.getElementById("js-label-nombre");
    var labelId = document.getElementById("label_numero_identificacion");
    var SelectTipo = document.getElementById("identification_type_id");
    var paisId = document.getElementById("country_id");
    var departamentoId = document.querySelector('select[name="state_id"]');
    var inputNID = document.getElementById("nit_check");
    
    if (inputNID) {
        if(inputNID.value == ""){
            paisId.value = "49"; // Valor del país por defecto (49 en este caso)
            if(paisId.value == "49"){
                departamentoId.value = "649";// Valor del departamento por defecto (649 en este caso)
            }
            //console.log(inputNID.value);
        }
    }
    
    $(document).ready(function() {
        // Función para actualizar el campo "name" según la selección
        function updateNameField() {
            var selectedtipo = SelectTipo.value;
            if (selectedtipo === "4") {
                    nameInput.textContent = "Nombre de la empresa"; // Valor para empresas
                    labelId.textContent = "Nit empresa (obligatorio)";
                    inputNID.placeholder = "ej: 900850351-1";
                } else {
                    nameInput.textContent = "Nombres y apellidos"; // Valor para nombres y apellidos
                    labelId.textContent = "Número de Identificación (Obligatorio)";
                    inputNID.placeholder = "ej: 1234567890";
                }
        }
        // Escuchar cambios en el select de país
        SelectTipo.addEventListener("change", updateNameField);
        // Llamar a la función inicialmente para configurar el valor inicial del campo "name"
        updateNameField();
    });

    document.addEventListener("DOMContentLoaded", function() {
        const phoneInput = document.getElementById("phone");
    
        phoneInput.addEventListener("input", function() {
            // Remover espacios y puntos del valor ingresado
            const formattedPhone = this.value.replace(/[\s.]/g, "");
    
            // Validar si el número es válido (solo dígitos)
            if (/^\d+$/.test(formattedPhone)) {
                // Formatear el número con los espacios deseados
                const formattedOutput = formattedPhone.replace(/(\d{3})(\d{2})(\d{4})(\d{1})(\d{7})/, "$1 $2 $3 $4 $5");
                this.value = formattedOutput;
                this.style.borderColor = ""; // Restaurar el color del borde
            } else {
                // Si no es un número válido, cambiar el color del borde a rojo
                this.style.borderColor = "red";
                alert("Solo se aceptan números, no se admiten puntos ni espacios.");
            }
        });
    });
}