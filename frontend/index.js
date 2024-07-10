document.addEventListener('DOMContentLoaded', function() {
    const form = document.getElementById('myForm');
    const fileInput = document.getElementById('upload');
    const submitButton = document.getElementById('submit-btn');
    const errorMessage = document.getElementById('error-message');
    
    form.addEventListener('submit', function(event) {
      if (fileInput.files.length === 0) {
        event.preventDefault();
        
        errorMessage.textContent = alert("Please Select the field");
        errorMessage.style.display = 'block';
      } else {
        errorMessage.textContent = '';
        errorMessage.style.display = 'none';
      }
    });
    fileInput.addEventListener('change', function() {
      const fileName = fileInput.files[0].name;
      document.getElementById('file-name').textContent = `Selected File: ${fileName}`;
    });
  });
  