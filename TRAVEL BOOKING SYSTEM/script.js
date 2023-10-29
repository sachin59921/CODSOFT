document.getElementById('search-button').addEventListener('click', function(event) {
    event.preventDefault();

    const searchQuery = document.getElementById('search-input').value;
    const checkInDate = document.getElementById('check-in-date').value;
    const checkOutDate = document.getElementById('check-out-date').value;

    if (searchQuery === 'rooms') {
        searchRooms(checkInDate, checkOutDate);
    } else if (searchQuery === 'flights') {
        searchFlights(checkInDate, checkOutDate);
    } else if (searchQuery === 'cars') {
        searchCars(checkInDate, checkOutDate);
    }
});

function searchRooms(_checkInDate, _checkOutDate) {
    const roomResults = [
        { name: 'Standard Room', price: 80 },
        { name: 'Deluxe Room', price: 120 },
        { name: 'Suite', price: 200 }
    ];
    displaySearchResults(roomResults);
}

function searchFlights(_checkInDate, _checkOutDate) {
    const flightResults = [
        { name: 'Flight to Paris', price: 500 },
        { name: 'Flight to Tokyo', price: 800 }
    ];
    displaySearchResults(flightResults);
}

function searchCars(_checkInDate, _checkOutDate) {
    const carResults = [
        { name: 'Economy Car', price: 40 },
        { name: 'SUV', price: 80 }
    ];
    displaySearchResults(carResults);
}

function displaySearchResults(results) {
    const resultsSection = document.getElementById('results');
    resultsSection.innerHTML = '';

    if (results.length === 0) {
        resultsSection.innerHTML = '<p>No results found.</p>';
    } else {
        results.forEach(result => {
            const resultItem = document.createElement('div');
            resultItem.innerHTML = `
                <h3>${result.name}</h3>
                <p>Price: $${result.price}</p>
                <button class="book-button">Book Now</button>
            `;
            resultsSection.appendChild(resultItem);
        });
    }
}
