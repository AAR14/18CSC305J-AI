num_rooms = int(input('Enter the number of rooms: '))
rooms = []
for i in range(num_rooms):
    status = input(f'Enter the status of room {i+1} (clean/dirty): ')
    rooms.append(status)

# clean the rooms
for i, room in enumerate(rooms):
    if room== 'clean':
        print(f'the room {i+1} is clean moving to the next room')
    if room == 'dirty':
        print(f'Cleaning room {i+1}... and moving to the next room')
        rooms[i] = 'clean'
print('All rooms are now clean.')
