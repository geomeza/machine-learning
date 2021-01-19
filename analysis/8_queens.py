import random

def show_board(locations):
    board = [[] for _ in range(8)]
    for row in board:
        for i in range(8):
            row.append('.')
    for location in locations:
        board[location[0]][location[1]] = str(locations.index(location))
    for row in board:
         row_string = '  '.join(row)
         print(row_string)

def calc_cost(locations):
    doubled = []
    for i in range(len(locations)):
        for j in range(i + 1, len(locations)):
            pair = [locations[i], locations[j]]
            if check_column(*pair) or check_row(*pair) or check_diagonal(*pair):
                if pair not in doubled and pair.reverse() not in doubled:
                    doubled.append(pair)
    return len(doubled)

def check_row(location_1, location_2):
    if location_1[0] == location_2[0]:
        return True
    else:
        return False

def check_diagonal(location_1, location_2):
    slope = (location_2[0] - location_1[0])/(location_2[1] - location_1[1])
    if slope == -1 or slope == 1:
        return True
    else:
        return False

def check_column(location_1, location_2):
    if location_1[1] == location_2[1]:
        return True
    else:
        return False

def random_optimizer(n):
    best = {'locations': None, 'cost': 250}
    for i in range(n):
        locations = [(random.randint(0,7), random.randint(0,7)) for i in range(8)]
        if calc_cost(locations) < best['cost']:
            best = {'locations': locations, 'cost': calc_cost(locations)}
    return best

def steepest_descent_optimizer(n):
    best = random_optimizer(100)
    possible_moves = [(0,1), (1,0), (0,-1), (-1,0), (1,-1), (-1,-1), (1,1), (-1,1)]
    for _ in range(n):
        all_iterations = []
        for i in range(len(best['locations'])):
            for move in possible_moves:
                new_locations = best['locations']
                test_change = (new_locations[i][0] + move[0], new_locations[i][1] + move[1])
                if in_bounds(test_change):
                    new_locations[i] = test_change
                    all_iterations.append(new_locations)
                else:
                    continue
        all_costs = [calc_cost(locations) for locations in all_iterations]
        if min(all_costs) <= best['cost']:
            best['locations'] = all_iterations[all_costs.index(min(all_costs))]
            best['cost'] = min(all_costs)
        else:
            return best
    return best      

def in_bounds(location):
    x,y = location
    if x < 0 or x > 7 or y < 0 or y > 7:
        return False
    else:
        return True

for n in [10, 50, 100, 500, 1000]:
    print('Steepest descent for', n ,'iterations:')
    result = steepest_descent_optimizer(n)
    print(result)

# while True:
#     board = steepest_descent_optimizer(1000)
#     if board['cost'] == 0:
#         print(calc_cost(board['locations']))
#         print(board)
#         break

# locations = [(0,0), (6,1), (2,2), (5,3), (4,4), (7,5), (1,6), (2,6)]
# show_board(locations)
# print(calc_cost(locations))
# for i in [10,50,100,500,1000]:
#     print('Best from',i,'combinations')
#     print(random_optimizer(i))