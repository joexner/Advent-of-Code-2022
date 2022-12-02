from locale import atoi

filename = 'Day 2 input.txt'
score = 0
with open(filename) as file:
    for line in file:
        opponent_move = line[0]
        my_move = line[2]
        match my_move:
            case 'X':
                score += 1
                match opponent_move:
                    case 'A':
                        score += 3
                    case 'B':
                        score += 0
                    case 'C':
                        score += 6
            case 'Y':
                score += 2
                match opponent_move:
                    case 'A':
                        score += 6
                    case 'B':
                        score += 3
                    case 'C':
                        score += 0
            case 'Z':
                score += 3
                match opponent_move:
                    case 'A':
                        score += 0
                    case 'B':
                        score += 6
                    case 'C':
                        score += 3
    print(score)
