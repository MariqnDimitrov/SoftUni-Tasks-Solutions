function solve(group, groupType, days){
    let price = 0;
    let totalPrice = 0;
    if(groupType == 'Students'){
        switch(days){
            case 'Friday':
                price = 8.45;
                break
            case 'Saturday':
                price = 9.80;
                break
            case 'Sunday':
                price = 10.46;
                break
        }
        totalPrice = price * group
        if(group >= 30){
            totalPrice = totalPrice * 0.85
        }
    }else if(groupType == 'Business'){
        switch(days){
            case 'Friday':
                price = 10.90;
                break
            case 'Saturday':
                price = 15.60;
                break
            case 'Sunday':
                price = 16;
                break
        }
        totalPrice = price * group
        if(group >= 100){
            totalPrice = totalPrice - (price * 10);
        }
    }else if(groupType == 'Regular'){
        switch(days){
            case 'Friday':
                price = 15;
                break
            case 'Saturday':
                price = 20;
                break
            case 'Sunday':
                price = 22.50;
                break
        }
        totalPrice = price * group
        if(group >= 10 && group <= 20){
            totalPrice = totalPrice * 0.95;
        }
    }
    console.log(`Total price: ${totalPrice.toFixed(2)}`);
}
solve(30,
    "Students",
    "Sunday"
    )