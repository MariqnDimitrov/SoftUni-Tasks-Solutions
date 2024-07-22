window.addEventListener("load", solve);

function solve() {
    const addButtonElement = document.getElementById('add-btn')
    const ulElement = document.getElementById('check-list')
    const ulContactListElement = document.getElementById('contact-list')

    addButtonElement.addEventListener('click',(e) => {
      const nameElement = document.getElementById('name')
      const phoneNumberElement = document.getElementById('phone')
      const categoryElement = document.getElementById('category')
      if(nameElement.value !== '' & phoneNumberElement.value !== '' & categoryElement.value != ''){
        const liElement = document.createElement('li')
        liElement.style.display = 'flex'
        
        const articleElement = document.createElement('article')
        articleElement.style.display = 'flex'
        

        const pNameElement = document.createElement('p')
        pNameElement.textContent = `name:${nameElement.value}`

        const pPhoneElement = document.createElement('p')
        pPhoneElement.textContent = `phone:${phoneNumberElement.value}`

        const pCategoryElement = document.createElement('p')
        pCategoryElement.textContent = `category:${categoryElement.value}`

        const divButtons = document.createElement('div')
        divButtons.className = 'buttons'
        divButtons.style.display = 'flex'

        const editButton = document.createElement('button')
        editButton.className = 'edit-btn'

        const saveButton = document.createElement('button')
        saveButton.className = 'save-btn'

        articleElement.appendChild(pNameElement)
        articleElement.appendChild(pPhoneElement)
        articleElement.appendChild(pCategoryElement)

        divButtons.appendChild(editButton)
        divButtons.appendChild(saveButton)

        liElement.appendChild(articleElement)
        liElement.appendChild(divButtons)

        ulElement.appendChild(liElement)
        const editName = nameElement.value
        const editPhoneNumber = phoneNumberElement.value
        const editCategory = categoryElement.value

        nameElement.value = ''
        phoneNumberElement.value = ''
        categoryElement.value = ''

        editButton.addEventListener('click',() => {
          nameElement.value = editName
          phoneNumberElement.value = editPhoneNumber
          categoryElement.value = editCategory
          liElement.remove()

        })
        saveButton.addEventListener('click', () => {
          liElement.removeChild(divButtons)
          const delButtonElement = document.createElement('button')
          delButtonElement.className = 'del-btn'
          const clonedLiElement = liElement.cloneNode(true)
          clonedLiElement.appendChild(delButtonElement)
          ulContactListElement.appendChild(clonedLiElement)
          delButtonElement.addEventListener('click',() => {
            ulContactListElement.removeChild(clonedLiElement)
          })
          liElement.remove()  
        })
        
        
      }
    })
    
  }
  