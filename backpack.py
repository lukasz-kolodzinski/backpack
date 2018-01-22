#Simple two-players game. Player has to guess what is hidden in his mate's backpack.

players = []
for x in range(2):
    players.append({
        'user':'',
        'points':0,
        'backpack':[]
    })
    players[x]['user'] = input('Provide name for player ' + str(x + 1) + ': ')
    print('Enter 4 things that you are going to hide into backpack:')
    for y in range(4):
        backpack_items = input('an item name: ')
        players[x]['backpack'].append(backpack_items)

print(players)

