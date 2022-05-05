//Prendre un número aleatori entre 1 i 20, i demanar amb una notificació a l’usuari que l’endevini.
//Aquest exercici és per treballar condicionals, funcions matemàtiques, 
//i funcions d’interacció amb el navegador i usuari (prompt, console.log)

//DOM EXERCICI 3//

boton = document.getElementById("1")
boton.addEventListener("click", myScript); 

function myScript(){
  parrafos = document.getElementsByTagName("p");
  for(let x=0; x<parrafos.length; x++){
  console.log(parrafos[x]);
    parrafos[x].style.backgroundColor = "green";
  }
}