function input_Text(){
    document.getElementById("input1").value = "클라우드";
    document.getElementById("input2").value = "클라우드 보안";
}

function newClickEvent(){
    document.getElementById("loading-image").hidden = null;
    // document.getElementById("welcome-image").hidden = true;
    document.getElementById("rightDiv").style = "display:none";
    document.getElementsByClassName("right").style = "display:none";
}

function zoomIn(event) {
    event.target.style.zIndex = 1;
    event.target.style.transform = "scale(2.5)";
    event.target.style.transition = "all 0.3s";
}

function zoomOut(event) {
    event.target.style.zIndex = 0;
    event.target.style.transform = "scale(1)";
    event.target.style.transition = "all 0.2s";
}
