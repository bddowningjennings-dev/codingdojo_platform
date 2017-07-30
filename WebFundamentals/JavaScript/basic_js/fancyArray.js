function fancyArray (arr, sym, reversed = false) {
  sym = " " + sym + " ";
  for (var i = 0; i < arr.length; i ++) {
    if (reversed) {
      console.log(i + sym + arr[(arr.length - 1) - i]);
    } else {
      console.log(i + sym + arr[i]);
    }
  }
}