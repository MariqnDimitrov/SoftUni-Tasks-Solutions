function solve(food, weight, money){
    kilogramWeight = weight / 1000
    finalPrice = money * kilogramWeight
    console.log(`I need $${finalPrice.toFixed(2)} to buy ${kilogramWeight.toFixed(2)} kilograms ${food}.`)
}
solve('apple', 1563, 2.35)