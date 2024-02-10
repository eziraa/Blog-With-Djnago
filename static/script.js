function toggleContent() {
  var content = document.querySelector(".content .hidden-content");
  var btn = document.querySelector(".content .see-more-btn");

  if (content.style.display === "none" || content.style.display === "") {
    content.style.display = "inline";
    btn.textContent = "See Less";
  } else {
    content.style.display = "none";
    btn.textContent = "See More";
  }
}
