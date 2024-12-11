from paths import all_possible_paths
from utils import read_file_to_set
import time

l1 = ['t','o','r','b']
l2 = ['i','a','e','t']
l3 = ['y','s','i','c']
l4 = ['a','n','n','u']

board = [l1,l2,l3,l4]

# 4x4 board
# path is ~ [(0, 0), (1, 0), (1, 1), (2, 0), (3, 0), (3, 1), (2, 1), (1, 2)]
def wordFromPath(board, path):
    word = []
    for e in path:
        word.append(board[e[1]][e[0]])

    return ''.join(word)


def create_words(board, paths):
    words = set()
    for path in paths:
        words.add(wordFromPath(board, path))
    return words

def filter_set(real_words, potential_words):
    words = set()
    for word in potential_words:
        if word in real_words:
            words.add(word)
    return words

def solve(board):
    start = time.time()
    real_words = read_file_to_set('word-list.txt')
    print(time.time() - start)

    potential_paths = all_possible_paths()
    print(time.time() - start)

    potential_words = create_words(board, potential_paths)
    print(time.time() - start)

    words_on_board = filter_set(real_words, potential_words)
    print(time.time() - start)
    print("##### DONE #####")
    print(len(words_on_board))
    print(words_on_board)


if __name__ == '__main__':
    # output = wordFromPath(board, [(0, 0), (1, 0), (1, 1), (2, 0), (3, 0), (3, 1), (2, 1), (1, 2)])
    # print(output)
    # solve(board)
    r1 = ''
    r2 = ''
    r3 = ''
    r4 = ''
    board2 = [r1, r2, r3, r4]
    solve(board2)
    