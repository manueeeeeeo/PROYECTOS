document.addEventListener('DOMContentLoaded', function(){
    /*Declaramos las variables*/
    const dividir = document.getElementById('dividir');
    const sumar = document.getElementById('sumar');
    const restar = document.getElementById('restar');
    const multi = document.getElementById('multiplicar');
    const uno = document.getElementById('uno');
    const dos = document.getElementById('dos');
    const tres = document.getElementById('tres');
    const cuatro = document.getElementById('cuatro');
    const cinco = document.getElementById('cinco');
    const seis = document.getElementById('seis');
    const siete = document.getElementById('siete');
    const ocho = document.getElementById('ocho');
    const nueve = document.getElementById('nueve');
    const cero = document.getElementById('cero');
    const borrar = document.getElementById('borrar');
    const igual = document.getElementById('obtener');
    const punto = document.getElementById('punto');
    const resultado = document.getElementById('resultado');
    let cadena = '';

    /*Introducimos lo que pasa cuando clicamos sobre borrar*/
    borrar.addEventListener('click', function(){
        cadena = '';
        resultado.value = '';
    });

    /*Añadimos el caracter de 1 al input*/
    uno.addEventListener('click', function(){
        cadena += '1';
        resultado.value = cadena;
    });

    /*Añadimos el caracter de 2 al input*/
    dos.addEventListener('click', function(){
        cadena += '2';
        resultado.value = cadena;
    });

    /*Añadimos el caracter de 3 al input*/
    tres.addEventListener('click', function(){
        cadena += '3';
        resultado.value = cadena;
    });

    /*Añadimos el caracter de 4 al input*/
    cuatro.addEventListener('click', function(){
        cadena += '4';
        resultado.value = cadena;
    });

    /*Añadimos el caracter de 5 al input*/
    cinco.addEventListener('click', function(){
        cadena += '5';
        resultado.value = cadena;
    });

    /*Añadimos el caracter de 6 al input*/
    seis.addEventListener('click', function(){
        cadena += '6';
        resultado.value = cadena;
    });

    /*Añadimos el caracter de 7 al input*/
    siete.addEventListener('click', function(){
        cadena += '7';
        resultado.value = cadena;
    });

    /*Añadimos el caracter de 8 al input*/
    ocho.addEventListener('click', function(){
        cadena += '8';
        resultado.value = cadena;
    });

    /*Añadimos el caracter de 9 al input*/
    nueve.addEventListener('click', function(){
        cadena += '9';
        resultado.value = cadena;
    });

    /*Añadimos el caracter de 0 al input*/
    cero.addEventListener('click', function(){
        cadena += '0';
        resultado.value = cadena;
    });

    /*Añadimos el caracter de punto/coma al input*/
    punto.addEventListener('click', function(){
        cadena += '.';
        resultado.value = cadena;
    });

    /*Añadimos el caracter de dividir al input*/
    dividir.addEventListener('click', function(){
        cadena += '/';
        resultado.value = cadena;
    });

    /*Añadimos el caracter de sumar al input*/
    sumar.addEventListener('click', function(){
        cadena += '+';
        resultado.value = cadena;
    });

    /*Añadimos el caracter de restar al input*/
    restar.addEventListener('click', function(){
        cadena += '-';
        resultado.value = cadena;
    });

    /*Añadimos el caracter de multiplicar al input*/
    multi.addEventListener('click', function(){
        cadena += '*';
        resultado.value = cadena;
    });

    /*Cuando clicamos al igual, utilizamos las función eval para calcular el resultado y mostrarle por pantalla*/
    igual.addEventListener('click', function(){
        resultado.value = eval(cadena);
    });
});
