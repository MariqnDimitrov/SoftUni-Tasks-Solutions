function solve(data){
    const chemicalsNum = data[0];
    let chemicals = {};
    for(let i = 1; i <= chemicalsNum; i++){
        let chemical = data[i].split(' # ')
        chemicals[chemical[0]] = {'Quantity': Number(chemical[1])};
    }
    for(let j = Number(chemicalsNum) + 1; j < data.length; j++ ){
        let commands = data[j].split(' # ')
        if(commands[0] === 'End'){
            break
        }
        switch (commands[0]){
            case 'Mix':
                if(commands[1] in chemicals && commands[2] in chemicals){
                    if(chemicals[commands[1]]['Quantity'] < commands[3] || chemicals[commands[2]]['Quantity'] < commands[3]){
                            console.log(`Insufficient quantity of ${commands[1]}/${commands[2]} to mix.`)
                        }else{
                            chemicals[commands[1]]['Quantity'] -= commands[3];
                            chemicals[commands[2]]['Quantity'] -= commands[3];
                            console.log(`${commands[1]} and ${commands[2]} have been mixed. ${commands[3]} units of each were used.`)
                        }    
                }
                break
            case 'Replenish':
                if(commands[1] in chemicals){
                    if(chemicals[commands[1]]['Quantity'] + Number(commands[2]) >= 500){
                        console.log(`${commands[1]} quantity increased by ${500 - chemicals[commands[1]]['Quantity']} units, reaching maximum capacity of 500 units!`)
                        chemicals[commands[1]]['Quantity'] = 500;
                    }else{
                        chemicals[commands[1]]['Quantity'] += Number(commands[2]);
                        console.log(`${commands[1]} quantity increased by ${commands[2]} units!`)
                    }
                }else{
                    console.log(`The Chemical ${chemicals[1]} is not available in the lab.`)
                }
                break
            case 'Add Formula':
                if(commands[1] in chemicals){
                    chemicals[commands[1]] = {'Quantity': chemicals[commands[1]]['Quantity'] , 'Formula': commands[2]} 
                    console.log(`${commands[1]} has been assigned the formula ${commands[2]}.`)
                }else{
                    console.log(`The Chemical ${commands[1]} is not available in the lab.`)
                }
                break
        }
    }
    for (const key of Object.keys(chemicals)){
        if('Formula' in chemicals[key]){
            console.log(`Chemical: ${key}, Quantity: ${chemicals[key]['Quantity']}, Formula: ${chemicals[key]['Formula']}`)  
        }else{
            console.log(`Chemical: ${key}, Quantity: ${chemicals[key]['Quantity']}`)
        }
    }
}
solve([ '4',
    'Water # 200',
    'Salt # 100',
    'Acid # 50',
    'Base # 80',
    'Mix # Water # Salt # 50',
    'Replenish # Salt # 150',
    'Add Formula # Acid # H2SO4',
    'End']
  )