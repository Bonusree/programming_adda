document.addEventListener("DOMContentLoaded", function() {
    var togglePassword = document.querySelector("#togglePassword");
    var toggleCPassword = document.querySelector("#toggleCPassword");
    var password = document.querySelector("#password");
    var cpassword = document.querySelector("#cpassword");

    togglePassword.addEventListener("click", function(e) {
        var type = password.getAttribute("type") === "password" ? "text" : "password";
        password.setAttribute("type", type);
        this.classList.toggle("bi-eye");
    });
    
    toggleCPassword.addEventListener("click", function(e) {
        var type = cpassword.getAttribute("type") === "password" ? "text" : "password";
        cpassword.setAttribute("type", type);
        this.classList.toggle("bi-eye");
    });
});
