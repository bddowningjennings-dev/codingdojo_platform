$(document).ready(function() {
  $('.hidden').hide();
  $('img').click(function() {
    var name = $(this).attr('class');
    $('img[class$='+name[name.length-1]+"]").toggle();
  })
})