function solve(number){
    const stringNum = number.toString();
    const numArray = [];
    for (const number of stringNum) {
        numArray.push(Number(number));
    }
    oddSum = numArray
                    .filter(num => num % 2 !== 0)
                    .reduce((sum, number) => sum + number, 0);            
    evenSum = numArray
                    .filter(num => num % 2 == 0)
                    .reduce((sum, number) => sum + number, 0); 
                    
    console.log(`Odd sum = ${oddSum}, Even sum = ${evenSum}`)
}
solve(1000435);