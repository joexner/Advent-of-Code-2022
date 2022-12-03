from locale import atoi

filename = 'Day 2 input.txt'
score = 0
with open(filename) as file:
    for line in file:
        opponent_move = line[0]
        my_move = line[2]
        match my_move:
            case 'X':
                score += 0
                match opponent_move:
                    case 'A':
                        score += 3
                    case 'B':
                        score += 1
                    case 'C':
                        score += 2
            case 'Y':
                score += 3
                match opponent_move:
                    case 'A':
                        score += 1
                    case 'B':
                        score += 2
                    case 'C':
                        score += 3
            case 'Z':
                score += 6
                match opponent_move:
                    case 'A':
                        score += 2
                    case 'B':
                        score += 3
                    case 'C':
                        score += 1
    print(score)
