document.addEventListener("DOMContentLoaded", function () {
  var scheme = localStorage.getItem("data-md-color-scheme") || "default";
  document.body.setAttribute("data-md-color-scheme", scheme);
});