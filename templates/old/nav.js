const btns = document.querySelectorAll(".nav-btn")
const img = document.getElementById("img")
btns.forEach(function(btn){
    btn.addEventListener("click", function(e){
        const styles = e.currentTarget.classList;
        if(styles.contains("hm")){
            document.body.style.background = "#edf4fa"
            document.body.style.transition = "1s"
            img.style.left = "800px"
            img.style.width = "90px"
        }
        if(styles.contains("menu1")){
            document.body.style.background = "yellow"
            document.body.style.transition = "1s"
            img.style.left = "890px"
            img.style.width = "110px"
        }
        if(styles.contains("menu2")){
            document.body.style.background = "#12bcb2"
            document.body.style.transition = "1s"
            img.style.left = "1020px"
            img.style.width = "120px"
            
        }
        if(styles.contains("menu3")){
            document.body.style.background = "#2ebcb2"
            document.body.style.transition = "1s"
            img.style.left = "1150px"
            img.style.width = "100px"
        }
        if(styles.contains("menu4")){
            document.body.style.background = "#57c12b"
            document.body.style.transition = "1s"
            img.style.left = "1250px"
            img.style.width = "90px"
        }
    })
})