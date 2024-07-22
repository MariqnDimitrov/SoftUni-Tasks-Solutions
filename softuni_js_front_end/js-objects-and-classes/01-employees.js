function solve(namesArr){
    let personalInfo = {}
    for (const name of namesArr) {
        personalInfo[name] = name.length
    }
    for (const person in personalInfo) {
        console.log(`Name: ${person} -- Personal Number: ${personalInfo[person]}` )
        
    }
}
solve([
    'Silas Butler',
    'Adnaan Buckley',
    'Juan Peterson',
    'Brendan Villarreal'
    ]
    )