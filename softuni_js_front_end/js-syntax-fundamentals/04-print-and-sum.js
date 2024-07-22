function solve(start, end){
    let number = 0
    let result = ''
    for(let i = start ; i <= end; i++){
        number += i
        result += i + ' '
    }
    console.log(result.trim())
    console.log(`Sum: ${number}`)
}
solve(0,26)