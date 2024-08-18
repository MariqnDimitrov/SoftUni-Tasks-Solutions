function attachEvents() {
  const submitBtnElement = document.getElementById('submit');
  const firstNameInputElement = document.querySelector('.inputs input[name="firstName"]')
  const lastNameInputElement = document.querySelector('.inputs input[name="lastName"]')
  const facultyNumberInputElement = document.querySelector('.inputs input[name="facultyNumber"]')
  const gradeInputElement = document.querySelector('.inputs input[name="grade"]')
  const tbodyElement = document.querySelector('tbody')
  const studentUrl = 'http://localhost:3030/jsonstore/collections/students'
  fetch(studentUrl)
    .then(res => res.json())
    .then(data => {Object.values(data).forEach(student => {
      createStudentTr(student)
    })
  })
  submitBtnElement.addEventListener('click', () => {
    let firstName = firstNameInputElement.value;
    let lastName = lastNameInputElement.value;
    let facultyNumber = facultyNumberInputElement.value;
    let grade = gradeInputElement.value;
    fetch(studentUrl, {
      method: "POST",
      headers:{
        "content-type": "application/json",
      },
      body:JSON.stringify({
        'firstName': firstName,
        'lastName': lastName,
        'facultyNumber': facultyNumber,
        'grade': grade,
      })
    })
    .then(data => data.json())
    .then(student => {
      Object.values(student)
      .forEach(
        createStudentTr(student)
      )
    })
  })
  function createStudentTr({firstName, lastName, facultyNumber, grade}){
    let trElement = document.createElement('tr')

    let tdFirstNameElement = document.createElement('td')
    tdFirstNameElement.textContent = firstName;

    let tdLastNameElement = document.createElement('td')
    tdLastNameElement.textContent = lastName;

    let tdFacultyNumberElement = document.createElement('td')
    tdFacultyNumberElement.textContent = facultyNumber;

    let tdGradeElement = document.createElement('td')
    tdGradeElement.textContent = grade;

    trElement.appendChild(tdFirstNameElement)
    trElement.appendChild(tdLastNameElement)
    trElement.appendChild(tdFacultyNumberElement)
    trElement.appendChild(tdGradeElement)
    tbodyElement.appendChild(trElement)
  }
}

attachEvents();