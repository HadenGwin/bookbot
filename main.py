from stats import word_count, char_count, sort_dict
import sys


def get_book_text(filepath):
    with open(filepath) as f:
        return f.read()

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    else:
        bookPath = sys.argv[1]
        text = get_book_text(bookPath)
        sortedDict = sort_dict(char_count(text))
    
        print("============ BOOKBOT ============")
        print(f'Analyzing book found at {bookPath}...')
        print("----------- Word Count ----------")
        print(f'Found {word_count(text)} total words')
        print("--------- Character Count -------")
        for item in sortedDict:
            print(f'{item['character']}: {item['num']}')

main()