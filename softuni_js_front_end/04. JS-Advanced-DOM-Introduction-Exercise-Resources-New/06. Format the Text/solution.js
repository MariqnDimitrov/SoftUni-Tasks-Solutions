function solve() {
  const inputElement = document.getElementById('input')
  const outputElement = document.getElementById('output')
  const input = inputElement.value
  const result = input
    .split('.')
    .filter(sentence => sentence)
    .reduce((result, sentence, index) => {
      let resultIndex = Math.floor(index / 3)
      if(!result[resultIndex]){
        result[resultIndex] = []
      }
      result[resultIndex].push(sentence.trim())
      return result
    }, [])
    .map(sentence => `<p>${sentence.join('. ')}.</p>`)
    .join('\n')
  outputElement.innerHTML = result
}