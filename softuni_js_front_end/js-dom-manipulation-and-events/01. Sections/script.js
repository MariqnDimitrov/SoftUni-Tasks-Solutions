function create(words) {
   const divContentElement = document.getElementById('content')
   words.forEach(word => {
      const divElement = document.createElement('div')
      const pElement = document.createElement('p')
      pElement.textContent = word
      pElement.style.display = 'none'
      divElement.appendChild(pElement)
      divContentElement.appendChild(divElement)
      divElement.addEventListener('click',(e) => {
         pElement.style.display = 'block'
      })
      
      
   });
}