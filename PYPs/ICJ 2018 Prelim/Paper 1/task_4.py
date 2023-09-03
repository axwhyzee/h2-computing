TEN = 'X'
STRIKE = TEN


def pins(throw: str):
    if throw == TEN:
        return 10
    return int(throw)


def bowling_score(throws: str):
    def bowling_score_helper(throws: str, frame_num: int):
        if frame_num == 10 and len(throws) == 2:
            return sum([
                pins(throws[0]), 
                pins(throws[1])
            ])
        
        if frame_num == 10 and len(throws) == 3:
            return sum([
                pins(throws[0]), 
                pins(throws[1]), 
                pins(throws[2])
            ])
    
        if throws[0] == STRIKE:
            frame_score = 10 + sum([
                pins(throws[1]),
                pins(throws[2])
            ])
            return frame_score + bowling_score_helper(throws[1:], frame_num+1)
        
        frame_score = sum([
            pins(throws[0]), 
            pins(throws[1])
        ])

        if frame_score == 10:
            return 10 + pins(throws[2]) + bowling_score_helper(throws[2:], frame_num+1)

        return frame_score + bowling_score_helper(throws[2:], frame_num+1)
    
    return bowling_score_helper(throws, 1)


SCORES_FILEPATH = 'SCORES.txt'


def bubble_sort(arr):
    n = len(arr)

    for i in range(n):
        swapped = False

        # optimization 1
        # --------------
        # at the end of each iteration, the next smallest number will be "bubbled" to the end of the arr
        # hence, we reduce the search range by 1 at the end of each iteration by minusing i 
        
        for j in range(n-i-1):
            if arr[j][2] < arr[j+1][2]:
                arr[j], arr[j+1] = arr[j+1], arr[j]

                # optimization 2
                # --------------
                # if no swaps have been made in the current round, this means that the arr is sorted already
                
                swapped = True

        if not swapped:
            return
            

def main():
    res = []
    with open(SCORES_FILEPATH, 'r') as f:
        for line in f.readlines():
            num, country, *scores = line.split()
            res.append([
                num, 
                country, 
                sum(list(map(lambda throws:bowling_score(throws), scores)))
            ])

    bubble_sort(res)

    print('Official Results\n')
    print('Position     Register Number     Country     Total Score')
    for i, row in enumerate(res):
        print(f'{i+1:<13}{row[0]:<20}{row[1]:<12}{row[2]}')


################
#   test 4.1   #
################

assert bowling_score('X737291XXX2364733') == 168
assert bowling_score('0580X05X6405819150') == 97
assert bowling_score('X2815X91X365452X0X') == 141
assert bowling_score("91739182X90X90X81") == 158
assert bowling_score('91739182X90X90X82X') == 170


################
#   test 4.3   #
################

main()