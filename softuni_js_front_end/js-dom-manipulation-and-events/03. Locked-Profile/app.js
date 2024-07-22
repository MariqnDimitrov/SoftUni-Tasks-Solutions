function lockedProfile() {
    const profileElements = document.getElementsByClassName('profile')
    Array.from(profileElements).forEach(profile => {
        const unlockedButton = profile.querySelectorAll('[type=radio][value=unlock]')
        const profileButton = profile.querySelectorAll('button')
        const userHiddenInfo = profile.querySelectorAll('div')
        profileButton[0].addEventListener('click',() => {
            if(unlockedButton[0].checked){
                if(profileButton[0].textContent === 'Show more'){
                    userHiddenInfo[0].style.display = 'block';
                    profileButton[0].textContent = 'Hide it';
                }else{
                    userHiddenInfo[0].style.display = 'none';
                    profileButton[0].textContent = 'Show more';
                }  
            }
        })  
    })
}