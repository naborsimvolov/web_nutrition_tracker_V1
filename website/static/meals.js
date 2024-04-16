function deleteMeal(mealId) {
    fetch(`/delete-meal/${mealId}`, {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
            'Accept': 'application/json'
        },
        body: JSON.stringify({ mealId: mealId })
    })
    .then(response => {
        if (!response.ok) {
            throw new Error(`HTTP error! Status: ${response.status}`);
        }
        return response.json();
    })
    .then(data => {
        console.log(data.message);
        window.location.reload();
    })
    .catch(error => {
        console.error('Error:', error);
    });
}
function addMeal() {
    const mealName = document.getElementById('mealName').value;
    const carbs = document.getElementById('carbs').value;
    const proteins = document.getElementById('proteins').value;
    const fats = document.getElementById('fats').value;


    const mealData = {
        mealName: mealName,
        carbs: carbs,
        proteins: proteins,
        fats: fats
    };

    fetch('/add-meal', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify(mealData)
    })
    .then(response => {
        if (!response.ok) {
            throw new Error('Network response was not OK');
        }
        return response.json();
    })
    .then(data => {
        console.log('Success:', data);

        window.location.reload();
    })
    .catch(error => {
        console.error('Error:', error);
    });
}
