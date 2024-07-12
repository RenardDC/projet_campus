def win_condition(self,liste):
    victoire = False
    
    for col, row in liste:
        if liste[0][0] = 'X' and liste[0][1] = 'X' and liste[0][2] = 'X' or liste[0][0] = 'O' and liste[0][1] = 'O' and liste[0][2] = 'O':
            victoire = True
        elif liste[1][0] = 'X' and liste[1][1] = 'X' and liste[1][2] = 'X' or liste[1][0] = 'O' and liste[1][1] = 'O' and liste[1][2] = 'O':
            victoire = True
        elif liste[2][0] = 'X' and liste[2][1] = 'X' and liste[2][2] = 'X' or liste[2][0] = 'O' and liste[2][1] = 'O' and liste[2][2] = 'O':
            victoire = True
        elif liste[0][0] = 'X' and liste[1][0] = 'X' and liste[2][0] = 'X' or liste[0][0] = 'O' and liste[1][0] = 'O' and liste[2][0] = 'O':
            victoire = True
        elif liste[0][1] = 'X' and liste[1][1] = 'X' and liste[2][1] = 'X' or liste[0][1] = 'O' and liste[1][1] = 'O' and liste[2][1] = 'O':
            victoire = True
        elif liste[0][2] = 'X' and liste[1][2] = 'X' and liste[2][2] = 'X' or liste[0][2] = 'O' and liste[1][2] = 'O' and liste[2][2] = 'O':
            victoire = True
        elif liste[0][0] = 'X' and liste[1][1] = 'X' and liste[2][2] = 'X' or liste[0][0] = 'O' and liste[1][1] = 'O' and liste[2][2] = 'O':
            victoire = True
        elif liste[2][0] = 'X' and liste[1][1] = 'X' and liste[0][2] = 'X' or liste[2][0] = 'O' and liste[1][1] = 'O' and liste[0][2] = 'O':
            victoire = True
        else:
            print('Match nul')
