$(document).ready(function() {
  $("form").submit(function( event ) {
  event.preventDefault();
  $("tbody").append(
    "<tr><td>"+$("#first-name").val()+
    "<td>"+$("#last-name").val()+
    "<td>"+$("#email").val()+
    "<td>"+$("#contact-number").val()+
    "</td></tr>"
  );
  $("form input").val("");
  $("form #submit").val("Add User");
  })

})












// $('#myForm').submit(function() {
//     // get all the inputs into an array.
//     var $inputs = $('#myForm :input');

//     // not sure if you wanted this, but I thought I'd add it.
//     // get an associative array of just the values.
//     var values = {};
//     $inputs.each(function() {
//         values[this.name] = $(this).val();
//     });

// });