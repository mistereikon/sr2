document.addEventListener('DOMContentLoaded', function () {
    updateVacancyList();
});

function createVacancy() {
    const form = document.getElementById("createVacancyForm");
    const formData = new FormData(form);

    fetch('/api/vacancies', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
                'Authorization': 'Bearer YOUR_ACCESS_TOKEN',
            },
            body: JSON.stringify(Object.fromEntries(formData)),
        })
        .then(response => response.json())
        .then(data => {
            alert('Vacancy created successfully!');
            updateVacancyList();
            console.log(data);
        })
        .catch((error) => {
            console.error('Error:', error);
        });
}

function updateVacancyList() {
    fetch('/api/vacancies')
        .then(response => response.json())
        .then(data => {
            const vacancyList = document.getElementById("vacancyList");
            vacancyList.innerHTML = "";
            data.forEach(vacancy => {
                const listItem = document.createElement("li");
                listItem.innerHTML = `<strong>${vacancy.title}</strong> - ${vacancy.location} - ${vacancy.salary} 
                                      <button onclick="updateVacancy(${vacancy.id})">Update</button> 
                                      <button onclick="deleteVacancy(${vacancy.id})">Delete</button>`;
                vacancyList.appendChild(listItem);
            });
        })
        .catch((error) => {
            console.error('Error:', error);
        });
}

function updateVacancy(vacancyId) {
    const newTitle = prompt("Enter new title:");
    const newLocation = prompt("Enter new location:");
    const newSalary = prompt("Enter new salary:");

    const updatedVacancy = {
        title: newTitle,
        location: newLocation,
        salary: newSalary
    };

    fetch(`/api/vacancies/${vacancyId}`, {
            method: 'PUT',
            headers: {
                'Content-Type': 'application/json',
                'Authorization': 'Bearer YOUR_ACCESS_TOKEN',
            },
            body: JSON.stringify(updatedVacancy),
        })
        .then(response => response.json())
        .then(data => {
            alert('Vacancy updated successfully!');
            updateVacancyList();
            console.log(data);
        })
        .catch((error) => {
            console.error('Error:', error);
        });
}

function deleteVacancy(vacancyId) {
    if (confirm("Are you sure you want to delete this vacancy?")) {
        fetch(`/api/vacancies/${vacancyId}`, {
                method: 'DELETE',
                headers: {
                    'Authorization': 'Bearer YOUR_ACCESS_TOKEN', 
                },
            })
            .then(response => response.json())
            .then(data => {
                alert('Vacancy deleted successfully!');
                updateVacancyList();
                console.log(data);
            })
            .catch((error) => {
                console.error('Error:', error);
            });
    }
}
