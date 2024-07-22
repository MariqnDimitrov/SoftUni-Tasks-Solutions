function solve(text){
    text = text.trim()
    let matches = text.matchAll(/[A-Z][a-z]*/g)
    let words = []
    for(let match of matches){
        words.push(match[0])
    }
    console.log(words.join(', '))
}
solve('ThisIsSoAnnoyingToDo')