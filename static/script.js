function toggleContent(button) {
  var content = button.previousElementSibling;
  var hiddenContent = content.querySelector(".hidden-content");

  if (content.style.display === "none" || content.style.display === "") {
    content.style.display = "inline";
    button.textContent = "See Less";
  } else {
    content.style.display = "none";
    button.textContent = "See More";
  }
}
