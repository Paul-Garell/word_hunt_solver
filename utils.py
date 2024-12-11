import time

#read in words into a dictionary
def read_file_to_set(filename):
    """Read a text file and store each line as an entry in a set."""
    try:
        with open(filename, 'r') as file:
            return {line.strip() for line in file}
    except FileNotFoundError:
        print(f"Error: The file '{filename}' was not found.")
        return set()
    
if __name__ == '__main__':
    start = time.time()
    end = time.time()
    wordSet = read_file_to_set('word-list.txt')
    print(end-start)
    
    print(len(wordSet))
