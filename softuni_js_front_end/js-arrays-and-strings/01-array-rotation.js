function solve(array, numberRotations){
    for( let i = 0; i < numberRotations; i++){
        rotatingNumber = array.shift();
        array.push(rotatingNumber);
    }
    console.log(array.join(' '));

}
solve([51, 47, 32, 61, 21], 2)

function solve1(array, numberRotations){
    let rotatedArray = []
    for( let j = 0; j < numberRotations; j++){
        rotatedArray = array.slice(1, array.length);
        rotatedArray.push(array[0])
        array = rotatedArray;
    }
    console.log(rotatedArray)
}
solve1([51, 47, 32, 61, 21], 2)