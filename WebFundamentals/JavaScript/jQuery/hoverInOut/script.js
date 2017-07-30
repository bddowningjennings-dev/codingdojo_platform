$(document).ready(function() {
  $('.hidden').toggle();
  $('img').hover(function() {
    $(this).attr("src", "putin2.png");
  },
    function() {
    $(this).attr("src", "putin.png");
    })
  })
