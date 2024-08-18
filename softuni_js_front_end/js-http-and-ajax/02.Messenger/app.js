function attachEvents() {
    const messageUrl = 'http://localhost:3030/jsonstore/messenger'
    const submitElement = document.getElementById('submit')
    const refreshElement = document.getElementById('refresh')
    const nameLabelElement = document.querySelector("#controls div input[name='author']")
    const contentLabelElement = document.querySelector("#controls div input[name='content']")
    const messageAreaElement = document.getElementById('messages')
    submitElement.addEventListener('click' , () => {
        fetch(messageUrl, {
            method: 'POST',
            headers: {
                'content-type': 'application/json',
            },
            body: JSON.stringify({
                'author': nameLabelElement.value,
                'content': contentLabelElement.value,
            }),
        });
        nameLabelElement.value = '';
        contentLabelElement.value = '';
    })
    refreshElement.addEventListener('click' , () => {
        messageAreaElement.textContent = '';
        fetch(messageUrl)
        .then(res => res.json())
        .then(data => Object.values(data)
                        .forEach(message => {
                            if(message == data[0]){
                                messageAreaElement.textContent += `${message.author}: ${message.content}`
                            }else{
                                messageAreaElement.textContent += `\n${message.author}: ${message.content}`
                            }
                        })
                    )
        })
    }
    


attachEvents();