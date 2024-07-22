function solve(strArray){
    const heroDataCollection = []
    for (const heroData of strArray) {
        const [heroName, heroLevel, ...items] = heroData.split(' / ')
        const heroObj = {
            name: heroName,
            level: heroLevel,
            items: items,
        }
        heroDataCollection.push(heroObj)
    }
    heroDataCollection
        .sort((a,b) => a.level - b.level)
        .forEach(hero => console.log(`Hero: ${hero.name}\nlevel => ${hero.level}\nitems => ${hero.items.join(', ')}`))
}
solve([
    'Batman / 2 / Banana, Gun',
    'Superman / 18 / Sword',
    'Poppy / 28 / Sentinel, Antara'
    ]    
    )