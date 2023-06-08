def read_file_input(*, filename:str):
    with open(filename, "r") as file:
        moves = file.readlines()
        # clean \n char
        moves = [ m.replace('\n','') for m in moves]
    
    return moves

def play_hand(*, player1_move: str, player2_move: str):
    if player1_move == player2_move:
        return "Draw"
    elif player1_move == "R" and player2_move == "S":
        return "Player1"
    elif player1_move == "P" and player2_move == "R":
        return "Player1"
    elif player1_move == "S" and player2_move == "P":
        return "Player1"
    else:
        return "Player2"

def write_output(*, filename:str, content:dict):
    with open(filename, "w") as file:
        file.write("Player1 wins:"+ str(content["Player1"]) +"\n")
        file.write("Player2 wins:"+ str(content["Player2"]) +"\n")
        file.write("Draws:"+ str(content["Draw"]))

if __name__ == "__main__":
    # ['R', 'S',...]
    player1_moves = read_file_input(filename="player1.txt")
    player2_moves = read_file_input(filename="player2.txt")

    if len(player1_moves) != len(player2_moves):
        raise ValueError("Mismatch in number of moves")

    sumup = {
        "Draw" : 0,
        "Player1" : 0,
        "Player2" : 0,
    }

    for index, value in enumerate(player1_moves):
        result = play_hand(player1_move=value, player2_move=player2_moves[index])

        sumup[result] = sumup[result] + 1
    
    write_output(filename="result.txt", content=sumup)
    print(sumup[result] + 1)
