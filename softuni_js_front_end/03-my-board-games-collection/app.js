const loadGamesButton = document.getElementById('load-games')
loadGamesButton.addEventListener('click', async ()=> {
    const loadGames = await fetch('http://localhost:3030/jsonstore/games/')
    const games = await loadGames.json()
    const gamesArr = Object.values(games)
    Array.from(gamesArr).forEach(game => {
        const divBoardGame = document.createElement('div')
        divBoardGame.className = 'board-game'
        const divContent = document.createElement('div')
        divContent.className = 'content'
        const divButtons = document.createElement('div')
        divButtons.className = 'buttons-container'
        const changeButton = document.createElement('button')
        changeButton.className = 'change-btn'
        changeButton.textContent = 'Change'
        const deleteButton = document.createElement('button')
        deleteButton.className = 'delete-btn'
        deleteButton.textContent = 'Delete'
        divButtons.appendChild(changeButton)
        divButtons.appendChild(deleteButton)
        const gamesListDivElement = document.getElementById('games-list')
        const pNameElement = document.createElement('p')
        const pTypeElement = document.createElement('p')
        const pMaxPlayers = document.createElement('p')
        
        pNameElement.textContent = game.name
        pTypeElement.textContent = game.type
        pMaxPlayers.textContent = game.players
        divContent.appendChild(pNameElement)
        divContent.appendChild(pTypeElement)
        divContent.appendChild(pMaxPlayers)
        divBoardGame.appendChild(divContent)
        divBoardGame.appendChild(divButtons)
        gamesListDivElement.appendChild(divBoardGame)

        
    });
})
