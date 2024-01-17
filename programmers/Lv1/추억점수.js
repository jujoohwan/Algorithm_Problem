function solution(name, yearning, photo) {
    var answer = []
    photo.map((arr) => {
        let temp = 0;
        arr.forEach((data) => {

            const index = name.indexOf(data)
            if (index >= 0) {
                temp += yearning[index]
            }

        })
        answer.push(temp)
    })

    return answer;
}