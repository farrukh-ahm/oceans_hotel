// ------ CARAOUSEL SLIDER ---------

const leftSlider = document.querySelector(".left-slider");
const rightSlider = document.querySelector(".right-slider");
const caroPics = document.querySelectorAll(".caro-pic")
const imageContainer = document.querySelector(".carousel-container")
let count = 0;

if(leftSlider){

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

}

if(rightSlider){

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

}

// -------------------- SERVICES ANIMATION

const services = document.querySelectorAll(".services");

const servicesAppearAnimation = new IntersectionObserver(entries=>{

    entries.forEach(entry=>{

        entry.target.classList.toggle("services-appear", entry.isIntersecting)

        if(entry.isIntersecting){
            servicesAppearAnimation.unobserve(entry.target)
        }

    })

},
{
    threshold: 1
})

services.forEach(service=>{
    servicesAppearAnimation.observe(service)
});


// -------------------- LOCATION CARD ROTATION AND ANIMATION
let locationCard = document.querySelectorAll(".perspective-box");
let locationFront = document.querySelectorAll(".loc-card")
let locationBack = document.querySelectorAll(".loc-detail")
let locationWrapper = document.querySelectorAll(".location-wrapper")

if(locationCard){

    const perspectiveAnimation = new IntersectionObserver(entries=>{
    
        entries.forEach(entry=>{
            // entry.target.style.transform = "translateX(0)"
            // entry.target.style.opacity = "1"
            entry.target.classList.toggle("perspective-box-appear", entry.isIntersecting)
            
            if(entry.isIntersecting){
                perspectiveAnimation.unobserve(entry.target)
            }
        })
    
    
    },
    {
        threshold: 0.5
    })

    locationWrapper.forEach(location=>{

        perspectiveAnimation.observe(location)
    })

    
    locationCard.forEach(card => {
        card.addEventListener("click", ()=>{
            card.classList.toggle("rotate")
        })
    })

}



// -------------------- RESTRICTING THE CHECK-IN DATES
// let checkIn = document.querySelector("#check-in");
// let checkOut = document.querySelector("#check-out")
let checkIn = document.querySelector("[data-validation='check-in-validation']");
let checkOut = document.querySelector("[data-validation='check-out-validation']")

if(checkIn){

    let todayDate = new Date()
    let dateForm = todayDate.getFullYear()+ "-" + ("0"+(todayDate.getMonth()+1)).slice(-2) + "-" + ("0" + todayDate.getDate()).slice(-2)    
    checkIn.min = `${dateForm.toString()}`
    // console.log(checkIn.min)

    let outDate = todayDate.getFullYear()+ "-" + ("0"+(todayDate.getMonth()+1)).slice(-2) + "-" + ("0" + (parseInt(todayDate.getDate())+1).toString()).slice(-2)
    checkOut.min = `${outDate.toString()}`
    // console.log(outDate)
}

if(checkOut){

    checkOut.addEventListener("change", e=>{
        let inDate = checkIn.value
        let outDate = checkOut.value
    
        if(inDate>outDate){
            document.querySelector(".date-field-container p").style.opacity = 1;
            document.querySelector(".index-room-search").style.display = "none";
            return
        }
        if (inDate<outDate){
            document.querySelector(".date-field-container p").style.opacity = 0;
            document.querySelector(".index-room-search").style.display = "block"
            return
        }
    })

    checkIn.addEventListener("change", e=>{
        let inDate = checkIn.value
        let outDate = checkOut.value
    
        if(inDate>outDate){
            document.querySelector(".date-field-container p").style.opacity = 1;
            document.querySelector(".index-room-search").style.display = "none";
            return
        }
        if (inDate<outDate){
            document.querySelector(".date-field-container p").style.opacity = 0;
            document.querySelector(".index-room-search").style.display = "block"
            return
        }
    })

}


// -------------------- ENSURING ONLY ONE ROOM CATEGORY SELECTION
const rooms = document.querySelectorAll(".radios")

