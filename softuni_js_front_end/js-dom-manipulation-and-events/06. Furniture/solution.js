function solve() {
  const generateButton = document.querySelectorAll('#exercise button:first-of-type')[0];
  const buyButton = document.querySelectorAll('#exercise button:last-of-type')[0]
  generateButton.addEventListener('click',() =>{
    const inputElement = document.querySelectorAll('#exercise textarea:first-of-type')[0];
    const inputs = JSON.parse(inputElement.value)
    for (const input of inputs) {
      const tBodyElement = document.querySelectorAll('.table tbody')[0]
      const trElement = document.createElement('tr');
      const tdImgElement = document.createElement('td');
      const imgElement = document.createElement('img');
      imgElement.src = input.img;
      tdImgElement.appendChild(imgElement);
      trElement.appendChild(tdImgElement);

      const tdNameElement = document.createElement('td');
      const pNameElement = document.createElement('p');
      pNameElement.textContent = input.name;
      tdNameElement.appendChild(pNameElement);
      trElement.appendChild(tdNameElement);

      const tdPriceElement = document.createElement('td');
      const pPriceElement = document.createElement('p');
      pPriceElement.textContent = input.price;
      tdPriceElement.appendChild(pPriceElement);
      trElement.appendChild(tdPriceElement);

      const tdDecElement = document.createElement('td');
      const pDecElement = document.createElement('p');
      pDecElement.textContent = input.decFactor;
      tdDecElement.appendChild(pDecElement);
      trElement.appendChild(tdDecElement);

      const tdMarkElement = document.createElement('td')
      const markElement = document.createElement('input')
      markElement.type = 'checkbox'
      tdMarkElement.appendChild(markElement)
      trElement.appendChild(tdMarkElement)

      tBodyElement.appendChild(trElement)
    }
    
    

  })
  buyButton.addEventListener('click',() =>{
    const resultElement = document.querySelectorAll('#exercise textarea:last-of-type')[0]
    resultElement.textContent = ''
    const boughtFurniture = []
    let totalPrice = 0
    let itemCount = 0
    let decSum = 0
    const trElements = document.querySelectorAll('tbody tr')
    Array.from(trElements)
    .forEach(element => {
      const markElement = element.querySelectorAll('input[type=checkbox]')[0]
      if(markElement.checked === true){
        itemCount++
        const pNameElement = element.children.item(1).textContent;
        boughtFurniture.push(pNameElement)
        const pPriceElement = element.children.item(2).textContent;
        totalPrice += Number(pPriceElement)
        const pDecElement = element.children.item(3).textContent
        decSum += Number(pDecElement)
      }else{
        return;
      }
    })
    const totalDec = decSum / itemCount
    resultElement.textContent += `Bought furniture: ${boughtFurniture.join(', ')}\n`
    resultElement.textContent += `Total price: ${totalPrice.toFixed(2)}\n`
    resultElement.textContent += `Average decoration factor: ${totalDec.toFixed(1)}` 
  })
}