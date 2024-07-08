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


// -------------------- RESTRICTING THE CHECK-IN DATES
let checkIn = document.querySelector("#check-in");
let checkOut = document.querySelector("#check-out")

if(checkIn){

    let todayDate = new Date()
    let dateForm = todayDate.getFullYear()+ "-" + ("0"+(todayDate.getMonth()+1)).slice(-2) + "-" + ("0" + todayDate.getDate()).slice(-2)    
    checkIn.min = `${dateForm.toString()}`
    // console.log(checkIn.min)

    let outDate = todayDate.getFullYear()+ "-" + ("0"+(todayDate.getMonth()+1)).slice(-2) + "-" + ("0" + (parseInt(todayDate.getDate())+1).toString()).slice(-2)
    checkOut.min = `${outDate.toString()}`
    // console.log(outDate)
}

checkOut.addEventListener("change", e=>{
    let inDate = checkIn.value
    let outDate = checkOut.value

    if(inDate>outDate){
        document.querySelector(".field-container p").style.opacity = 1;
        document.querySelector(".index-room-search").style.display = "none";
        return
    }
    if (inDate<outDate){
        document.querySelector(".field-container p").style.opacity = 0;
        document.querySelector(".index-room-search").style.display = "block"
        return
    }
})

// const radios = document.querySelector(".radios::is('selected')")
// console.log(radios)
// const radios = document.querySelectorAll(".radios")
// radios.forEach(radio => radio.addEventListener("click", e=>{
//     let attri = e.target.getAttribute("data-value")
//     console.log(attri)

// }))

// const indexButton = document.querySelector(".index-room-search")
// indexButton.addEventListener("click", e=>{

//     e.preventDefault()

//     console.log(checkIn.value)
//     let selectedRooms = document.querySelectorAll(".cat-container:has(.radios:checked)")
//     console.log(selectedRooms)

// })