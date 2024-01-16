function solution(arr, queries) {
  queries.forEach((d, i) => {
    arr[d[0]] ^= arr[d[1]];
    arr[d[1]] ^= arr[d[0]];
    arr[d[0]] ^= arr[d[1]];
  });
  return arr;
}
