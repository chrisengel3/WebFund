//EVENT DRIVEN / INPUT DRIVEN

console.log("hello is me shmavadrift")

function handlesClick(){
    confirm('Wow you did it')
}

//DOCUMENT always references HTML doc in JS
function changeText(){
    var button = document.querySelector("#loginbtn")
    button.innerHTML = "Logout"
}
function removeText(){
    var button = document.querySelector(".contributionButton")
    button.remove();
}
function likeAlert(){
    var button = document.querySelector(".likeButton")
    alert("Ninja has been liked!")
}