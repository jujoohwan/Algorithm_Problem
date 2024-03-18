const readline = require("readline").createInterface({
  input: process.stdin,
  output: process.stdout,
});

let input = [];

readline
  .on("line", function (line) {
    input = line.split(" ").map((el) => parseInt(el));
  })
  .on("close", function () {
    // N : 노래 N곡 , L : 모든 노래의 길이 , D : 전화벨 D초에 1번 한번 울리면 1초동안 울림
    // [2 5 7]
    const [N, L, D] = input;
    const time = [N * L + 5 * (N - 1)]; // // 첫노래 멈춘시간 제외
    for (let index = 0; index < N; index++) {
      const s = (L + 5) * index;
      for (let j = s; j < s + L; j++) {
        time[j] = true; // 재생중이면 true, 멈췄으면 false
      }
    }
    console.log(time.length);
    let answer = 0;
    while (answer < time.length) {
      if (!time[answer]) break;
      answer += D;
    }
    console.log(answer);

    process.exit();
  });
