// Get references to HTML elements
const uploadForm = document.getElementById("upload-form");
const fileUploadInput = document.getElementById("file-upload");
const resultSection = document.getElementById("result");
const generatedImage = document.getElementById("generated-image");
const downloadLink = document.getElementById("download-link");

// Handle form submission
uploadForm.addEventListener("submit", async e => {
  e.preventDefault();

  // Get the selected file
  const file = fileUploadInput.files[0];

  if (file) {
    // Create a FormData object to send the file
    const formData = new FormData();
    formData.append("file", file);

    // Send the file to the server for processing
    try {
      const response = await fetch("/process", {
        method: "POST",
        body: formData,
      });

      if (response.ok) {
        // Display the generated image and download link
        const imageUrl = await response.text();
        generatedImage.src = imageUrl;
        downloadLink.href = imageUrl;
        resultSection.style.display = "block";
      } else {
        console.error("Error processing file:", response.statusText);
      }
    } catch (error) {
      console.error("Error processing file:", error);
    }
  }
});
