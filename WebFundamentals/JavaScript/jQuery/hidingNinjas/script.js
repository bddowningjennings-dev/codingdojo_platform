$(document).ready(function() {
  $("img").click(function() {
    $(this).hide();
  })
  $("a.btn").click(function() {
    $("img").show();
  })
})