function solve(){
    const baseUrl = 'http://localhost:3030/jsonstore/records'
    const loadRecordsBtnElement = document.getElementById('load-records');
    const listUlElement = document.getElementById('list');
    const addBtnElement = document.getElementById('add-record');
    const inputNameElement = document.getElementById('p-name');
    const inputStepsElement = document.getElementById('steps');
    const inputCaloriesElement = document.getElementById('calories');
    const editBtnElement = document.getElementById('edit-record');
    let currentPersonId = null;
    loadRecordsBtnElement.addEventListener('click', () => reload())
    addBtnElement.addEventListener('click', async () => {
         await fetch(baseUrl, {
            method: 'POST',
            headers:{
                'content-type': 'application/json',
            },
            body: JSON.stringify({
                "name" : inputNameElement.value,
                "steps" : inputStepsElement.value,
                "calories" : inputCaloriesElement.value,
                "_id": currentPersonId,
            })
        })
        inputNameElement.value = '';
        inputStepsElement.value = '';
        inputCaloriesElement.value = '';
        reload();
    })
    editBtnElement.addEventListener('click', async () => {
        await fetch(`${baseUrl}/${currentPersonId}`,{
            method: 'PUT',
            headers:{
                'Content-Type': 'application/json',
            },
            body:JSON.stringify({
                "name": inputNameElement.value,
                "steps": inputStepsElement.value,
                "calories": inputCaloriesElement.value,
                "_id": currentPersonId,
            })
        })
        inputNameElement.value = '';
        inputStepsElement.value = '';
        inputCaloriesElement.value = '';
        editBtnElement.setAttribute('disabled', 'disabled');
        addBtnElement.removeAttribute('disabled');
        reload();
    })
    function reload(){
        listUlElement.innerHTML = '';
        fetch(baseUrl)
        .then(res => res.json())
        .then(data => {
            Object.values(data).forEach(person => {
                const liElement = document.createElement('li');
                liElement.className = 'record';
                                
                const divInfoElement = document.createElement('div');
                divInfoElement.className = 'info';
                
                const pNameElement = document.createElement('p');
                pNameElement.textContent = person.name;
                
                const pStepsElement = document.createElement('p');
                pStepsElement.textContent = person.steps;
                
                const pCaloriesElement = document.createElement('p');
                pCaloriesElement.textContent = person.calories;
        
                const divBtnWrapperElement = document.createElement('div');
                divBtnWrapperElement.className = 'btn-wrapper';
                
                const changeBtnElement = document.createElement('button');
                changeBtnElement.className = 'change-btn';
                changeBtnElement.textContent = 'Change';
                       
                const deleteBtnElement = document.createElement('button');
                deleteBtnElement.className = 'delete-btn';
                deleteBtnElement.textContent = 'Delete';
        
                divInfoElement.appendChild(pNameElement);
                divInfoElement.appendChild(pStepsElement);
                divInfoElement.appendChild(pCaloriesElement);
                
                divBtnWrapperElement.appendChild(changeBtnElement);
                divBtnWrapperElement.appendChild(deleteBtnElement)
                
                liElement.appendChild(divInfoElement);
                liElement.appendChild(divBtnWrapperElement);
                
                listUlElement.appendChild(liElement);  
                changeBtnElement.addEventListener('click', () => {
                    inputNameElement.value = person.name;
                    inputStepsElement.value = person.steps;
                    inputCaloriesElement.value = person.calories;
                    liElement.remove();
                    editBtnElement.removeAttribute('disabled');
                    addBtnElement.setAttribute('disabled', 'disabled');
                    currentPersonId = person._id;
                })
                deleteBtnElement.addEventListener('click', async () => {
                    await fetch(`${baseUrl}/${person._id}`,{
                        method: 'DELETE',
                    })
                    reload();
                })
            })
        })
         
    }
}

solve()