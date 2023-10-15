
const checkbox_tarjeta = document.getElementById("id_tarjeta_madre_no_aplica");
const checkbox_fuente_poder = document.getElementById("id_fuente_poder_no_aplica");
const checkbox_procesador = document.getElementById("id_procesador_no_aplica");
const checkbox_disco_duro_1 = document.getElementById("id_disco_duro_1_no_aplica");
const checkbox_disco_duro_2 = document.getElementById("id_disco_duro_2_no_aplica");
const checkbox_ram_slot_1 = document.getElementById("id_ram_slot_1_no_aplica");
const checkbox_ram_slot_2 = document.getElementById("id_ram_slot_2_no_aplica");
const checkbox_tarjeta_video = document.getElementById("id_tarjeta_video_no_aplica");
const checkbox_monitor = document.getElementById("id_monitor_no_aplica");
const checkbox_mouse = document.getElementById("id_mouse_no_aplica");
const checkbox_teclado = document.getElementById("id_teclado_no_aplica");
const tarjeta_madre = document.getElementsByClassName("tarjeta_madre");
const fuente_poder = document.getElementsByClassName("fuente_poder");
const procesador = document.getElementsByClassName("procesador");
const disco_duro_1 = document.getElementsByClassName("disco_duro_1");
const disco_duro_2 = document.getElementsByClassName("disco_duro_2");
const ram_slot_1 = document.getElementsByClassName("ram_slot_1");
const ram_slot_2 = document.getElementsByClassName("ram_slot_2");
const tarjeta_video = document.getElementsByClassName("tarjeta_video");
const monitor = document.getElementsByClassName("monitor");
const mouse = document.getElementsByClassName("mouse");
const teclado = document.getElementsByClassName("teclado");

function getEventListenerForCheckbox(checkboxElement, elements) {
    return () => {
        const isDisabled = checkboxElement.checked;
        for (const element of elements) {
            if (isDisabled) {
                element.setAttribute("disabled", "disabled");
            } else {
                element.disabled = isDisabled;
            }
        }
    };
}

checkbox_tarjeta.addEventListener("click", getEventListenerForCheckbox(checkbox_tarjeta, tarjeta_madre));
checkbox_fuente_poder.addEventListener("click", getEventListenerForCheckbox(checkbox_fuente_poder, fuente_poder));
checkbox_procesador.addEventListener("click", getEventListenerForCheckbox(checkbox_procesador, procesador));
checkbox_disco_duro_1.addEventListener("click", getEventListenerForCheckbox(checkbox_disco_duro_1, disco_duro_1));
checkbox_disco_duro_2.addEventListener("click", getEventListenerForCheckbox(checkbox_disco_duro_2, disco_duro_2));
checkbox_ram_slot_1.addEventListener("click", getEventListenerForCheckbox(checkbox_ram_slot_1, ram_slot_1));
checkbox_ram_slot_2.addEventListener("click", getEventListenerForCheckbox(checkbox_ram_slot_2, ram_slot_2));
checkbox_tarjeta_video.addEventListener("click", getEventListenerForCheckbox(checkbox_tarjeta_video, tarjeta_video));
checkbox_monitor.addEventListener("click", getEventListenerForCheckbox(checkbox_monitor, monitor));
checkbox_mouse.addEventListener("click", getEventListenerForCheckbox(checkbox_mouse, mouse));
checkbox_teclado.addEventListener("click", getEventListenerForCheckbox(checkbox_teclado, teclado));
