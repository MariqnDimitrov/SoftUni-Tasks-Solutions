function solve(number){
    matrix = []
    for(let i = 0; i < number; i++){
        matrix.push([])
        for(let j = 0; j < number; j++){
            matrix[i].push(number)
        }
    }
    matrix.forEach(row => console.log(row.join(' ')));
}
solve(3)