document.getElementById("contact-form").addEventListener("submit", function (e) {
  e.preventDefault();

  let isValid = true;

  // Get form fields
  const name = document.getElementById("name");
  const email = document.getElementById("email");
  const message = document.getElementById("message");

  // Reset errors
  document.getElementById("name-error").textContent = "";
  document.getElementById("email-error").textContent = "";
  document.getElementById("message-error").textContent = "";

  // Validate name
  if (name.value.trim() === "") {
    document.getElementById("name-error").textContent = "Name is required.";
    isValid = false;
  }

  // Validate email
  const emailPattern = /^[^ ]+@[^ ]+\.[a-z]{2,3}$/;
  if (!email.value.match(emailPattern)) {
    document.getElementById("email-error").textContent = "Enter a valid email.";
    isValid = false;
  }

  // Validate message
  if (message.value.trim().length < 10) {
    document.getElementById("message-error").textContent = "Please enter a message (10+ characters).";
    isValid = false;
  }

  // If all valid, simulate submission
  if (isValid) {
    alert("Thanks for reaching out! I'll get back to you shortly.");
    document.getElementById("contact-form").reset();
  }
});
