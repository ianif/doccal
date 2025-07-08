const appointmentForm = document.getElementById('appointment-form');
const doctorSelect = document.getElementById('doctor');
const dateSelect = document.getElementById('date');
const timeSelect = document.getElementById('time');
const messageDiv = document.getElementById('message');

appointmentForm.addEventListener('submit', function(e) {
  e.preventDefault();

  const formData = {
    doctor: doctorSelect.value,
    date: dateSelect.value,
    time: timeSelect.value
  };

  fetch('/book', {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json'
    },
    body: JSON.stringify(formData)
  })
  .then(response => response.json())
  .then(data => {
    messageDiv.textContent = data.message;
    messageDiv.style.color = data.status === 'success' ? 'green' : 'red';
  });
});