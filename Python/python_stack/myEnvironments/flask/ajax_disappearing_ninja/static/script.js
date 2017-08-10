
$(document).ready(function() {
  console.log('ready');
  $('a').click(function(event) {
    event.preventDefault();
    var attr = $(this).attr('name');
    var result = {};
    result['color'] = attr;
    console.log(result);
    $('#colors').submit();
  })
})
