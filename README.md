# learning-python-sportsdata

A Simple program for learning Python!
Query data about the NHL!

# Where to start?

- Install Python3.9 https://www.python.org/downloads/release/python-390/

- Check you have the right version in your PATH

```bash
> python --version
Python 3.9.0
```

- Install tox

```bash
> pip install tox
```

- Install git and clone the project. https://git-scm.com/

```bash
git clone https://github.com/cal-pratt/learning-python-sportsdata.git
cd learning-python-sportsdata
```

- Run tox:

```
> tox
GLOB sdist-make: C:\workspace\python\sportsdata\setup.py
py39 inst-nodeps: C:\workspace\python\sportsdata\.tox\.tmp\package\1\sportsdata-0.0.0.zip
py39 installed: ...
py39 run-test-pre: PYTHONHASHSEED='669'
py39 run-test: commands[0] | pytest tests/
=============================== test session starts=================================
platform win32 -- Python 3.9.0, pytest-6.1.2, py-1.9.0, pluggy-0.13.1
cachedir: .tox\py39\.pytest_cache
rootdir: C:\workspace\python\sportsdata
collected 1 item

tests\test_import.py .                                                        [ 33%]
tests\test_nhl_teams.py ..                                                    [100%]


================================ 1 passed in 0.03s ==================================
______________________________________summary________________________________________
  py39: commands succeeded
  congratulations :)
```

- Open PowerShell in admin mode and run `set-executionpolicy remotesigned`

- Activate the virtual environment and try a script:

```
> .\.tox\py39\Scripts\activate
(py39) > print-nhl-teams
New Jersey Devils
New York Islanders
New York Rangers
Philadelphia Flyers
Pittsburgh Penguins
...
```
