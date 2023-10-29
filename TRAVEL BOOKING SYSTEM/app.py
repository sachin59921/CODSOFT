from flask import Flask, request, jsonify
import datetime

app = Flask(__name)

# Define a list of rooms with their availability dates
rooms = [
    {'id': 1, 'name': 'Standard Room', 'available_dates': [datetime.date(2023, 3, 1), datetime.date(2023, 3, 2)]},
    {'id': 2, 'name': 'Deluxe Room', 'available_dates': [datetime.date(2023, 3, 1), datetime.date(2023, 3, 2), datetime.date(2023, 3, 3)]},
    {'id': 3, 'name': 'Suite', 'available_dates': [datetime.date(2023, 3, 2), datetime.date(2023, 3, 3)]},
]

# Function to search for available rooms within a date range
def search_available_rooms(check_in_date, check_out_date):
    available_rooms = []
    for room in rooms:
        available_dates = room['available_dates']
        if all(date >= check_in_date and date <= check_out_date for date in available_dates):
            available_rooms.append(room)
    return available_rooms

@app.route('/search', methods=['POST'])
def search_rooms():
    data = request.json
    check_in_date = datetime.datetime.strptime(data['check_in_date'], '%Y-%m-%d').date()
    check_out_date = datetime.datetime.strptime(data['check_out_date'], '%Y-%m-%d').date()
    
    available_rooms = search_available_rooms(check_in_date, check_out_date)

    if not available_rooms:
        return jsonify({'error': 'No available rooms for the selected dates'}), 404

    return jsonify(available_rooms)

@app.route('/book/<int:room_id>', methods=['POST'])
def book_room(room_id):
    room = next((r for r in rooms if r['id'] == room_id), None)

    if room is None:
        return jsonify({'error': 'Room not found'}), 404

    available_dates = room['available_dates']
    data = request.json
    check_in_date = datetime.datetime.strptime(data['check_in_date'], '%Y-%m-%d').date()
    check_out_date = datetime.datetime.strptime(data['check_out_date'], '%Y-%m-%d').date()

    if check_in_date not in available_dates or check_out_date not in available_dates:
        return jsonify({'error': 'Room is not available for the selected dates'}), 400

    # In a real application, you would handle the booking logic here,
    # such as updating the database or confirming the booking.

    # For this demonstration, we'll remove the available dates.
    available_dates.remove(check_in_date)
    available_dates.remove(check_out_date)

    return jsonify({'message': 'Booking successful'})

if __name__ == '__main__':
    app.run()
