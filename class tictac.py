class player:

    def __init__(self, name, choice = ""):
        self.player = name
        self.choice = choice

    def get_name(self):
        return self.player

    def get_choice(self):
        return self.choice

    def set_choice(self, choice):
        self.choice = choice

    def has_choice(self):
        return self.choice != None



class Tictactoe:

    def __init__(self, player = None):
        self.grid = ["" for i in range(9)]
        self.player = player
        self.win_comb = [0,1,2],[3,4,5],[6,7,8],[0,4,8],[2,4,6],[0,3,6],[1,4,7],[2,5,8]
        self.moves = 9

    
    def printgrid(self):
        print("\n")
        print("\t     |     |")
        print("\t  {}  |  {}  |  {}".format(self.grid[0],self.grid[1],self.grid[2]))
        print('\t_____|_____|_____')
    
        print("\t     |     |")
        print("\t  {}  |  {}  |  {}".format(self.grid[3],self.grid[4],self.grid[5]))
        print('\t_____|_____|_____')
    
        print("\t     |     |")
    
        print("\t  {}  |  {}  |  {}".format(self.grid[6],self.grid[7],self.grid[8]))
        print("\t     |     |")
        print("\n")


    def check(self):
        moves = 9
        winner = ""
        while 0 <= moves:
            for list in self.win_comb:
                x_count, o_count = 0, 0
                for i in list:
                    if self.grid[i] == "X": x_count += 1
                    
                    if self.grid[i] == "O": o_count += 1

                    if x_count == 3:
                        winner = "X"
                        break

                    if o_count == 3:
                        winner = "O"
                        break
            moves -= 1
        print(winner)
        return winner


    def valid_place(self, user_input):
        return True if self.grid[user_input] == "" else False

    
    def place(self,user_input,value):
        if self.valid_place(user_input):
            self.grid[user_input] = value
        else:
            print("Spot already taken!!!!")
            self.moves += 1

    
    def main(self, player):
        self.player = player
        curr_val = player[0].get_choice()

        while 0 < self.moves:
            self.printgrid()
            if self.check() == self.player[0].get_choice():
                print("Winner :"+ self.player[0].get_name())
                break
            if self.check() == self.player[1].get_choice():
                print("Winner :"+ self.player[1].get_name())
                break
            try:
                try:
                    print(f"Tries: {self.moves}")
                    user_input = int(input("place 1-9 in the grid: "))
                except ValueError:
                    print("input a number")
                    continue
                if isinstance(user_input, int):
                    user_input -= 1
                    self.place(user_input, curr_val)
                    if curr_val == "X": curr_val = "O"
                    else: curr_val = "X"
                    self.moves -= 1
                else:
                    raise ValueError
            except IndexError or ValueError:
                print(" Input number : less then or equal to 9")
        count = 0
        for i in self.grid:
            if i == "X":
                count += 1
            
            if i == "O":
                count += 1

        if count == len(self.grid):
            print("Draw")

        return


    def get_move(self):
        return self.moves

if __name__ == "__main__":
    game = Tictactoe()
    players = []
    for i in range(2):
        name = input("Name:")
        players.append(player(name)) 

    while True:
        try:
            user_input = input(f"{players[0].get_name()} Chosse between 'X' or 'O' !\n").upper()
            if user_input not in ["X","O"]:
                raise ValueError
            else:
                players[0].set_choice(user_input)
                if user_input == "X":
                    players[1].set_choice("O")
                    break
                else:
                    players[1].set_choice("X")
                    break
        except ValueError:
            print("Wrong input!!")

    print(""+players[0].get_name()+" :"+players[0].get_choice())
    print(""+players[1].get_name()+" :"+players[1].get_choice())
    game.main(players)





    


    





