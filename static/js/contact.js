document.getElementById("contact-form").addEventListener("submit", function (e) {
  // For debugging
  console.log("Form submission attempted");

  let isValid = true;
  const name = document.getElementById("name").value.trim();
  const email = document.getElementById("email").value.trim();
  const message = document.getElementById("message").value.trim();

  // Log form values
  console.log("Form values:", { name, email, message });

  if (!name || !email || !message) {
    isValid = false;
  }

  if (!isValid) {
    e.preventDefault(); // Only prevent submission if validation fails
    console.log("Form validation failed");
  } else {
    console.log("Form validation passed, submitting...");
  }
});
