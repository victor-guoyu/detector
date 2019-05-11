To run this locally, you need to have Python 3.6.3 +

Sample command
```bash
$: python cli.py ./test_files/s.txt ./test_files/1.txt ./test_files/2.txt 2
```

Test setup:
```bash
# skip if you don't mind to install test dependecies globally
$: mkvirtualenv detector -a . --python=python3
$: pip install -r test-requirements.txt
$: pytest -v
```
