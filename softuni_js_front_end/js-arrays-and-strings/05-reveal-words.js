function solve(hiddenWords, sentence){
    let hiddenArray = hiddenWords.split(', ');
    let matches = sentence.matchAll(/\*+/g);
    for(const match of matches){
        const word = hiddenArray.find(w => w.length === match[0].length)
        sentence = sentence.replace(match[0], word)
    }
    console.log(sentence)

    
}
solve('great, learning',
'softuni is ***** place for ******** new programming languages'

)