function solve(currStock, orderProducts){
    let stock = {};
    for(let i = 0; i < currStock.length; i += 2){
        const product = currStock[i]
        const quantity = Number(currStock[i + 1])
        stock[product] = quantity;
    }
    for(let j = 0; j < orderProducts.length; j += 2){
        const product = orderProducts[j]
        const quantity = Number(orderProducts[j + 1])
        if(!stock[product]){
            stock[product] = 0
        }
        stock[product] += quantity
    }
    
    for (const product in stock) {
        console.log(`${product} -> ${stock[product]}`)
    }
}
solve([
    'Chips', '5', 'CocaCola', '9', 'Bananas', '14', 'Pasta', '4', 'Beer', '2'
    ],
    [
    'Flour', '44', 'Oil', '12', 'Pasta', '7', 'Tomatoes', '70', 'Bananas', '30'
    ]
    )