import xmlrpc.server
import random

def round(opponent1, opponent2):
    if(opponent1.lower() == "rock"):
        if(opponent2.lower() == "rock"):
            return("Drawn! Opponent chose: " + opponent2)
        elif(opponent2.lower() == "paper"):
            return("Lost! Opponent chose: " + opponent2)
        else:
            return("Won! Opponent chose: " + opponent2)
    elif(opponent1.lower() == "paper"):
        if(opponent2.lower() == "paper"):
            return("Drawn! Opponent chose: " + opponent2)
        elif(opponent2.lower() == "scissors"):
            return("Lost! Opponent chose: " + opponent2)
        else:
            return("Won! Opponent chose: " + opponent2)
    elif(opponent1.lower() == "scissors"):
        if(opponent2.lower() == "scissors"):
            return("Drawn! Opponent chose: " + opponent2)
        elif(opponent2.lower() == "rock"):
            return("Lost! Opponent chose: " + opponent2)
        else:
            return("Won! Opponent chose: " + opponent2)
    else:
        return("Give input of Rock, Paper or Scissors")

class Game:
    storedGames = []

    def npcRound(self, clientGame):
        npcGames = ["Rock", "Paper", "Scissors"]
        npc = random.choice(npcGames)
        return round(clientGame, npc)
    
    def client1Round(self, clientGame):
        client2Game = self.storedGames[1]
        self.resetStoredGames = []
        return round(clientGame, client2Game)
        
    def client2Round(self, client2Game):
        clientGame = self.storedGames[0]
        self.storedGames.append(client2Game)
        return round(client2Game, clientGame)

    def registerGame(self, game):
        if(len(self.storedGames) == 0):
            self.storedGames.append(game)
            return True
        else:
            return False

    def storageCount(self):
        return len(self.storedGames)

port = 8000
server = xmlrpc.server.SimpleXMLRPCServer(("localhost", port))
server.register_instance(Game())

print("Server running on port " + str(port) + "...")

try:
    server.serve_forever()
finally:
    server.server_close()
