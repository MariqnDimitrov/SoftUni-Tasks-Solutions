function solve(townInfo){
    let towns = []
    for (let town of townInfo) {
        [townName,latitude,longitude] = town.split(' | ');
        townObj = {town: townName, latitude:Number(latitude).toFixed(2), longitude: Number(longitude).toFixed(2)}
        towns.push(townObj)
    }
    towns.forEach(townArr => console.log(townArr))

}
solve(['Sofia | 42.696552 | 23.32601',
'Beijing | 39.913818 | 116.363625']
);