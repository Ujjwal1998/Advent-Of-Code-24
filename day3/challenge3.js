const fs = require("node:fs");

function getInput(location) {
  const data = fs.readFileSync(String(location), "utf-8");
  return data;
}

function solution1() {
  const input = getInput(
    "/Users/utalwar/Projects/Advent-Of-Code-24/day3/input.txt"
  );

  let res = [];
  for (let i = 0; i < input.length; i++) {
    if (performScan && input[i] === "m") {
      if (input[i + 1] === "u") {
        if (input[i + 2] === "l") {
          if (input[i + 3] === "(") {
            if (isNaN(input[i + 4])) continue;
            else {
              let k = 4;
              let num1 = "";
              let num2 = "";
              while (!isNaN(input[i + k])) {
                num1 += input[i + k];
                k++;
              }
              if (!(input[i + k] === ",")) continue;
              k++;
              while (!isNaN(input[i + k])) {
                num2 += input[i + k];
                k++;
              }
              if (!(input[i + k] === ")")) continue;
              res.push(parseInt(num1) * parseInt(num2));
            }
          }
        }
      }
    }
  }
  return res.reduce((acc, val) => acc + val, 0);
}
function solution2() {
  const input = getInput(
    "/Users/utalwar/Projects/Advent-Of-Code-24/day3/input.txt"
  );

  let res = [];
  let performScan = true;
  for (let i = 0; i < input.length; i++) {
    if (performScan && input[i] === "m") {
      if (input[i + 1] === "u") {
        if (input[i + 2] === "l") {
          if (input[i + 3] === "(") {
            if (isNaN(input[i + 4])) continue;
            else {
              let k = 4;
              let num1 = "";
              let num2 = "";
              while (!isNaN(input[i + k])) {
                num1 += input[i + k];
                k++;
              }
              if (!(input[i + k] === ",")) continue;
              k++;
              while (!isNaN(input[i + k])) {
                num2 += input[i + k];
                k++;
              }
              if (!(input[i + k] === ")")) continue;

              res.push(parseInt(num1) * parseInt(num2));
            }
          }
        }
      }
    }
    if (input[i] === "d") {
      if (input[i + 1] === "o") {
        if (input[i + 2] === "(") {
          if (input[i + 3] === ")") performScan = true;
        } else {
          if (input[i + 2] === "n") {
            if (input[i + 3] === "'") {
              if (input[i + 4] === "t") {
                if (input[i + 5] === "(") {
                  if (input[i + 6] === ")") performScan = false;
                }
              }
            }
          }
        }
      }
    }
  }
  return res.reduce((acc, val) => acc + val, 0);
}
