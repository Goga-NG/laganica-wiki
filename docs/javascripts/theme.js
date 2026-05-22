var scheme = localStorage.getItem("data-md-color-scheme");
if (scheme) {
  document.documentElement.setAttribute("data-md-color-scheme", scheme);
}

var btn = document.createElement("button");
btn.className = "go-to-bottom";
btn.innerHTML = "↓";
btn.onclick = function() {
  window.scrollTo({ top: document.body.scrollHeight, behavior: "smooth" });
};
document.body.appendChild(btn);