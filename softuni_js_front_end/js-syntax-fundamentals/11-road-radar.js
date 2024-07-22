function solve(speed, area){
    limit = 0;
    let status = '';
    switch(area){
        case 'motorway':
            limit = 130;
            break
        case 'interstate':
            limit = 90;
            break
        case 'city':
            limit = 50;
            break
        case 'residential':
            limit = 20
            break
    }
    speeding = speed - limit
    if(speeding <= 0){
        console.log(`Driving ${speed} km/h in a ${limit} zone`)
    }else if(speeding <= 20){
        status = 'speeding'
        console.log(`The speed is ${speeding} km/h faster than the allowed speed of ${limit} - ${status}`)
    }else if(speeding <= 40){
        status = 'excessive speeding'
        console.log(`The speed is ${speeding} km/h faster than the allowed speed of ${limit} - ${status}`)
    }else{
        status = 'reckless driving'
        console.log(`The speed is ${speeding} km/h faster than the allowed speed of ${limit} - ${status}`)
    }
}
solve(40, 'city')
solve(21, 'residential')