function attachEvents() {
    const phonebookUrl = 'http://localhost:3030/jsonstore/phonebook'
    const loadBtnElement = document.getElementById("btnLoad");
    const createBtnElement = document.getElementById("btnCreate");
    const phonebookElement = document.getElementById('phonebook');
    const personInputElement = document.getElementById('person');
    const phoneInputElement = document.getElementById('phone')
    loadBtnElement.addEventListener('click' , () => {
        phonebookElement.innerHTML = '';
        fetch(phonebookUrl)
            .then(res => res.json())
            .then(data => {
                Object.values(data)
                    .forEach(entry => {
                        phonebookElement.appendChild(createLiElement(entry));
            });
        })
    });
    createBtnElement.addEventListener('click', () => {
        fetch(phonebookUrl, {
            method: 'POST',
            headers:{
                'content-type': 'application/json',
            },
            body: JSON.stringify({
                'person': personInputElement.value,
                'phone': phoneInputElement.value,
            })
        }).then(res => res.json())
        .then(entry => {
            const liElement = createLiElement(entry);
            phonebookElement.appendChild(liElement);
            personInputElement.value = '';
            phoneInputElement.value = '';
        })
    })
    function createLiElement({_id, person, phone}){
        const liElement = document.createElement('li');
        liElement.textContent = `${person}: ${phone}`; 

        const deleteBtnElement = document.createElement('button');
        deleteBtnElement.textContent = 'Delete';

        deleteBtnElement.addEventListener('click', () => {
        fetch(`${phonebookUrl}/${_id}`, {
                method: 'DELETE',
            })
            .then(() => {
                liElement.remove();
            });
        });
        
        liElement.appendChild(deleteBtnElement);
        return liElement;
    }
}

attachEvents();