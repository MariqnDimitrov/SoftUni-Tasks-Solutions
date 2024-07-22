function solve() {
  const sentenceElement = document.getElementById('text');
  const wantedCaseElement = document.getElementById('naming-convention');
  const resultElement = document.getElementById('result');
  let sentence = sentenceElement.value.toLowerCase().split(' ');
  const wantedCase = wantedCaseElement.value;
  const upperCaseConvertor = (text) => text.map(text => text.charAt(0).toUpperCase() + text.slice(1)).join('')
  const convertor = {
    'Pascal Case': (text) => upperCaseConvertor(text),
    'Camel Case': (text) => upperCaseConvertor(text).charAt(0).toLowerCase() + upperCaseConvertor(text).slice(1)
  }
  if(!convertor[wantedCase]){
    resultElement.textContent = 'Error!'
  }else{
    resultElement.textContent = convertor[wantedCase](sentence)
  }
}