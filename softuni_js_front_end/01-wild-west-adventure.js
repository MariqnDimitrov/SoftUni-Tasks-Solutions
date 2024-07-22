function solve(input){
    const heroes = []
    const charNumber = Number(input.shift())
    for(let i = 0; i < charNumber; i++){
        const [heroName, heroHealth, heroBullets] = input[i].split(' ')
        const hero = {
            name: heroName,
            health: Number(heroHealth),
            bullets: Number(heroBullets),
        }
        heroes.push(hero)
    }
    for(let j = charNumber; j < input.length; j++){
        if(input[j] === 'Ride Off Into Sunset'){
            break;
        }
        const commands = input[j].split(' - ')
        if(commands.includes('FireShot')){
            const charName = commands[1]
            const targetName = commands[2]
            fireShot(charName,targetName)
        }else if(commands.includes('TakeHit')){
            const charName = commands[1]
            const damage = commands[2]
            const attacker = commands[3]
            takeHit(charName, damage, attacker)
        }else if(commands.includes('Reload')){
            const charName = commands[1]
            reload(charName)
        }else if(commands.includes('PatchUp')){
            const charName = commands[1]
            const amount = commands[2]
            patchUp(charName, amount)
        }
    }
    heroes.forEach(hero => console.log(`${hero.name}\n HP: ${hero.health}\n Bullets: ${hero.bullets}`));
    function fireShot(name, target){
        const heroObj = heroes.find(()=>{
            for (const hero of heroes) {
                if(name === hero.name){
                    return hero
                }
            }
        })
        if(heroObj.bullets > 0){
            heroObj.bullets -= 1
            console.log(`${heroObj.name} has successfully hit ${target} and now has ${heroObj.bullets} bullets!`)
        }else{
            console.log(`${heroObj.name} doesn't have enough bullets to shoot at ${target}!`)
        }
    }
    function takeHit(name, damage, attacker){
        const heroObj = heroes.find(()=>{
            for (const hero of heroes) {
                if(name === hero.name){
                    return hero
                }
            }
        })
        heroObj.health -= Number(damage)
        if(heroObj.health > 0){
            console.log(`${heroObj.name} took a hit for ${damage} HP from ${attacker} and now has ${heroObj.health} HP!`)
        }else{
            for(let k = 0; k < heroes.length; k++){
                if(heroes[k].name === heroObj.name){
                    heroes.splice(k, 1)
                }
            }
            console.log(`${heroObj.name} was gunned down by ${attacker}!`)
        }
    }
    function reload(name){
        const heroObj = heroes.find(()=>{
            for (const hero of heroes) {
                if(name === hero.name){
                    return hero
                }
            }
        })
        if(heroObj){
            if(heroObj.bullets < 6){
                const reloadedBullets = 6 - heroObj.bullets;
                heroObj.bullets = 6
                console.log(`${heroObj.name} reloaded ${reloadedBullets} bullets!`)
            }else{
                console.log(`${heroObj.name}'s pistol is fully loaded!`)
            }
        }
       
    }
    function patchUp(name, amount){
        const heroObj = heroes.find(()=>{
            for (const hero of heroes) {
                if(name === hero.name){
                    return hero
                }
            }
        })
        if(heroObj.health === 100){
            console.log(`${heroObj.name} is in full health!`)
        }else{
            const heroHealth = heroObj.health + Number(amount)
            if(heroHealth > 100){
                const overHeal = Math.abs(100 - heroHealth)
                const amountRecovered = Number(amount) - overHeal
                heroObj.health = 100
                console.log(`${heroObj.name} patched up and recovered ${amountRecovered} HP!`)
            }else{
                heroObj.health += Number(amount)
                console.log(`${heroObj.name} patched up and recovered ${amount} HP!`)
            }
    }

}
}
solve((["2",
"Gus 100 4",
"Walt 100 5",
"FireShot - Gus - Bandit",
"TakeHit - Walt - 100 - Bandit",
"Reload - Gus",
"Ride Off Into Sunset"])
)
