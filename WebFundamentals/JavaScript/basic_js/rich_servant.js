function reward (days, amount = Infinity) {
  var value = 0.01;
  if (days < 0 || isNaN(days)) {
    return 0;
  }
  for (var i = 1; i < days; i++) {
    if (value === amount || value > amount) {
      break;
    }
    value *= 2;
  }
  console.log("At", i, "days the amount is", value);
}

//At 30 days the amount is 5368709.12
//At 21 days the amount is 10485.76
//At 38 days the amount is 1374389534.72
//At 1032 days the amount is Infinity