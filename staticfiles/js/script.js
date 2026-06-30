const swiper = new Swiper(".heroSwiper", {

    loop:true,

    speed:1000,

    autoplay:{

        delay:4000,

        disableOnInteraction:false,

    },

    pagination:{

        el:".swiper-pagination",

        clickable:true,

    },

    navigation:{

        nextEl:".swiper-button-next",

        prevEl:".swiper-button-prev",

    },

});