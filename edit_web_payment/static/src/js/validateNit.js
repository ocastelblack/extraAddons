document.getElementById('nit_check').addEventListener('blur', function () {
    var identificationType = document.querySelector('select[name="identification_type_id"]').value;
    if (identificationType === '4') {
        var nit = this.value;
        if (!isValidNITFormat(nit)) {
            alert('El formato del NIT ingresado no es válido. Debe ser XXX.XXX.XXX - Y');
            this.value = ''; // Limpiar el campo
        }
    }
});

function isValidNITFormat(nit) {
    var regex = /^\d{3}\.\d{3}\.\d{3} - \d$/;// Formato esperado: 123.456.789 - 0
    return regex.test(nit);
}