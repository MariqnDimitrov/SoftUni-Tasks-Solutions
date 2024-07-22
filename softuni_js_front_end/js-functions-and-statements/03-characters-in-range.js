function solve(firstChar, secondChar){
    const numArray = []
    const smallerNum = Math.min(firstChar.charCodeAt(0), secondChar.charCodeAt(0))
    const biggerNum = Math.max(firstChar.charCodeAt(0), secondChar.charCodeAt(0))

    for(let i = smallerNum + 1; i < biggerNum; i++){
        let currChar = String.fromCharCode(i)
        numArray.push(currChar)
    }
    console.log(numArray.join(' '))
}
solve('C',
'#'
)