let count = true;

function activBtn() {
    const burg1 = document.getElementById("burger");
    const list = document.getElementById("navList");
    if (count) {
        burg1.classList.add("open");
        list.classList.add("open");
        count = false;
    } else {
        burg1.classList.remove("open");
        list.classList.remove("open");
        count = true;
    }
}