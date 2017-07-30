function TellTime(hour, minute, period) {
  var msg = "It's";
  if (minute < 31) {
    if (minute === 5) {
      msg += " 5 after ";
    } else if (minute === 15) {
      msg += " quarter after ";
    } else if (minute === 30) {
      msg += " half past ";
    } else {
      msg += " just after ";
    }
  } else {
    msg += " almost ";
    hour++;
  }
  if (hour === 12) {
    if (period === "AM") {
      msg += "midnight";
    } else {
      msg += "noon";
    }
  } else {
  msg += hour + " ";
    if (period === "PM" && hour > 6) {
      msg += "at night";
    } else if (period === "PM" && hour < 3) {
      msg += "in the afternoon";
    } else if (period === "PM") {
      msg += "in the evening";
    } else {
      msg += "in the morning";
    }
  }
  console.log(msg);
}