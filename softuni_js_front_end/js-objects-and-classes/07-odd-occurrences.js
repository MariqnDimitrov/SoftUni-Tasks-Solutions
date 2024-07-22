function solve(sentence){
    const oddOccurancesWords = new Set();
    const sentenceArr = sentence.split(' ');
    for (const searchedWord of sentenceArr) {
        const wordObj = {
            word: searchedWord.toLowerCase(),
            occurances: 0,
        };
        for (const word of sentenceArr) {
            if(word.toLowerCase() == searchedWord.toLowerCase()){
                wordObj.occurances += 1;
            }   
        }
        if (wordObj.occurances % 2 != 0){
            oddOccurancesWords.add(wordObj.word)
        }   
    }
    console.log(Array.from(oddOccurancesWords).join(' '))
}
solve('Java C# Php PHP Java PhP 3 C# 3 1 5 C#')