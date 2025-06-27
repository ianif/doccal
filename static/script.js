document.getElementById('appointment-form').addEventListener('submit', function(e) {
  e.preventDefault();

  const doctor = document.getElementById('doctor').value;
  const date = document.getElementById('date').value;
  const time = document.getElementById('time').value;

  fetch('/book', {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json'
    },
    body: JSON.stringify({ doctor, date, time })
  })
  .then(response => response.json())
  .then(data => {
    const message = document.getElementById('message');
    message.innerText = data.message;
    message.style.color = data.status === 'success' ? 'green' : 'red';
  });
});

