Grid = {'7':'','8':'','9':'',
        '4':'','5':'','6':'',
        '1':'','2':'','3':''}

print('Hello and welcome to a game of tick-tack-toe!\nPlayer X goes first, to choose a field which You want to mark, type a corresponding number as indicated on the grid below.')
print('-------')
print('|7' + '|' + '8' + '|' + '9|')
print(' -+-+-')
print('|4' + '|' + '5' + '|' + '6|')
print(' -+-+-')
print('|1' + '|' + '2' + '|' + '3|')
print('-------')


for i in range (99):
        decision = input('Please type: NEW GAME to start, or type EXIT to exit the programme:')
        if decision == 'NEW GAME':
                print('Let the GAME begin!')
                break
        elif decision == 'EXIT':
                print('Program will now terminate.')
                quit()
        if decision != 'NEW GAME' != 'EXIT':
                print('You have entered an invalid value. Please try again.')
                continue





def printgrid(Grid):
        print(Grid['7'] + ' |' + Grid['8'] + ' |' + Grid['9'])
        print('-+-+-')
        print(Grid['4'] + ' |' + Grid['5'] + ' |' + Grid['6'])
        print('-+-+-')
        print(Grid['1'] + ' |' + Grid['2'] + ' |' + Grid['3'])

def game():
        player = 'X'
        turn = 1

        for i in range (9):
                printgrid(Grid)
                move = input('It is now turn ' + str(turn) + ' player ' + player + ':')

                if Grid[move] == '':
                        Grid[move] = player

                elif Grid[move] == 'X' or 'O':
                        print('That field is already taken!')
                        continue

                if turn >= 3:
                        if Grid['7'] == Grid['8'] == Grid['9'] != '':
                                printgrid(Grid)
                                print('Congratulations ' + player + '! You have won the game!')
                                break
                        elif Grid['4'] == Grid['5'] == Grid['6'] != '':
                                printgrid(Grid)
                                print('Congratulations ' + player + '! You have won the game!')
                                break
                        elif Grid['1'] == Grid['2'] == Grid['3'] != '':
                                printgrid(Grid)
                                print('Congratulations ' + player + '! You have won the game!')
                                break
                        elif Grid['7'] == Grid['4'] == Grid['1'] != '':
                                printgrid(Grid)
                                print('Congratulations ' + player + '! You have won the game!')
                                break
                        elif Grid['8'] == Grid['5'] == Grid['2'] != '':
                                printgrid(Grid)
                                print('Congratulations ' + player + '! You have won the game!')
                                break
                        elif Grid['9'] == Grid['6'] == Grid['3'] != '':
                                printgrid(Grid)
                                print('Congratulations ' + player + '! You have won the game!')
                                break
                        elif Grid['7'] == Grid['5'] == Grid['3'] != '':
                                printgrid(Grid)
                                print('Congratulations ' + player + '! You have won the game!')
                                break
                        elif Grid['9'] == Grid['5'] == Grid['1'] != '':
                                printgrid(Grid)
                                print('Congratulations ' + player + '! You have won the game!')
                                break

                if turn == 5:
                        print('The GAME is a TIE!')


                if player == 'X':
                        player = 'O'
                else:
                        player = 'X'
                        turn += 1

game()

