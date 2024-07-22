function solve(number, ...operations){
    let result = Number(number);
    for(let i = 0; i < operations.length; i++){
            if(operations[i] === 'chop'){
                result = result / 2;
            }else if(operations[i] === 'dice'){
                result = Math.sqrt(result);
            }else if(operations[i] === 'spice'){
                result += 1;
            }else if(operations[i] === 'bake'){
                result = result * 3;
            }else if(operations[i] === 'fillet'){
                result -= result * 0.2;
            }
        console.log(result)
    }  
}
solve('9', 'dice', 'spice', 'chop', 'bake', 'fillet')