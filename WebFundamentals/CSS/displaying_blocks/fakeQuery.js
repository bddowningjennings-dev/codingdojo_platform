var $ = function(elementId) {
  var el = document.getElementById(elementId);
  return {
    setText: function(value) {
      el.innerHTML = value;
    },
    addClickThingy: function(thingToDo) {
      el.addEventListener('click', thingToDo);
    },
    onLoad: function() {
      document.addEventListener("load", console.log("hi"))
    }
  }
}