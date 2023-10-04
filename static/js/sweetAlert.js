
const boton = document.querySelector("btn btn-success")

boton.addEventListener("click",  prevenirEvent() )
  function prevenirEvent(e) {
    e.preventDefault()
}

async function showSweetAlert(accion, url) {
 let title, text, icon;

  if (accion === 'editar') {
    title = 'Editar';
    text = 'Quieres Editarlo?';
    icon = 'question';
  } else if (accion === 'eliminar') {
    title = 'Eliminar';
    text = 'Quieres Eliminarlo?';
    icon = 'warning';
  }
  else {
    title = 'Agregar';
    text = 'Deseas Agregarlo';
    icon = 'question';
  }

  const result = await Swal.fire({
    title: title,
    text: text,
    icon: icon,
    showCancelButton: true,
    confirmButtonText: 'Yes',
    cancelButtonText: 'No'
});

if (result.isConfirmed) {

  window.location.href = url;

}
}







