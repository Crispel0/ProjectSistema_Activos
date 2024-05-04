
function show_password(){
  var input_show_hide_password = document.getElementsByClassName("hide_password");
  for (i = 0 ; i <= input_show_hide_password.length ; i++) {
      if (input_show_hide_password[i].getAttribute('type') === "password"){
          input_show_hide_password[i].setAttribute("type","text")
  }    
  else {
          input_show_hide_password[i].setAttribute("type","password");
  }
  }; 
}