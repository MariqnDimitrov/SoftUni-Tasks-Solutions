function solve(strArray){
    const wordOccurances = [];
    const searchedWord = strArray.shift().split(' ')
    for (const word of searchedWord) {
        const wordOccurancesObject = {
            searchedWord: word,
            occurances: 0,
        };
        for (const words of strArray) {
            if(words === word){
                wordOccurancesObject.occurances += 1;
            };
            
        };
        wordOccurances.push(wordOccurancesObject)
    }
    wordOccurances
    .sort((a,b) => b.occurances - a.occurances)
    .forEach(word => console.log(`${word.searchedWord} - ${word.occurances}`))
}
solve([
    'this sentence', 
    'In', 'this', 'sentence', 'you', 'have', 'to', 'count', 'the', 'occurrences', 'of', 'the', 'words', 'this', 'and', 'sentence', 'because', 'this', 'is', 'your', 'task'
    ]
    )