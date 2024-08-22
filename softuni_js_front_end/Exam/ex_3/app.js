function solve(){
    const baseUrl = 'http://localhost:3030/jsonstore/appointments'
    const loadAppointmentsBtnElement = document.getElementById('load-appointments');
    const ulAppointmentsListElement = document.getElementById('appointments-list');
    const carModelInputElement = document.getElementById('car-model');
    const carServiceSelectElement = document.getElementById('car-service');
    const dateInputElement = document.getElementById('date');
    const addAppointmentBtnElement = document.getElementById('add-appointment');
    const editAppointmentBtnElement = document.getElementById('edit-appointment')
    let currentAppointmentId = null;
    loadAppointmentsBtnElement.addEventListener('click', () => {reload()})
    addAppointmentBtnElement.addEventListener('click', async () => {
        await fetch(baseUrl,{
            method: 'POST',
            headers:{
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({
                "model": carModelInputElement.value,
                "service": carServiceSelectElement.value,
                "date": dateInputElement.value, 
            })
        })
        reload();
        carModelInputElement.value = '';
        carServiceSelectElement.value = '';
        dateInputElement.value = '';
    })
    editAppointmentBtnElement.addEventListener('click', async () => {
        await fetch(`${baseUrl}/${currentAppointmentId}`, {
            method: "PUT",
            headers: {
                'Content-Type' : 'application-json',
            },
            body: JSON.stringify({
                "model": carModelInputElement.value,
                "service": carServiceSelectElement.value,
                "date": dateInputElement.value,
                "_id": currentAppointmentId,
            })
        })
        reload();
        editAppointmentBtnElement.setAttribute('disabled', 'disabled');
        addAppointmentBtnElement.removeAttribute('disabled');
        carModelInputElement.value = '';
        carServiceSelectElement.value = '';
        dateInputElement.value = '';
    })
    function reload(){
        ulAppointmentsListElement.innerHTML = '';
        fetch(baseUrl)
        .then(res => res.json())
        .then(data => {
            Object.values(data)
            .forEach(appointment => {
                const appointmentLiElement = document.createElement('li');
                appointmentLiElement.className = 'appointment';

                const h2CarModelElement = document.createElement('h2')
                h2CarModelElement.textContent = appointment.model;

                const h3DateElement = document.createElement('h3');
                h3DateElement.textContent = appointment.date;

                const h3ServiceElement = document.createElement('h3');
                h3ServiceElement.textContent = appointment.service;

                const divBtnsAppointmentElement = document.createElement('div');
                divBtnsAppointmentElement.className = 'buttons-appointment';

                const changeBtnElement = document.createElement('button');
                changeBtnElement.className = 'change-btn';
                changeBtnElement.textContent = 'Change';

                const deleteBtnElement = document.createElement('button');
                deleteBtnElement.className = 'delete-btn';
                deleteBtnElement.textContent = 'Delete';

                appointmentLiElement.appendChild(h2CarModelElement);
                appointmentLiElement.appendChild(h3DateElement);
                appointmentLiElement.appendChild(h3ServiceElement);
                appointmentLiElement.appendChild(divBtnsAppointmentElement);

                divBtnsAppointmentElement.appendChild(changeBtnElement);
                divBtnsAppointmentElement.appendChild(deleteBtnElement);

                ulAppointmentsListElement.appendChild(appointmentLiElement);

                changeBtnElement.addEventListener('click', () => {
                    carModelInputElement.value = appointment.model;
                    carServiceSelectElement.value = appointment.service;
                    dateInputElement.value = appointment.date;
                    currentAppointmentId = appointment._id;
                    editAppointmentBtnElement.removeAttribute('disabled');
                    addAppointmentBtnElement.setAttribute('disabled', 'disabled');
                    appointmentLiElement.remove();
                })

                deleteBtnElement.addEventListener('click', async () => {
                    await fetch(`${baseUrl}/${appointment._id}`, {
                        method: 'DELETE',
                    })
                    appointmentLiElement.remove();
                    reload();
                })

            })
        })
    }
}
solve();