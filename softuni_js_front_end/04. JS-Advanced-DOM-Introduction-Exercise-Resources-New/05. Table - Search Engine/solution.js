function solve() {
   document.querySelector('#searchBtn').addEventListener('click', onClick);

   function onClick() {
      const searchElement = document.getElementById('searchField')
      const trElements = document.querySelectorAll('tbody > tr')
      for (const trElement of trElements) {
         const tdElements = trElement.querySelectorAll('td');
         let isSelected = false
         trElement.classList.remove('select')
         for (const tdElement of tdElements) {
            if(tdElement.textContent.includes(searchElement.value)){
               isSelected = true
               break;
            }            
         }
         if(isSelected){
            trElement.className = 'select';
         }
         
      }
      searchElement.value = ''
     
      }
}
