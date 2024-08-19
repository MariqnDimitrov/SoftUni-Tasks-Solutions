function solve(data){
    let spell = data[0];
    let commands = data.slice(1);
    for( let command of commands){
        if(command == "End"){
            break
        }else if(command == "RemoveEven"){
            spell = spell.split('').filter(x => spell.indexOf(x) % 2 == 0).join('')
            console.log(spell)
        }else if(command.includes("TakePart")){
            command = command.split('!')
            spell = spell.slice(command[1], command[2])
            console.log(spell)
        }else if(command.includes('Reverse')){
            command = command.split('!');
            if(spell.includes(command[1])){
                spell = spell.replace(command[1], '')
                spell += command[1].split('').reverse().join('')
                console.log(spell)
            }else{
                console.log('Error');
            }   
        }
        }
        console.log(`The concealed spell is: ${spell}`)
    };
    


solve(((["hZwemtroiui5tfone1haGnanbvcaploL2u2a2n2i2m", 
    "TakePart!31!42",
    "RemoveEven",
    "Reverse!anim",
    "Reverse!sad",
    "End"])
    )
    );