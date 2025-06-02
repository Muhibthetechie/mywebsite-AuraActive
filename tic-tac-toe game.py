theboard = {'7':'','8':'','9':'','6':'','5':'','4':'','3':'','2':'','1':''}
board_keys = []
for key in theboard:
    board_keys.append(key)

def printBoard(board):
    print(board['7']  + '|' + board['8']  + '|' + board['9'] )
    print('-+-+-')
    print(board['4']  + '|' + board['5']  + '|' + board['6'] )
    print('-+-+-')
    print(board['1']  + '|' + board['2']  + '|' + board['3'] )


def game():
    turn = 'x'
    count =0

    for i in range(10):
        printBoard(theboard)
        print("This is your turn" + turn + "Move to which place?")
        move = input()

        if theboard[move] == '':
            theboard[move] = turn
            count+=1
        else:
            print("The place is already filled.\n move to which place?")
            continue
        if count>= 5:
            if theboard['7'] == theboard['8'] == theboard['9'] !='':
                printBoard(theboard)
                print("\nGame over\n")
                print("*****" + turn + " won *****")
                break
            elif theboard['4'] == theboard['5'] == theboard['6'] !='':
                printBoard(theboard)
                print("\nGame over\n")
                print("*****" + turn + " won *****")
                break
            elif theboard['1'] == theboard['2'] == theboard['3'] !='':
                printBoard(theboard)
                print("\nGame over\n")
                print("*****" + turn + " won *****")
                break
            elif theboard['1'] == theboard['4'] == theboard['7'] !='':
                printBoard(theboard)
                print("\nGame over\n")
                print("*****" + turn + " won *****")
                break
            elif theboard['2'] == theboard['5'] == theboard['8'] !='':
                printBoard(theboard)
                print("\nGame over\n")
                print("*****" + turn + " won *****")
                break
            elif theboard['3'] == theboard['6'] == theboard['9'] !='':
                printBoard(theboard)
                print("\nGame over\n")
                print("*****" + turn + " won *****")
                break
            elif theboard['7'] == theboard['5'] == theboard['3'] !='':
                printBoard(theboard)
                print("\nGame over\n")
                print("*****" + turn + " won *****")
                break
            elif theboard['1'] == theboard['5'] == theboard['9'] !='':
                printBoard(theboard)
                print("\nGame over\n")
                print("*****" + turn + " won *****")
                break

            if count == 9:
                print("\nGame over\n")
                print("Its a tie!!!")

            if turn == 'X':
                turn = 'O'
            else:
                turn = 'X'
        
        restart = input("Do you want to play again? (y/n)")
        if restart == "y" or restart == "Y":
            for key in board_keys:
                theboard[key] = ""
                game()

if __name__=="__main__":
    game()