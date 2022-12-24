import replit

def secretAuction():
    auction = []
    buyers = {}
    while True:
        replit.clear()
        name = input('What\'s your name? ')
        bid = input('What\'s your bid? $')
        buyers['Name'] = name
        buyers['Bid'] = bid
        auction.append(buyers.copy())
        question = input('Are there any other bidders? Type "yes" or "no": ')
        if question == 'no':
            break
    return auction

def checkWinner(rank):
    winner = []
    max = 0
    for i in rank:
        bid = int(i.get('Bid'))
        if max < bid:
            max = bid
            winner.clear()
            winner.append(i.get('Name'))
            winner.append(i.get('Bid'))
    return 'Winner is ' + winner[0] + ' with a bid of $' + winner[1]