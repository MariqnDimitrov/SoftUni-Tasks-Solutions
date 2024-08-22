window.addEventListener("load", solve);

function solve() {
    const clearBtnElement = document.querySelector('#laptops-container div div > button')
    const ulCheckListElement = document.getElementById('check-list');
    const ulLaptopsListElement = document.getElementById('laptops-list');
    const addBtnElement = document.getElementById('add-btn');
    const laptopmodelInputElement = document.getElementById('laptop-model');
    const storageInputElement = document.getElementById('storage');
    const priceInputElement = document.getElementById('price');
    
      addBtnElement.addEventListener('click', () => {
        if(laptopmodelInputElement.value != '' && storageInputElement.value != '' && priceInputElement.value != ''){
          const liElement = document.createElement('li');
          liElement.className = 'laptop-item';
    
          const articleElement = document.createElement('article');
          
          const pLaptopModelElement = document.createElement('p');
          pLaptopModelElement.textContent = laptopmodelInputElement.value;
          const editLaptopModelText = laptopmodelInputElement.value;
    
          const pStorageElement = document.createElement('p');
          pStorageElement.textContent = `Memory: ${storageInputElement.value} TB`;
          const editStorageElementText = storageInputElement.value;
    
          const pPriceElement = document.createElement('p');
          pPriceElement.textContent = `Price: ${priceInputElement.value}$`;
          const editPriceElementText = priceInputElement.value;
    
          const editBtnElement = document.createElement('button');
          editBtnElement.className = 'btn edit';
          editBtnElement.textContent = 'edit';
          editBtnElement.addEventListener('click', () => {
            laptopmodelInputElement.value = editLaptopModelText;
            storageInputElement.value = editStorageElementText;
            priceInputElement.value = editPriceElementText;
            liElement.remove();
            addBtnElement.removeAttribute('disabled');
          })
    
          const okBtnElement = document.createElement('button');
          okBtnElement.className = 'btn ok';
          okBtnElement.textContent = 'ok'
          okBtnElement.addEventListener('click', () => {
            ulLaptopsListElement.appendChild(liElement);
            liElement.removeChild(editBtnElement);
            liElement.removeChild(okBtnElement);
            ulCheckListElement.removeChild(liElement);
            addBtnElement.removeAttribute('disabled');
          })
    
          articleElement.appendChild(pLaptopModelElement);
          articleElement.appendChild(pStorageElement);
          articleElement.appendChild(pPriceElement);
    
          liElement.appendChild(articleElement);
          liElement.appendChild(editBtnElement);
          liElement.appendChild(okBtnElement);
    
          ulCheckListElement.appendChild(liElement)
          
          addBtnElement.setAttribute('disabled', 'disabled');
          laptopmodelInputElement.value = '';
          storageInputElement.value = '';
          priceInputElement.value = '';
          clearBtnElement.addEventListener('click',() => {
            liElement.remove();
            laptopmodelInputElement.value = '';
            storageInputElement.value = '';
            priceInputElement.value = '';
            addBtnElement.removeAttribute('disabled');
          })
        }
      })  
  }
  