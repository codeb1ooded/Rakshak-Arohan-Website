function myFunction() {
    var x = document.getElementByClass("up");
    if (x.style.display === "none") {
        x.style.display = "block";
    } else {
        x.style.display = "none";
    }
}