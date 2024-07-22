function solve(array, step){
    let finalArray = [];
    for(let i = 0; i < array.length; i += step){
        finalArray.push(array[i])
    }
    return finalArray
}
solve(['5', 
'20', 
'31', 
'4', 
'20'], 
2
)