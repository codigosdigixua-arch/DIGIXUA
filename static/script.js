/*=====================================================
DIGIXUA v2.0
=====================================================*/


//==============================================
// ESPERAR A QUE CARGUE LA PÁGINA
//==============================================

document.addEventListener("DOMContentLoaded", function () {

    //------------------------------------------
    // FORMULARIO
    //------------------------------------------

    const formulario = document.getElementById("formBuscar");

    const botonBuscar = document.getElementById("btnBuscar");

    if (formulario && botonBuscar) {

        formulario.addEventListener("submit", function () {

            botonBuscar.disabled = true;

            botonBuscar.innerHTML =
                "⏳ BUSCANDO...";

        });

    }


    //------------------------------------------
    // EFECTO INPUT
    //------------------------------------------

    const input = document.getElementById("correo");

    if (input) {

        input.addEventListener("focus", function () {

            input.style.transform = "scale(1.01)";

        });

        input.addEventListener("blur", function () {

            input.style.transform = "scale(1)";

        });

    }


    //------------------------------------------
    // APARICIÓN TARJETA
    //------------------------------------------

    const tarjeta = document.querySelector(".tarjeta");

    if (tarjeta) {

        tarjeta.style.opacity = "0";

        tarjeta.style.transform = "translateY(30px)";

        setTimeout(function () {

            tarjeta.style.transition =
                "all .45s ease";

            tarjeta.style.opacity = "1";

            tarjeta.style.transform =
                "translateY(0px)";

        }, 120);

    }


    //------------------------------------------
    // MENSAJE
    //------------------------------------------

    const mensaje = document.querySelector(".mensaje");

    if (mensaje) {

        mensaje.style.opacity = "0";

        setTimeout(function () {

            mensaje.style.transition =
                ".45s";

            mensaje.style.opacity = "1";

        }, 100);

    }

});



//==============================================
// COPIAR CÓDIGO
//==============================================

function copiarCodigo() {

    const codigo =
        document.getElementById("codigo");

    if (!codigo) {

        return;

    }

    navigator.clipboard.writeText(

        codigo.innerText.trim()

    );

    const boton =
        document.getElementById("btnCopiar");

    if (!boton) {

        return;

    }

    boton.innerHTML =
        "✅ COPIADO";

    boton.style.background =
        "linear-gradient(135deg,#00D26A,#00E676)";

    boton.style.transform =
        "scale(.97)";

    setTimeout(function () {

        boton.innerHTML =
            "📋 COPIAR CÓDIGO";

        boton.style.background =
            "";

        boton.style.transform =
            "scale(1)";

    }, 1800);

}



//==============================================
// LOGO PRINCIPAL
//==============================================

const logo =
    document.querySelector(".logo-principal");

if (logo) {

    logo.addEventListener("mouseenter", function () {

        logo.style.transition =
            ".35s";

        logo.style.transform =
            "scale(1.05) rotate(2deg)";

    });

    logo.addEventListener("mouseleave", function () {

        logo.style.transform =
            "scale(1) rotate(0deg)";

    });

}



//==============================================
// EFECTO BOTONES
//==============================================

const botones =
    document.querySelectorAll("button,.boton");

botones.forEach(function (boton) {

    boton.addEventListener("mouseenter", function () {

        boton.style.transition =
            ".25s";

        boton.style.transform =
            "translateY(-3px)";

    });

    boton.addEventListener("mouseleave", function () {

        boton.style.transform =
            "translateY(0px)";

    });

});



//==============================================
// SCROLL SUAVE
//==============================================

window.scrollTo({

    top: 0,

    behavior: "smooth"

});