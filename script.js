document.addEventListener("DOMContentLoaded", function() {
    const form = document.querySelector('form');

    form.addEventListener('submit', function(event) {
        event.preventDefault(); // Prevent default form submission behavior

        // Validate all fields
        const name = document.getElementById('name').value.trim();
        const phone = document.getElementById('phone').value.trim();
        const email = document.getElementById('email').value.trim();
        const issue = document.getElementById('issue').value.trim();

        // Check if all fields are filled
        if (name === '' || phone === '' || email === '' || issue === '') {
            alert('Please fill in all fields.');
            return;
        }

        // Validate email format
        const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
        if (!emailRegex.test(email)) {
            alert('Please enter a valid email address.');
            return;
        }

        // Redirect to another webpage
        window.location.href = 'result.html'; // Replace '#' with the URL of the other webpage
    });
});
