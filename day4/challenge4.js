const fs = require("node:fs");

const grid = fs
  .readFileSync("./input.txt")
  .toString()
  .split("\n")
  .map((line) => line.split(""));

function solution1(grid) {
  const m = grid.length,
    n = grid[0].length;
  const directions = [
    [0, 1],
    [1, 0],
    [-1, 0],
    [0, -1],
    [1, 1],
    [1, -1],
    [-1, 1],
    [-1, -1],
  ];
  function withinBounds(x, y) {
    return x >= 0 && y >= 0 && x < m && y < n;
  }
  function checkMatch(i, j, direction) {
    for (let k = 0; k < "XMAS".length; k++) {
      let nbrX = i + k * direction[0];
      let nbrY = j + k * direction[1];
      if (!withinBounds(nbrX, nbrY)) {
        return false;
      }
      if (grid[nbrX][nbrY] !== "XMAS"[k]) return false;
    }
    return true;
  }
  let res = 0;
  for (let i = 0; i < m; i++) {
    for (let j = 0; j < n; j++) {
      for (const direction of directions) {
        res += checkMatch(i, j, direction) ? 1 : 0;
      }
    }
  }
  return res;
}
function solution2(grid) {
  const m = grid.length,
    n = grid[0].length;
  function withinBounds(x, y) {
    return x >= 0 && y >= 0 && x < m && y < n;
  }
  let directions = [
    [
      [1, 1],
      [-1, -1],
    ],
    [
      [-1, 1],
      [1, -1],
    ],
  ];
  function checkNeighbors(i, j) {
    for (let dir of directions) {
      let nbrX = i + dir[0][0];
      let nbrY = j + dir[0][1];
      let nbrX2 = i + dir[1][0];
      let nbrY2 = j + dir[1][1];

      if (!withinBounds(nbrX, nbrY) || !withinBounds(nbrX2, nbrY2))
        return false;
      if (
        !(
          (grid[nbrX][nbrY] === "M" && grid[nbrX2][nbrY2] === "S") ||
          (grid[nbrX][nbrY] === "S" && grid[nbrX2][nbrY2] === "M")
        )
      )
        return false;
    }
    return true;
  }
  let res = 0;
  for (let i = 0; i < m; i++) {
    for (let j = 0; j < n; j++) {
      if (grid[i][j] === "A") {
        res += checkNeighbors(i, j);
      }
    }
  }
  return res;
}