rooms.forEach(room => room.addEventListener("change", e=>{

    if(e.target.checked){
        rooms.forEach(room =>{
            if(!room.checked){
                room.disabled = true
            }
        })
    }

    else{
        rooms.forEach(room =>{
            if(!room.checked){
                room.disabled = false
            }
        })
    }

}))


// -------------------- BOOKING ELEMENTS ANIMATION
const dateField = document.querySelectorAll(".date-field-container");
const catField = document.querySelectorAll(".cat-container");

if(dateField && catField){

    let bookingAnime = new IntersectionObserver(entries=>{
        entries.forEach(entry=>{
            entry.target.classList.toggle("booking-section-appear", entry.isIntersecting)

            if(entry.isIntersecting){
                bookingAnime.unobserve(entry.target)
            }
        })
    }, {
        threshold: 0.5
    })

    dateField.forEach(date=>{
        bookingAnime.observe(date)
    })

    catField.forEach(cat=>{
        bookingAnime.observe(cat)
    })
}


// -------------------- BOOKING PAGE ELEMENTS

// let checkDates = document.querySelectorAll(".date-picker input");
let dateChange = document.querySelectorAll(".date-modal-trigger");
let dateModal = document.querySelector(".booking-modal");
let dateModalClose = document.querySelector(".date-modal-close");

// if(checkDates){
//     checkDates.forEach(date => {
//         date.style.color = "rgb(128, 70, 27)"
//     })
// }

if (dateChange){

    dateChange.forEach(date => {
        date.addEventListener("click", ()=>{
            dateModal.showModal()

        })

    })

}

if(dateModalClose){
    dateModalClose.addEventListener("click", (e)=>{
        e.preventDefault()
        dateModal.close();

    })
}


// -------------------- BOOKING DISPLAY ON PROFILE
const bookingToggle = document.querySelector(".test-it")
const toggleButton = document.querySelector(".toggle-bookings")
const roomContainer = document.querySelectorAll(".room-container")
const detailDisplay = document.querySelectorAll(".detail")
const detailTab = document.querySelectorAll(".profile-book-detail")

if(roomContainer){
    let translate = 1
    roomContainer.forEach(room => {
        room.style.transform = `translateY(-${translate*150}%)`
        room.style.zIndex = `-${translate}`
        translate++
    })
}

if(toggleButton){
    toggleButton.addEventListener("click", ()=>{
        // bookingToggle.classList.toggle("room-sections-positions")
        // bookingToggle.classList.toggle("room-sections-flex")
        roomContainer.forEach(room => {
            room.classList.toggle("room-container-appear")
        })
    })

if(detailDisplay){

    detailDisplay.forEach(detail => {
        
        detail.addEventListener("click", (e)=>{

            let bookID = detail.getAttribute("data-id")
            let sectionExpand = document.querySelector(`section[data-id='${bookID}']`)
            let sectionDetail = document.querySelector(`div[data-id='${bookID}']`)
            console.log(sectionExpand)
            sectionExpand.classList.toggle("section-expand")
            sectionDetail.classList.toggle("section-detail-transform")

        })

    })
}

}


// let locationCard = document.querySelectorAll(".perspective-box");

// locationCard.forEach(card => {
//     card.addEventListener("click", ()=>{
//         card.classList.toggle("rotate")
//     })
// })

// -------------------- CANCEL MODAL
let cancelModalTrigger = document.querySelectorAll(".cancel-book-btn")
let cancelModal = document.querySelector(".cancel-book-modal")
let closeCancelModal = document.querySelector(".close-cancel-modal")

if(cancelModalTrigger){

    cancelModalTrigger.forEach(trigger => {
        trigger.addEventListener("click", e=>{
            let bookingId = trigger.getAttribute("data-booking")
            let cancel_form = document.querySelector("#cancel-form")
            cancel_form.setAttribute("action", `/cancelbooking/${bookingId}`)
            cancelModal.showModal()
        })
    })

}

if(closeCancelModal){
    closeCancelModal.addEventListener("click", ()=>{
        cancelModal.close()
    })
}