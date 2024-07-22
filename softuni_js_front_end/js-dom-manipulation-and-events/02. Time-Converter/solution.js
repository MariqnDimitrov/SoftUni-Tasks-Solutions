function attachEventsListeners() {
    const daysButtonElement = document.getElementById('daysBtn');
    const hoursButtonElement = document.getElementById('hoursBtn');
    const minutesButtonElement = document.getElementById('minutesBtn');
    const secondsButtonElement = document.getElementById('secondsBtn');
    const daysInputElement = document.getElementById('days');
    const hoursInputElement = document.getElementById('hours');
    const minutesInputElement = document.getElementById('minutes');
    const secondsInputElement = document.getElementById('seconds')
    daysButtonElement.addEventListener("click",() =>{
        const daysInput = daysInputElement.value;
        hoursInputElement.value = 24 * Number(daysInput);
        minutesInputElement.value = 24 * 60 * Number(daysInput);
        secondsInputElement.value = 24 * 60 * 60 * Number(daysInput);
    })
    hoursButtonElement.addEventListener("click",() => {
        const hoursInput = hoursInputElement.value;
        daysInputElement.value = (Number(hoursInput) / 24).toFixed(1);
        minutesInputElement.value = 60 * Number(hoursInput);
        secondsInputElement.value = 60 * 60 * Number(hoursInput);   
    })
    minutesButtonElement.addEventListener("click", () => {
        const minutesInput = minutesInputElement.value;
        daysInputElement.value = (Number(minutesInput) / 60 / 24).toFixed(1);
        hoursInputElement.value = (Number(minutesInput) / 60).toFixed(1);
        secondsInputElement.value = 60 * Number(minutesInput);
    })
    secondsButtonElement.addEventListener("click", () => {
        const secondsInput = secondsInputElement.value;
        daysInputElement.value = (Number(secondsInput)/ 60 / 60 / 24).toFixed(1);
        hoursInputElement.value = (Number(secondsInput) / 60 / 60).toFixed(1);
        minutesInputElement.value = (Number(secondsInput) / 60).toFixed(1);
    })
}