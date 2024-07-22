function solve(number){
    const loadingBar = []
    const loadedPercent = number / 10;
    const leftPercent = (100 - number) / 10;
    loadingBar.push('%'.repeat(loadedPercent))
    loadingBar.push('.'.repeat(leftPercent))
    
    if(number === 100){
        console.log(`${number}% Complete!`)
        console.log(`[${loadingBar.join('')}]`)
    }else{
        console.log(`${number}% [${loadingBar.join('')}]`)
        console.log('Still loading...')
    }
    
}
solve(100)