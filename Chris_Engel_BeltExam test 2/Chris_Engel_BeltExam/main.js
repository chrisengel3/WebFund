
function emptyCart(){
    alert("Your Cart is empty!")
}

function hoverPictureChanger(){
    var image = document.querySelector("#succulents1")
    image.src = "images/assets/succulents-2.jpg"
}
function hoverPictureChangerOFF(){
    var image = document.querySelector("#succulents1")
    image.src = "images/assets/succulents-1.jpg"
}
function cookieAccept(){
    var cookies = document.querySelector("#cookiePopup")
    cookies.remove()
}