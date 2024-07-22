function solve(modernString){
    let matches = modernString.matchAll(/#(?<words>[A-Za-z]+)/g)
    for( let match of matches){
        console.log(match.groups.words)
    }
}
solve('Nowadays everyone uses # to tag a #special word in #socialMedia')