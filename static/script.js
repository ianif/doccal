// Author: JOY

const appointmentForm = document.getElementById('appointment-form');
const doctorSelect = document.getElementById('doctor');
const dateSelect = document.getElementById('date');
const timeSelect = document.getElementById('time');
const messageDiv = document.getElementById('message');

appointmentForm.addEventListener('submit', function(e) {
  e.preventDefault();

  const doctor = doctorSelect.value;
  const date = dateSelect.value;
  const time = timeSelect.value;

  fetch('/book', {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json'
    },
    body: JSON.stringify({ doctor, date, time })
  })
  .then(response => response.json())
  .then(data => {
    messageDiv.textContent = data.message;
    messageDiv.style.color = data.status === 'success' ? 'green' : 'red';
  });
});
  .then(data => {
    // Use cached messageElem variable
    messageElem.innerText = data.message;
    messageElem.style.color = data.status === 'success' ? 'green' : 'red';
  });
});