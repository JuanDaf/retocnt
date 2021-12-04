
function limitar(e, contenido, caracteres) {
            // obtenemos la tecla pulsada
  var unicode=e.keyCode? e.keyCode : e.charCode;
 
            // Permitimos las siguientes teclas:// 8 backspace
            // 46 suprimir
            // 13 enter
            // 9 tabulador
            // 37 izquierda
            // 39 derecha
            // 38 subir
            // 40 bajar
  if(unicode==8 || unicode==46 || unicode==13 || unicode==9 || unicode==37 || unicode==39 || unicode==38 || unicode==40)
                return true;
 
            // Si ha superado el limite de caracteres devolvemos false
  if(contenido.length>=caracteres)
  
   return false;
 
  return true;
}

function validarNumero(e) {
    tecla = (document.all) ? e.keyCode : e.which;
    if (tecla==8) return true; 
    patron =/[0-9]/;
    te = String.fromCharCode(tecla); 
    return patron.test(te); 
 }

