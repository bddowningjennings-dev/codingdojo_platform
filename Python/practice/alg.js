function reverse(str) {
  var temp = "";
    for (var i = str.length - 1; i >=0; i--) {
      temp += str[i];
    }
    return temp;
}
console.log(reverse("meow"));

function Add(str, indx, str2) {
  var temp = "";
  for (var i = 0; i < str.length; i++) {
    if (i === indx) {
      temp += str2;
    }
    temp += str[i];
  }
  return temp;
}
console.log(Add("meow",2,"bob"));


