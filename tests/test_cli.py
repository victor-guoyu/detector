import io
import pytest
import mock
from cli import main, HELP_MSG

@mock.patch('sys.stdout', new_callable=io.StringIO)
def test_invalid_argument(std_out):
    main([])
    assert 'USAGE:' in std_out.getvalue()

@mock.patch('sys.stdout', new_callable=io.StringIO)
@mock.patch('cli.is_file_valid')
def test_invalid_snyonym_file(is_file_valid, std_out):
    is_file_valid.return_value = False
    main(['blah', 'blah', 'blah', 'blah'])
    assert 'Synonym file not found:' in std_out.getvalue()

@mock.patch('sys.stdout', new_callable=io.StringIO)
@mock.patch('cli.is_file_valid')
@mock.patch('builtins.open')
def test_invalid_input_file_1(open_file, is_file_valid, std_out):
    is_file_valid.side_effect = [True, False]
    main(['blah', 'blah', 'blah', 'blah'])
    assert 'input file 1 not found:' in std_out.getvalue()

@mock.patch('sys.stdout', new_callable=io.StringIO)
@mock.patch('cli.is_file_valid')
@mock.patch('builtins.open')
def test_invalid_input_file_2(open_file, is_file_valid, std_out):
    is_file_valid.side_effect = [True, True, False]
    main(['blah', 'blah', 'blah', 'blah'])
    assert 'input file 2 not found:' in std_out.getvalue()

@mock.patch('sys.stdout', new_callable=io.StringIO)
@mock.patch('cli.is_file_valid')
@mock.patch('builtins.open')
def test_invalid_tuple_size(open_file, is_file_valid, std_out):
    is_file_valid.side_effect = [True, True, True]
    main(['blah', 'blah', 'blah', 'blah', -1])
    assert 'tupple size should be greater than 0!' in std_out.getvalue()