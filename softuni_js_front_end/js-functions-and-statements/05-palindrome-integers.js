function solve(numArray){
    const strArray = numArray.map(a => a.toString())
    for (const str of strArray) {  
        console.log(str === str.split('').reverse().join('')) 
    }
}
solve([32,2,232,1001])