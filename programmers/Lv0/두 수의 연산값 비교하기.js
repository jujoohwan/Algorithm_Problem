function solution(a, b) {
  let temp1 = Number(String(a) + String(b));
  let temp2 = 2 * a * b;
  return temp1 < temp2 ? temp2 : temp1;
}
