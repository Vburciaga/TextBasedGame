# A dictionary for the simplified dragon text game
# The dictionary links a room to other rooms.
rooms = {
    'Coast': {'West': 'Stream'},
    'Stream': {'North': 'Calm Lands', 'East': 'Coast', 'West': 'Forest', 'item': 'Bow'},
    'Forest': {'North': 'Cliff', 'East': 'Stream', 'item': 'Armor'},
    'Cliff': {'East': 'Calm Lands', 'South': 'Forest', 'item': 'Gauntlets'},
    'Calm Lands': {'North': 'Swamp', 'East': 'Waterfall', 'South': 'Stream', 'West': 'Cliff', 'item': 'Rusty Shield'},
    'Swamp': {'East': 'Bone Yard', 'South': 'Calm Lands', 'item': 'Sword'},
    'Bone Yard': {'West': 'Swamp', 'item': 'Legendary Mirror'},
    'Waterfall': {'North': 'Hidden Cave', 'West': 'Calm Lands'},
    'Hidden Cave': {'South': 'Waterfall', 'item': 'Medusa'}
}

# direction options
current_room = 'Coast'
directions = ['North', 'South', 'East', 'West']

# players inventory
inventory = []


# add item to inventory and remove from room
def get_item():
    if (rooms[current_room]['item']) not in inventory:
        print('Would you like to pick up the item? \n')
        pick_up = input('')
        if pick_up == 'yes':
            inventory.append((rooms[current_room]['item']))
            print('Item was retrieved and added to your inventory.')

        else:
            print('You left the item behind')


# instructions for game
def introduction():
    print('Young Warrior!')
    print('You must avenge your village that was turned to stone by a Mythological creature. ')
    print('You have arrived at the rumored island where you must explore to find the creature.')
    print('As travel through the Island, collect all 6 items to help slay the creature or become the next victim!')
    print('You will Begin at the Coast.')
    print('Take caution as your travel through the hazardous conditions.... ')
    print("Move Commands: You can move north, east, south, or west by typing 'go____'")
    print("Items Commands: You can pick up items or leave them behind by answering 'yes' or 'no'")


# player status
def player_status():
    message = ('You are arriving at the {}.'.format(current_room))
    print('_' * len(message))
    print('\nYour current inventory: {}'.format(inventory))
    print(message)
    if "item" in rooms[current_room]:
        print('You see a {} on the ground.'.format(rooms[current_room]['item']))
    print('_' * len(message))


# single word direction input ('North', etc)
def get_direction_1():
    user_command = input('Please enter a direction:\n>').title()
    for direction in directions:
        for word in user_command.split():
            if word == direction:
                user_command = word
                return user_command


# double word direction input (go north, etc)
def get_direction_2():
    user_command = input('Please enter a direction:\n>').split()
    if len(user_command) == 1:
        return user_command[0].title()
    if len(user_command) == 2:
        return user_command[1].title()


introduction()

while True:
    if len(inventory) == 6:
        print('Congratulations! You collected all the items, you encountered Medusa and defeated the creature!')
        print('Return back home young warrior.')
        print('Thanks for playing the game. Hope you enjoyed it.')
        exit()
    else:
        while current_room == 'Coast':
            player_status()
            user_command = get_direction_1()
            if user_command not in rooms[current_room]:
                print('Invalid Command.')
            elif user_command == 'West':
                current_room = rooms[current_room][user_command]

        while current_room == 'Stream':
            player_status()
            get_item()
            user_command = get_direction_1()
            if user_command.title() not in rooms[current_room]:
                print('Invalid Command.')
            elif user_command == 'North':
                current_room = rooms[current_room][user_command]
            elif user_command == 'East':
                current_room = rooms[current_room][user_command]
            elif user_command == 'West':
                current_room = rooms[current_room][user_command]

        while current_room == 'Forest':
            player_status()
            get_item()
            user_command = get_direction_1()
            if user_command.title() not in rooms[current_room]:
                print('Invalid Command.')
            elif user_command == 'North':
                current_room = rooms[current_room][user_command]
            elif user_command == 'East':
                current_room = rooms[current_room][user_command]

        while current_room == 'Cliff':
            player_status()
            get_item()
            user_command = get_direction_1()
            if user_command.title() not in rooms[current_room]:
                print('Invalid Command.')
            elif user_command == 'East':
                current_room = rooms[current_room][user_command]
            elif user_command == 'South':
                current_room = rooms[current_room][user_command]

        while current_room == 'Calm Lands':
            player_status()
            get_item()
            user_command = get_direction_1()
            if user_command.title() not in rooms[current_room]:
                print('Invalid Command.')
            elif user_command == 'North':
                current_room = rooms[current_room][user_command]
            elif user_command == 'East':
                current_room = rooms[current_room][user_command]
            elif user_command == 'South':
                current_room = rooms[current_room][user_command]
            elif user_command == 'West':
                current_room = rooms[current_room][user_command]

        while current_room == 'Swamp':
            player_status()
            get_item()
            user_command = get_direction_1()
            if user_command.title() not in rooms[current_room]:
                print('Invalid Command.')
            elif user_command == 'East':
                current_room = rooms[current_room][user_command]
            elif user_command == 'South':
                current_room = rooms[current_room][user_command]

        while current_room == 'Bone Yard':
            player_status()
            get_item()
            user_command = get_direction_1()
            if user_command.title() not in rooms[current_room]:
                print('Invalid Command.')
            elif user_command == 'West':
                current_room = rooms[current_room][user_command]

        while current_room == 'Waterfall':
            player_status()
            user_command = get_direction_1()
            if user_command.title() not in rooms[current_room]:
                print('Invalid Command.')
            elif user_command == 'North':
                current_room = rooms[current_room][user_command]
            elif user_command == 'West':
                current_room = rooms[current_room][user_command]

        while current_room == 'Hidden Cave':
            print('You confronted Medusa without your items and have been turned to stone....Game Over.....')
            print('Thanks for playing the game. Hope you enjoyed it.')
            exit()
