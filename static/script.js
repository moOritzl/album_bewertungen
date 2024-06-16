// script.js

document.addEventListener('DOMContentLoaded', function () {
    // Get the modal
    var modal = document.getElementById("login-modal");

    // Get the button that opens the modal
    var btn = document.getElementById("login-btn");

    // Get the <span> element that closes the modal
    var span = document.getElementsByClassName("close-btn")[0];

    // Function to show the login modal
    function showLoginModal() {
        modal.style.display = "block";
    }

    // When the user clicks on <span> (x), close the modal
    span.onclick = function () {
        modal.style.display = "none";
    }

    // When the user clicks anywhere outside of the modal, close it
    window.onclick = function (event) {
        if (event.target == modal) {
            modal.style.display = "none";
        }
    }

    // Expose the showLoginModal function to the global scope
    window.showLoginModal = showLoginModal;
});
