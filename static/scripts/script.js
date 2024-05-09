console.log('Hello Worlds')

var form = document.getElementById("text-form");

var mode = document.getElementById('mode-selector');
var modeBtns = mode.getElementsByClassName('btn');

for(var i=0; i<modeBtns.length; i++) {
    modeBtns[i].addEventListener("click", function(e) {
        e.preventDefault();
        var current = document.getElementsByClassName('active');
        current[0].className = current[0].className.replace(" active", "");
        this.className += " active";

        // Check which form to show
        if(this.classList.contains("sms-b")) {
            form.action = "/smsprediction";
        } else {
            form.action = "/emailprediction";
        }
    });
}


window.onscroll = function() {myFunction()};

var navbar = document.getElementById('navbar');
var sticky = navbar.offsetTop;

function myFunction() {
    if(window.pageYOffset > sticky) {
        navbar.classList.add('sticky');
    } else {
        navbar.classList.remove('sticky');
    }
}