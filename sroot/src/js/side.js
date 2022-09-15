const liBtn = document.querySelectorAll('.li-btn')
const linkCont = document.querySelectorAll('.links-container')
const miniLinksCont = document.querySelectorAll('.drop-lists')
const dropDnBtn = document.querySelectorAll('.drop-down-icon')
const infoDropCont = document.querySelector('.info-drop-container')
const infoUl = document.querySelector('.info-drop-ul')
const threeDotsBtn = document.querySelector('.three-dots')
const timeEl = document.getElementById('time')
const ulCont = document.querySelector('.ul-container')
const today = new Date()
// let time = today.getHours() + ':' + today.getMinutes() + ':' + today.getSeconds()

function time() {
    t1 = new Date()
    let hrs = t1.getHours()
    let min = t1.getMinutes()
    let sec = t1.getSeconds()
    if (hrs > 12) {
        hrs -= 12
    }

    timeEl.innerHTML = hrs + ":" + min + ":" + sec

    if (hrs < 10) {
        timeEl.innerHTML = "0" + hrs + ":" + min + ":" + sec
    }
    if (min < 10) {
        timeEl.innerHTML = hrs + ":" + "0" + min + ":" + sec
    }
    if (sec < 10) {
        timeEl.innerHTML = hrs + ":" + min + ":" + "0" + sec
    }

    if (hrs < 10 && min < 10) {
        timeEl.innerHTML = "0" + hrs + ":" + "0" + min + ":" + sec
    }
    if (hrs < 10 && sec < 10) {
        timeEl.innerHTML = "0" + hrs + ":" + min + ":" + "0" + sec
    }
    if (min < 10 && sec < 10) {
        timeEl.innerHTML = hrs + ":" + "0" + min + ":" + "0" + sec
    }
    if (hrs < 10 && min < 10 && sec < 10) {
        timeEl.innerHTML = "0" + hrs + ":" + "0" + min + ":" + "0" + sec
    }
}
setInterval(time, 1000)

threeDotsBtn.addEventListener('click', function () {
    const infoContHeight = infoDropCont.getBoundingClientRect().height
    const infoUlHeight = infoUl.getBoundingClientRect().height
    console.log(infoUlHeight)
    if (infoContHeight == 0) {
        infoDropCont.style.height = `140px`
        infoDropCont.style.display = 'block'
    }
    else {
        infoDropCont.style.height = '0px'
        infoDropCont.style.display = 'none'
    }
})

liBtn.forEach(function (btn) {
    btn.addEventListener('click', function (e) {
        const styles = e.currentTarget.classList
        linkCont.forEach(function (cont) {
            cont.style.height = '0'
        })
        dropDnBtn.forEach(function (bbtn) {
            bbtn.style.transform = 'rotate(0deg)'
        })
        if (styles.contains('crs')) {
            if (linkCont[0].getBoundingClientRect().height === 0) {
                linkCont[0].style.height = `${miniLinksCont[0].getBoundingClientRect().height}px`
                dropDnBtn[0].style.transform = 'rotate(180deg)'
            }
            else {
                linkCont[0].style.height = '0'
                dropDnBtn[0].style.transform = 'rotate(0deg)'
            }

        }
        if (styles.contains('adm')) {
            if (linkCont[1].getBoundingClientRect().height === 0) {
                linkCont[1].style.height = `${miniLinksCont[1].getBoundingClientRect().height}px`
                dropDnBtn[1].style.transform = 'rotate(180deg)'
            }
            else {
                linkCont[1].style.height = '0'
                dropDnBtn[1].style.transform = 'rotate(0deg)'
            }

        }
        if (styles.contains('acad')) {
            if (linkCont[2].getBoundingClientRect().height === 0) {
                linkCont[2].style.height = `${miniLinksCont[2].getBoundingClientRect().height}px`
                dropDnBtn[2].style.transform = 'rotate(180deg)'
            }
            else {
                linkCont[2].style.height = '0'
                dropDnBtn[2].style.transform = 'rotate(0deg)'
            }

        }
        if (styles.contains('frm')) {
            if (linkCont[3].getBoundingClientRect().height === 0) {
                linkCont[3].style.height = `${miniLinksCont[3].getBoundingClientRect().height}px`
                dropDnBtn[3].style.transform = 'rotate(180deg)'
            }
            else {
                linkCont[3].style.height = '0'
                dropDnBtn[3].style.transform = 'rotate(0deg)'
            }

        }
        if (styles.contains('wdl')) {
            if (linkCont[4].getBoundingClientRect().height === 0) {
                linkCont[4].style.height = `${miniLinksCont[4].getBoundingClientRect().height}px`
                dropDnBtn[4].style.transform = 'rotate(180deg)'
            }
            else {
                linkCont[4].style.height = '0'
                dropDnBtn[4].style.transform = 'rotate(0deg)'
            }
        }

        if (styles.contains('my-profile')) {
            if (linkCont[5].getBoundingClientRect().height === 0) {
                linkCont[5].style.height = `${miniLinksCont[5].getBoundingClientRect().height}px`
                dropDnBtn[5].style.transform = 'rotate(180deg)'
            }
            else {
                linkCont[5].style.height = '0'
                dropDnBtn[5].style.transform = 'rotate(0deg)'
            }

        }
    })
})
function showMenu() {
    ulCont.style.width = '250px'
}
function hideMenu() {
    ulCont.style.width = '0'
}

// Graph Javascript starts here

$(function () {
    $('.chart').easyPieChart({
        size: 160,
        barColor: "rgb(155, 0, 198)",
        scaleLength: 0,
        lineWidth: 15,
        trackColor: "#373737",
        lineCap: "circle",
        animate: 2000,
    });
});

// Graph Javascript code ends here