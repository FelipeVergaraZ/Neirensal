function myFunction() {
    var x = document.getElementById("myTopnav");
    if (x.className === "topnav") {
        x.className += " responsive";
    } else {
        x.className = "topnav";
    }
}

function validar() {
    var a = document.forms["myForm"]["username"].value;
    if (a == "") {
        alert("Falta llenar el Usuario,\n ");
        return false;
    }
    var b = document.forms["myForm"]["email"].value;
    if (b == "") {
        alert("Falta llenar el Email");
        return false;
    }
    var c = document.forms["myForm"]["phone"].value;
    if (c == "") {
        alert("Falta llenar el numero");
        return false;
    }
    var d = document.forms["myForm"]["message"].value;
    if (d == "") {
        alert("Falta llenar el mensaje");
        return false;
    }
    console.log(email, 'hola');
    email.send({

    })






}

function iniciarMap() {
    var coord = { lat: -32.7723101, lng: -71.5333 };
    var map = new google.maps.Map(document.getElementById('map'), {
        zoom: 10,
        center: coord
    });
    var marker = new google.maps.Marker({
        position: coord,
        map: map
    });
}

window.addEventListener('DOMContentLoaded', event => {
    const listHoursArray = document.body.querySelectorAll('.list-hours li');
    listHoursArray[new Date().getDay()].classList.add(('today'));
})




//Consumo de Propia API
$(document).ready(function() {
    //para setear los Header de la llamada a la API y otrgarle permisos
    $.ajaxSetup({
        headers: {
            'Authorization': 'Token c30623b137ba27cdfe8d56910c7430ceb0d382b1'
        }
    });
    //obtengo la info de la API
    $.getJSON("http://127.0.0.1:8000/api/lista_categoria", function(json) {
        $.each(json, function(i, item) {
            $('#propia-api').append("<tr><td>" + item.ID_CATPROD + "</td><td>" +
                item.NOM_CATPROD + "</td></tr>");
        });
    }).fail(function() {
        console.log('Error');
    });
});

//POST a la API para obtener el token 
function log(username, password) {
    console.log(username, password)
    var myHeaders = new Headers();
    myHeaders.append("Content-Type", "text/plain");

    var raw = JSON.stringify({
        "username": username,
        "password": password
    });

    var requestOptions = {
        method: 'POST',
        headers: myHeaders,
        body: raw,
        redirect: 'follow'
    };

    fetch("http://127.0.0.1:8000/api/login", requestOptions)
        .then(response => response.text())
        .then(result => { console.log(result) })
}