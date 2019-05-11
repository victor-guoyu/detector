import os
import sys
from detector import Detector
from exceptions import InvalidArgument, InvalidFileInput, InvalidTupleSize

MIN_NUM_ARG = 4
MAX_NUM_ARG = 5
DEFAULT_TUPLE_SIZE = 3
HELP_MSG = """
Plagiarism Detection:
    A simple CLI tool that performs plagiarism detection using N-tuple comparison
USAGE:
    <synonym_file> <input_file_1> <input_file_2> [<tuple_size>]
"""

def is_file_valid(file_path):
    return os.path.isfile(file_path)

def main(cli_args):
    try:
        cli_arg_len = len(cli_args)
        if cli_arg_len < MIN_NUM_ARG or cli_arg_len > MAX_NUM_ARG:
            raise InvalidArgument

        synonym_file = cli_args[1]
        if not is_file_valid(synonym_file):
            raise InvalidFileInput(f'Synonym file not found: {synonym_file}')
        synonym_file = open(synonym_file, 'r')

        input_file_1 = cli_args[2]
        if not is_file_valid(input_file_1):
            raise InvalidFileInput(f'input file 1 not found: {input_file_1}')
        input_file_1 = open(input_file_1, 'r')

        input_file_2 = cli_args[3]
        if not is_file_valid(input_file_2):
            raise InvalidFileInput(f'input file 2 not found: {input_file_2}')
        input_file_2 = open(input_file_2, 'r')

        tuple_size = DEFAULT_TUPLE_SIZE
        if cli_arg_len == MAX_NUM_ARG:
            tuple_size = int(cli_args[4])
            if tuple_size < 1:
                raise InvalidTupleSize

        detector = Detector(
            synonym_file=synonym_file,
            input_file_1=input_file_1,
            input_file_2=input_file_2,
            tuple_size=tuple_size
        )
        percentage = detector.calculate_percentage()
        print(f'🥁 total match percentage is: {percentage}%')
    except InvalidArgument:
        print(HELP_MSG)
    except InvalidFileInput as file_error:
        print(file_error.message)
    except InvalidTupleSize:
        print('tupple size should be greater than 0!')
    except Exception as e:
        print('😱 An unknow error occured! Cannot compute!')
        print(e)


if __name__ == "__main__":
    main(sys.argv)
