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
      // Add click event handler to all menu links
    $('.nav-link').on('click', function() {
        console.log('Clicked link:', this);
        // Remove the active class from the currently active link (if there is one)
        $('.nav-link.active').removeClass('active');
        
        // Add the active class to the clicked link
        $(this).addClass('active');
    });
});