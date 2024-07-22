function solve() {
   document.querySelector('#btnSend').addEventListener('click', onClick);
   function onClick () {
      const restaurantInfo = []
      const inputElement = document.querySelectorAll('#inputs textarea')
      const input = JSON.parse(inputElement[0].value)
      for (const restaurant of input) {
         const [name, employeesInfo] = restaurant.split(' - ')
         const employees = employeesInfo
            .split(', ')
            .map(employee => employee.split(' '))
         console.log(employees)
         const salaries = employees.map(employee => {return Number(employee[1])})
         const bestSalary = Math.max(...salaries)
         const avgSalary = salaries.reduce((result, number) => result += number, 0) / salaries.length
           
            const restaurantObj = {
               name: name,
               employees: employees,
               bestSalary: bestSalary,
               avgSalary: avgSalary,
            }
            if(name === restaurantInfo.find(name).name){
               const currRestaurant = restaurantInfo.find(name)
               currRestaurant.employees.push(employees)
               const updatedBestSalary = Math.max(currRestaurant.bestSalary, bestSalary)
               const updatedAvgSalary = (currRestaurant.avgSalary + avgSalary) / (currRestaurant.employees.length / 2 + salaries.length)
            }else{
               restaurantInfo.push(restaurantObj)
            }
      }
      restaurantInfo.sort((a,b) => b.avgSalary - a.avgSalary)
      const bestRestaurant = restaurantInfo[0]
      console.log(bestRestaurant)
   }
}