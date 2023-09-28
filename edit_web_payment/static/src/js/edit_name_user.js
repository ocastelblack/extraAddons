// $(document).ready(function() {
//     var selectElement = document.getElementById("identification_type_id");
//     var labelElement = document.getElementById("js-label-nombre");
//     selectElement.on('change', function() {
//         var selectedValue = selectElement.val();
//         if (selectedValue == 4) {
//             labelElement.text('Empresa');
//         } else {
//             labelElement.text('Nombres y Apellidos');
//         }
//     });
// });

// odoo.define('edit_web_payment.edit_name_user', function (require) {
//     "use strict";

//     var core = require('web.core');
//     var ajax = require('web.ajax');
//     var _t = core._t;
//     var QWeb = core.qweb;
    
//     $(document).ready(function() {
//         var selectElement = document.getElementById("identification_type_id");
//         var labelElement = document.getElementById("js-label-nombre");

//         selectElement.addEventListener('change', function() {
//             var selectedValue = selectElement.value;
//             if (selectedValue == 4) {
//                 labelElement.textContent = 'Empresa';
//             } else {
//                 labelElement.textContent = 'Nombres y Apellidos';
//             }
//         });
//     });
// });

odoo.define("edit_web_payment.edit_name_user", function (require) {"use strict";
    alert("Hello world");
    $(document).ready(function() {
        var selectElement = document.getElementById("identification_type_id");
        var labelElement = document.getElementById("js-label-nombre");
    
        if (selectElement && labelElement) {
            selectElement.addEventListener('change', function() {
                var selectedValue = selectElement.value;
                if (selectedValue == 4) {
                    labelElement.textContent = 'Empresa';
                } else {
                    labelElement.textContent = 'Nombres y Apellidos';
                }
            });
        }
    });

});