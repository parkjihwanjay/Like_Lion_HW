const divs = document.querySelectorAll("div")

const yellow = "yellow";
const blue = "blue";
const white = "white";

function clickMouse(event){
    event.target.style.background = blue;
    if (event.target.parentElement.nodeName !== "BODY"){
        event.target.parentElement.style.background = yellow;
        console.log("check")
    }
}

function mouseOut(){
    this.style.background = white;
}
divs.forEach(divElement=>{
    divElement.addEventListener('click', clickMouse)
});
divs.forEach(divElement =>{
    divElement.addEventListener('mouseout', mouseOut)
});




console.log("on!")