// ------ CARAOUSEL SLIDER ---------

const leftSlider = document.querySelector(".left-slider");
const rightSlider = document.querySelector(".right-slider");
const caroPics = document.querySelectorAll(".caro-pic")
const imageContainer = document.querySelector(".carousel-container")
let count = 0;

leftSlider.addEventListener("click", e=>{

    let currentImage = caroPics[count]
    imageContainer.scrollBy(-currentImage.offsetWidth,0)
    count--
    // console.log(count)
    if (count === 0){
        leftSlider.style.display = "none"
    }

    if(rightSlider.style.display!=="initial"){
        rightSlider.style.display = "initial"
    }

})

rightSlider.addEventListener("click", e=>{

    let currentImage = caroPics[count]
    // console.log(currentImage)
    imageContainer.scrollBy(currentImage.offsetWidth,0)
    count++
    // console.log(count)
    if (count === 6){
        rightSlider.style.display = "none"
    }

    if(leftSlider.style.display!=="initial"){
        leftSlider.style.display = "initial"
    }

})