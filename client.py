import xmlrpc.client
import time

proxy = xmlrpc.client.ServerProxy("http://localhost:8000")
choice = 0
timer = 0

while(choice < 1 or choice > 2): 
    choice = int(input("Choose between a NPC (1) or Player (2) opponent: "))

game = input("Choose your game (Rock, Paper or Scissors): ")

if(choice == 1):
    response = proxy.npcRound(game)
    print(response)
elif(choice == 2):
    rounds = proxy.storageCount()
    if(rounds == 0):
        if(proxy.registerGame(game)):
            while(rounds < 3 or timer >= 30):
                print("Game registered successfully, waiting for opponent...")
                rounds = proxy.storageCount()
                if(rounds == 2):
                    response = proxy.client1Round(game)
                    print(response)
                    rounds += 1
                
                time.sleep(1)
                timer += 1
                print("Timing out in: " + str(30-timer))
            if(timer >= 30):
                print("No opponent found :(")
    elif(rounds == 1):
        response = proxy.client2Round(game)
        print(response)
        rounds += 1
