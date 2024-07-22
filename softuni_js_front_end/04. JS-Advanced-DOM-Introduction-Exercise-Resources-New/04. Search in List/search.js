function search() {
   const townsElement = document.getElementById('towns')
   const searchText = document.getElementById('searchText')
   const matchesElement = document.getElementById('result')
   let matches = 0
   for (const town of Array.from(townsElement.children)) {
      if(town.textContent.toLowerCase().includes(searchText.value.toLowerCase())){
         town.style.textDecoration = 'underline';
         town.style.fontWeight = 'bold';
         matches++
      }else{
         town.style.textDecoration = 'none';
         town.style.fontWeight = '';
      }
      
   }
   matchesElement.textContent = `${matches} matches found`
   searchText.value = ''
   
}
