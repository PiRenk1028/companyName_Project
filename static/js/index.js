document.getElementById('form').addEventListener('submit', function(event) {
  event.preventDefault()

  form = event.target
  formData = new FormData(form)
  data = Object.fromEntries(formData.entries())

  fetch('/',{
    method: 'POST',
    headers: {"Content-Type": "application/json"},
    body: JSON.stringify(data)
  })
  .catch(error => {
        console.error('Error:', error);
        // Handle errors
    });

});
