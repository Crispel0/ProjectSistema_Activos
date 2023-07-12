
var fontSize = 1; //valor predeterminado

        /*obtiene todos las clases tag y cualquier cosa que contenga despues del la etiqueta body 
        y hace un recorrido a cada una de las etiquetas hasta que termine el archivo html y por cada elemento suma un 0.01 em*/
        function aumentar() {
            fontSize += 0.01;
            var elementosDOM = document.querySelectorAll("body *");
            for (let index = 0; index < elementosDOM.length; index++) {
               elementosDOM[index].style.fontSize = fontSize + "em" ;
            }
            
        }

        /*obtiene todos las clases tag y cualquier cosa que contenga despues del la etiqueta body 
        y hace un recorrido a cada una de las etiquetas hasta que termine el archivo html y por cada elemento resta un 0.01 em*/
         function disminuir() {
            fontSize -= 0.01;
            var  elementosDOM = document.querySelectorAll("body *");
            for(let index = 0; index < elementosDOM.length; index++) {
                elementosDOM[index].style.fontSize = fontSize + "em";
            }
        }