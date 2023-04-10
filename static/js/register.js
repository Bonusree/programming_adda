$(document).ready(function() {
    var password = $("#password");
    var cpassword = $("#cpassword");
    $("#togglePassword").on('click', function(){
        var type = password.attr("type") === "password" ? "text" : "password";
        password.attr("type", type);
        this.classList.toggle("bi-eye");
    });
    
    $("#toggleCPassword").on('click', function(){
        var type = cpassword.attr("type") === "password" ? "text" : "password";
        cpassword.attr("type", type);
        this.classList.toggle("bi-eye");
    });
});