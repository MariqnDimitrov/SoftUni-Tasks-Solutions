function encodeAndDecodeMessages() {
    const decodedMessageElement = document.querySelectorAll('#main div:first-of-type textarea')[0]
    const encodedMessageElement = document.querySelectorAll('#main div:last-of-type textarea')[0]
    const encodeMessageButton = document.querySelectorAll('#main div:first-of-type button')[0]
    const decodeMessageButton = document.querySelectorAll('#main div:last-of-type button')[0]
    decodeMessageButton.addEventListener('click', () =>{
        const textArr = []
        const text = encodedMessageElement.value;
        text
            .split('')
            .forEach(char => {
                const charAsciiCode = char.charCodeAt(0)
                char = String.fromCharCode(charAsciiCode - 1)
                textArr.push(char)
            });           
        encodedMessageElement.value =  textArr.join('')
    })
    encodeMessageButton.addEventListener('click', () => {
        const textArr = []
        const text = decodedMessageElement.value;
        text
            .split('')
            .forEach(char => {
                const charAsciiCode = char.charCodeAt(0)
                char = String.fromCharCode(charAsciiCode + 1)
                textArr.push(char)
            });
        decodedMessageElement.value = ''
        encodedMessageElement.value =  textArr.join('')
    })


}