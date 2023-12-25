function solution(code) {
  var answer = "";
  let mode = "0";
  let ret = "";
  for (let i = 0; i < code.length; i++) {
    if (mode == "0") {
      if (code.charAt(i) != "1" && i % 2 == 0) {
        ret += code.charAt(i);
      } else if (code.charAt(i) == "1") {
        mode = "1";
      }
    } else if (mode == "1") {
      if (code.charAt(i) != "1" && i % 2 != 0) {
        ret += code.charAt(i);
      } else if (code.charAt(i) == "1") {
        mode = "0";
      }
    }
  }
  if (ret.length == 0) {
    return "EMPTY";
  }
  return ret;
}
