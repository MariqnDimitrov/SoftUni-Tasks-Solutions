function solve(number){
    let textNumber = number.toString();
    let sum = 0;
    let sameDigits = true;
    for(let i = 0; i < textNumber.length; i++){
        sum += Number(textNumber[i]);
        if(textNumber[i] !== textNumber[0]){
            sameDigits = false;
        }
    }
    if(sameDigits === true){
        console.log("true");
    }else{
        console.log("false");
    }
    console.log(sum)
}
solve(1234)
