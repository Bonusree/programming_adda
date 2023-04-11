$(document).ready(function() {
  // Add click event handler to all menu links
  $('.nav-link').on('click', function() {
    console.log('Clicked link:', this);
    // Remove the active class from the currently active link (if there is one)
    $('.nav-link.active').removeClass('active');
    
    // Add the active class to the clicked link
    $(this).addClass('active');
  });
});
