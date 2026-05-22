var scheme = localStorage.getItem("data-md-color-scheme");
if (scheme) {
  document.documentElement.setAttribute("data-md-color-scheme", scheme);
}