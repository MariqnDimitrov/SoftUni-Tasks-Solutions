window.addEventListener("load", solve)

function solve() {
    const adoptBtnElement = document.getElementById('adopt-btn');
    const adoptionInfoElement = document.getElementById('adoption-info');
    const inputTypeElement = document.getElementById('type');
    const inputAgeElement = document.getElementById('age');
    const selectGenderElement = document.getElementById('gender');
    const adoptedListElement = document.getElementById('adopted-list');
    adoptBtnElement.addEventListener('click', (e) => {
      e.preventDefault();
      if(inputTypeElement.value != '' && inputAgeElement.value != '' && (selectGenderElement.value == 'male' || selectGenderElement.value == 'female')){
        const liElement = document.createElement('li');
        const articleElement = document.createElement('article');

        const pTypeElement = document.createElement('p');
        pTypeElement.textContent = `Pet:${inputTypeElement.value}`;
        const editInputTypeText = inputTypeElement.value;

        const pGenderElement = document.createElement('p');
        pGenderElement.textContent = `Gender:${selectGenderElement.value}`;
        const editInputGenderText = selectGenderElement.value;

        const pAgeElement = document.createElement('p');
        pAgeElement.textContent = `Age:${inputAgeElement.value}`;
        const editInputAgeText = inputAgeElement.value;

        const divBtnsElement = document.createElement('div');
        divBtnsElement.className = 'buttons';

        const editBtnElement = document.createElement('button');
        editBtnElement.className = 'edit-btn';
        editBtnElement.textContent = 'Edit';

        editBtnElement.addEventListener('click', () => {
          inputTypeElement.value = editInputTypeText;
          inputAgeElement.value = editInputAgeText;
          selectGenderElement.value = editInputGenderText;
          adoptionInfoElement.removeChild(liElement);
        })

        const doneBtnElement = document.createElement('button');
        doneBtnElement.className = 'done-btn';
        doneBtnElement.textContent = 'Done';
        doneBtnElement.addEventListener('click', () => {
          liElement.removeChild(divBtnsElement);
          const liClone = liElement.cloneNode(true);
          adoptionInfoElement.removeChild(liElement)
          const clearBtnElement = document.createElement('button');
          clearBtnElement.className = 'clear-btn';
          clearBtnElement.textContent = 'Clear';
          liClone.appendChild(clearBtnElement);
          adoptedListElement.appendChild(liClone);
          clearBtnElement.addEventListener('click', () => {
            adoptedListElement.removeChild(liClone);
          })
        })
        articleElement.appendChild(pTypeElement);
        articleElement.appendChild(pGenderElement);
        articleElement.appendChild(pAgeElement);

        divBtnsElement.appendChild(editBtnElement);
        divBtnsElement.appendChild(doneBtnElement);

        liElement.appendChild(articleElement);
        liElement.appendChild(divBtnsElement);

        adoptionInfoElement.appendChild(liElement);

        inputTypeElement.value = '';
        inputAgeElement.value = '';
        selectGenderElement.value = '';

      }
  })
}
  