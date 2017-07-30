function slotMachine(quarters, goal=0) {
  while (quarters > 0 && quarters > goal) {
    quarters--;
    if (Math.floor(Math.random() * 100 ) + 1 === 7) {
      quarters += winQuarters();
      return quarters;
    }
  }
  return quarters;
}

function winQuarters() {
  return Math.floor(Math.random() * 50) + 50;
}