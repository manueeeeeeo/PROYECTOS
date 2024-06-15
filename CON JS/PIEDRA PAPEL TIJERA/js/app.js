//Creamos las varibles necesarias para los contadores
let userScore = 0;
let pcScore = 0;

//Obtenemos todos los elementos necesarios del Index
const userDisplay = document.getElementById("user-score");
const pcDisplay = document.getElementById("pc-score");
const scoreBoard_div = document.querySelector(".score-board");
const result_div = document.querySelector(".resultado > p");
const rock_div = document.getElementById("piedra");
const paper_div = document.getElementById("papel");
const sisor_div = document.getElementById("tijera");

//Elegimos aleatoriamente una elección para la maquina
function getComputerChoice(){
    const choices = ['r', 'p', `s`];
    const randomNumber = Math.floor(Math.random()*3);
    return choices[randomNumber];
}

/*FUNCIÓN DE LA QUE PASA CUANDO GANA EL USUARIO*/
function ganado(user, computer){
    let eleccion = "";
    let ele2 = "";
    console.log("USUARIO HA GANADO");
    userScore++;
    console.log(userScore);
    userDisplay.innerHTML = userScore;
    pcDisplay.innerText = pcScore;
    if (user=="r"){
        eleccion = "Piedra";
    }else if(user=="p"){
        eleccion = "Papel";
    }else if(user=="s"){
        eleccion = "Tijera";
    }

    if (computer=="r"){
        ele2 = "Piedra";
    }else if(computer=="p"){
        ele2 = "Papel";
    }else if(computer=="s"){
        ele2 = "Tijera";
    }

    result_div.innerHTML = "GANADO -> Jugador: " + eleccion + " / PC: " + ele2;
}

/*FUNCIÓN DE LA QUE PASA CUANDO PIERDE EL USUARIO*/
function perdido(user, computer){
    let eleccion = "";
    let ele2 = "";
    console.log("USUARIO HA PERDIDO");
    pcScore++;
    console.log(pcScore);
    pcDisplay.innerText = pcScore;
    userDisplay.innerText = userScore;
    if (user=="r"){
        eleccion = "Piedra";
    }else if(user=="p"){
        eleccion = "Papel";
    }else if(user=="s"){
        eleccion = "Tijera";
    }

    if (computer=="r"){
        ele2 = "Piedra";
    }else if(computer=="p"){
        ele2 = "Papel";
    }else if(computer=="s"){
        ele2 = "Tijera";
    }

    result_div.innerHTML = "PERDIDO -> Jugador: " + eleccion + " / PC: " + ele2;
}

/*FUNCIÓN DE LA QUE PASA CUANDO EMPATAN*/
function empatado(user, computer){
    let eleccion = "";
    let ele2 = "";
    console.log("HAN EMPATADO");
    if (user=="r"){
        eleccion = "Piedra";
    }else if(user=="p"){
        eleccion = "Papel";
    }else if(user=="s"){
        eleccion = "Tijera";
    }

    if (computer=="r"){
        ele2 = "Piedra";
    }else if(computer=="p"){
        ele2 = "Papel";
    }else if(computer=="s"){
        ele2 = "Tijera";
    }

    result_div.innerHTML = "EMPATADO -> Jugador: " + eleccion + " / PC: " + ele2;
}

/*FUNCIÓN DEL JUEGO*/
function game(userChoice){
    const computerChoice = getComputerChoice();
    console.log("user choice => " + userChoice);
    console.log("pc choice => " + computerChoice);

    switch(userChoice + computerChoice){
        case "rs":
        case "pr":
        case "sp":
            ganado(userChoice, computerChoice);
            break;
        case "sr":
        case "rp":
        case "ps":
            perdido(userChoice, computerChoice);
            break;
        case "rr":
        case "pp":
        case "ss":
            empatado(userChoice, computerChoice);
            break;
    }
}

/*LO QUE PAS AL INICIAR EL JUEGO*/
function main(){
    rock_div.addEventListener('click', function(){
        game("r");
    });

    paper_div.addEventListener('click', function(){
        game("p");
    });

    sisor_div.addEventListener('click', function(){
        game("s");
    });
}

/*INICIAMOS EL JUEGO*/
main();
