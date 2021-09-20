function burgBtn() {
    const burger1 = document.getElementById("burger1");
    const burger2 = document.getElementById("burger2");
    const burger3 = document.getElementById("burger3");
    const list = document.getElementById("navList");
    
    burger1.classList.toggle("open");
    burger2.classList.toggle("open");
    burger3.classList.toggle("open");
    list.classList.toggle("open");
}

console.log("test!");