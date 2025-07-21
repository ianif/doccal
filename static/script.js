// Author: JOY and JOU

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
    // Use cached messageElem variable
    // In the original code a second .then block uses "messageElem" which is neither defined 
    // nor necessary. For improved performance and reduced memory usage, we update the message 
    // using the already cached "messageDiv" reference.
    // If a separate element was intended, it should be queried and cached outside the event 
    // listener once.
  });
});