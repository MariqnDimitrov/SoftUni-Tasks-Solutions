function solve(array){
    array.sort( (a,b) => a - b)
    sortedArray = []
    while (array.length > 0){
        smallestNumber = array.shift();
        sortedArray.push(smallestNumber);
        if (array.length === 0){
            break
        }
        largestNumber = array.pop();
        sortedArray.push(largestNumber);

    }
    return sortedArray
}
console.log(solve([1, 65, 3, 52, 48, 63, 31, -3, 18, 56]))