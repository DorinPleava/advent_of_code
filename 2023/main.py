import sys

from readInput import readInput


def run_challenge(day):
    day_module = __import__(f'{day}.{day}', fromlist=['run'])

    input = readInput(f'{day}/input.txt')

    day_module.run(input)


if __name__ == '__main__':
    if len(sys.argv) != 2:
        print('Usage: python main.py <day>')
        sys.exit(1)

    day = sys.argv[1]
    print(f'Running challenge {day}')
    run_challenge(day)
