function addItem() {
    const textElement = document.getElementById('newItemText');
    const valueElement = document.getElementById('newItemValue');
    const selectElement = document.getElementById('menu')
    const text = textElement.value;
    const value = valueElement.value;
    const optionElement = document.createElement('option')
    optionElement.textContent = text;
    optionElement.value = value;
    selectElement.appendChild(optionElement);
    textElement.value = '';
    valueElement.value = '';
}