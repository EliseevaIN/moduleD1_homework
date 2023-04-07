let pid = document.querySelector("[data-id-page]").getAttribute("data-id-page");
let nid = document.querySelector(`[data-id-nav='${pid}']`);

console.log(pid);
console.log(nid);

if(pid == nid.getAttribute("data-id-nav")) {
    console.log(111);
    nid.classList.add("active");
}
