console.log("hello is me shmavadrift")


// ~~~~~~~~~~~~~~~ DEMO STUFF AND EXAMPLES ~~~~~~~~~~~~~~~~
function handlesClick(){
    confirm('Wow you did it')
}

function changeText(){
    var button = document.querySelector("#loginbtn")
    button.innerHTML = "Logout"
}
function removeText(){
    var button = document.querySelector(".contributionButton")
    button.remove();
}
function likeAlert(){
    var button = document.querySelector("#loginbtn")
    alert("You are logged in")
}

//this > element targeted with function(this) ex onclick="changeColor(this)"
function changeColor(element){
    // element.remove()
    element.style.backgroundColor = "black"
    element.style.color = "white"
    }

    var click = 0
function toggleMode(element){
    // TOGGLE BETWEEN LIGHT AND DARK
    var container = document.querySelector(".container")
    // FIGURE OUT IF THE CONTAINER IS CURRENTLY IN DARK MODE OR LIGHT MODE
    if(container.classList.contains("light-mode")){
        // CONTAINER IS CURRENLTY IN LIGHT MODE, CHANGE TO DARK MODE
        container.classList.remove("light-mode")
        container.classList.add("dark-mode")
    }
    else{
        container.classList.remove("dark-mode")
        container.classList.add("light-mode")
    }
    // INCREAES COUNT OF CLICK AND SHOW THE NEW NUMBER
    click++
    element.innerHTML = `Toggle Mode ${click}`
}

// ~~~~~~~~~~~START NEW STUFF HERE~~~~~~~~~~~~~~~~~