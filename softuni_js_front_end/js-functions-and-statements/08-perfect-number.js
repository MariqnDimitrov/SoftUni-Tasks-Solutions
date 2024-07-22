function solve(number){
    const divisors = []
    for( let i = 0; i <= number / 2; i++){
        if(number % i == 0){
            divisors.push(i)
        }
    }
    result = divisors.reduce((sum,number) => sum + number, 0)
    if(result === number){
        console.log("We have a perfect number!")
    }else{
        console.log("It's not so perfect.")
    }
}
solve(1236498)