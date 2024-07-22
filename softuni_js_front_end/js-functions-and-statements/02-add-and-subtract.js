function solve(firstNum, secondNum, thirdNum){
    function sum(){
        const numberSum = firstNum + secondNum
        return numberSum
    }
    function subtract(){
        const result = sum() - thirdNum
        return result
    }
    console.log(subtract())
}
solve(23,
    6,
    10
    )