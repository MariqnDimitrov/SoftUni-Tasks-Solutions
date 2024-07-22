function solve(input){
    const movies = [];
    for (const row of input) {
        const addMovieCommand = 'addMovie';
        const directedByCommand = 'directedBy';
        const onDateCommand = 'onDate';
        if(row.includes(addMovieCommand)){
            const movieName = row.substring(addMovieCommand.length + 1)
            const movieObj = {
                name: movieName,
            };
            movies.push(movieObj)
        }else if(row.includes(directedByCommand)){
            const [movieName, movieDirector] = row.split(` ${directedByCommand} `)
            const searchedMovie = movies.find(movie => movie.name === movieName)
            if(searchedMovie){
                searchedMovie.director = movieDirector;
            }
        }else if(row.includes(onDateCommand)){
            const [movieName, movieData] = row.split(` ${onDateCommand} `)
            const searchedMovie = movies.find(movie => movie.name === movieName)
            if(searchedMovie){
                searchedMovie.date = movieData;
            }

        }
        
        
    }
    movies
        .filter(movie => movie.date && movie.director)
        .forEach(movie => console.log(JSON.stringify(movie)))
    

}
solve([
    'addMovie Fast and Furious',
    'addMovie Godfather',
    'Inception directedBy Christopher Nolan',
    'Godfather directedBy Francis Ford Coppola',
    'Godfather onDate 29.07.2018',
    'Fast and Furious onDate 30.07.2018',
    'Batman onDate 01.08.2018',
    'Fast and Furious directedBy Rob Cohen'
    ]
    )