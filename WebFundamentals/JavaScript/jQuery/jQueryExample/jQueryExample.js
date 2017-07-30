$(document).ready(function() {
  $(".hide").hide();
  $("#addclass > a").click(function() {
    $("#addclass > p").addClass("red");
    console.log('hi');
  })
  $("#slidetoggle > a").click(function() {
    $(".putin-bro").slideToggle();
    console.log('hi');
  })
  $("#append > a").click(function() {
    $("#append").append("<p>New paragraph!</p>");
    console.log('hi');
  })
  $("#fade > a").click(function() {
    $(".fade").fadeIn();
    console.log('hi');
  })
  $("#text > a").click(function() {
    $("#text > p").text($("#fade > input").val());
    console.log('hi');
  })

  // $("a.button").click(function() {
  //   $("p.toggle").toggle();
  // })
  // $(".btn-slide").click(function() {
  //   $(".slide").show();
  //   $(".slide-down").slideDown();
  // })
  // $("p.slide").click(function() {
  //   $("p.slide").slideUp();
  // })
  // $("p.slide > span#toggle-slide").click(function() {
  //   $(".toggle-slide").slideToggle();
})