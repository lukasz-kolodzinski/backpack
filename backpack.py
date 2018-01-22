#Simple two-players game. Player has to guess what is hidden in his mate's backpack.

players = []
for x in range(2):
    players.append({
        'user':'',
        'points':0,
        'backpack':[]
    })
