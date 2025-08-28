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
  .then(response => response.json())
    .then(result => {
        document.getElementById("Output").innerHTML = `Name: ${result['First Name']} ${result['Last Name']}
        Amount: $${result['Loan']}`;
      })
  .catch(error => {
          console.error('Error:', error);
        // Handle errors
    });

});
