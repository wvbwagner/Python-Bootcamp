import Auction_Functions

auction = Auction_Functions.secretAuction()
winner = Auction_Functions.checkWinner(auction)
print(f'Winner is {winner[0]} with a bid of ${winner[1]}')