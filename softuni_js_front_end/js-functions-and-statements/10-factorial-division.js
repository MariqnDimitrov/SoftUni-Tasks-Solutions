function solve(firstNum, secondNum){
    function factorial(number){
        if (number === 1){
            return 1
        }
        return number * factorial(number - 1)
    }
    result = factorial(firstNum) / factorial(secondNum)
    console.log(result.toFixed(2))
}
solve(5,2)