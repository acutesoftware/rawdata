@echo off
REM check_coverage.bat
REM Thanks to nedbat @irc #python
coverage run tests\run_tests.py
coverage html
start htmlcov/index.html
