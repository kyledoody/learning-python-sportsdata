# nfl

A Simple program for learning Python!

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
git clone ...
cd nfl
```

- Run tox:

```
> tox
GLOB sdist-make: C:\workspace\python\nfl\setup.py
py39 inst-nodeps: C:\workspace\python\nfl\.tox\.tmp\package\1\nfl-0.0.0.zip
py39 installed: ...
py39 run-test-pre: PYTHONHASHSEED='669'
py39 run-test: commands[0] | pytest tests/
=============================== test session starts=================================
platform win32 -- Python 3.9.0, pytest-6.1.2, py-1.9.0, pluggy-0.13.1
cachedir: .tox\py39\.pytest_cache
rootdir: C:\workspace\python\nfl
collected 1 item

tests\test_module.py .                                                     [100%]

================================ 1 passed in 0.03s ==================================
______________________________________summary________________________________________
  py39: commands succeeded
  congratulations :)
```
