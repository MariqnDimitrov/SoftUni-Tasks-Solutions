function solve(password){
    isValid = true
    if (password.length < 6 || password.length > 10){
        isValid = false
        console.log("Password must be between 6 and 10 characters")
    }
    if(/\W/gm.test(password)){
        isValid = false
        console.log("Password must consist only of letters and digits")
    }
    if(!/\d{2,}/gm.test(password)){
        isValid = false
        console.log("Password must have at least 2 digits")
    }
    if(isValid){
        console.log("Password is valid")
    }
}
solve('MyPass123')