import os.path

input_dir = os.path.dirname(os.path.realpath(__file__))

def file_contents(filename):
    with open(os.path.join(input_dir, filename)) as f:
        return f.read()

day01 = file_contents('day01.txt')
day02 = file_contents('day02.txt')
day03 = file_contents('day03.txt')
day05 = file_contents('day05.txt')
day06 = file_contents('day06.txt')
day07 = file_contents('day07.txt')
day08 = file_contents('day08.txt')
day09 = file_contents('day09.txt')
day10 = file_contents('day10.txt')
