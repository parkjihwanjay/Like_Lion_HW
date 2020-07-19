const resultNumber1 = document.querySelector(".numberCheckingWithSpace");
const resultNumber2 = document.querySelector(".numberCheckingWithOutSpace")
const input = document.querySelector(".input");

// function numberChecking(event){
//     let inputValue1 = "";
//     let inputValue2 = "";

//     inputValue1 = event.target.value.length;
//     inputValue2 = event.target.value.split(" ").join("").length;
//     if (event.key === 'Enter'){
//         resultNumber1.textContent = inputValue1;
//         resultNumber2.textContent = inputValue2;
//     }
// }

// input.addEventListener('keydown', numberChecking);

function numberChecking(event){
    let inputValue1 = "";
    let inputValue2 = "";

    inputValue1 = event.target.value.length;
    inputValue2 = event.target.value.split(" ").join("").length;

    resultNumber1.textContent = inputValue1;
    resultNumber2.textContent = inputValue2;

}

input.addEventListener('keydown', numberChecking);