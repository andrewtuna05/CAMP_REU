import numpy as np

def get_positive_integer() :
    N = int(input("Please give positive integer N: "))

    while(N <= 0) :
        try : 
            print("Invalid entry %d" % N)
            x = int(input("Please give positive integer N: "))
        except ValueError:
            print("Invalid entry %d" % N)
    return N

def choose_number(N, bool_vec, score1, score2, bool):
    while(True):
        try : 
            x = int(input("Please give positive integer x: "))
            if 0 < x <= N and bool_vec[x - 1] != 0:
                break
            else:
                print("Invalid entry %d" % x)
        except ValueError:
            print("Invalid entry %d" % x)
    if bool == True:
        bool_vec[x-1] = 0
        score1 += x

        vec = np.arange(1, N+1)
        vec = np.multiply(vec, bool_vec)
        vec = vec[vec != x]
        vec = vec[vec !=0]
        for val in vec :
            if x % val == 0:
                score2 += val
                bool_vec[val-1] = 0
        bool = False
    
    elif bool == False:
        bool_vec[x-1] = 0
        score2 += x

        vec = np.arange(1, N+1)
        vec = np.multiply(vec, bool_vec)
        vec = vec[vec != x]
        vec = vec[vec !=0]
        for val in vec :
            if x % val == 0:
                score1 += val
                bool_vec[val-1] = 0
        bool = True
    return score1, score2, bool_vec, bool

def print_available_numbers(N, bool_vec) :
    vec = np.arange(1, N+1)
    vec = np.multiply(vec, bool_vec)
    vec = vec.astype(int)
    vec = vec[vec !=0]
    print(" ".join(str(val) for val in vec))

def check_if_number_still_available(bool_vec):
    if np.sum(bool_vec) == 0:
        return False
    else :
        return True
    
def play_game():
    score1 = 0
    score2 = 0
    N = get_positive_integer()
    bool_vec = np.ones(N, dtype=int)
    bool = True
    while(check_if_number_still_available(bool_vec)):  
        print_available_numbers(N, bool_vec)
        score1, score2, bool_vec, bool = choose_number(N, bool_vec, score1, score2, bool)
        print("Player 1’s score is %d and player 2’s score is %d" % (score1, score2))

    if score1 > score2:
        print("Player 1 Wins!")
    elif score2 > score1:
        print("Player 2 Wins!")
    else:
        print("Tie!")

play_game()
