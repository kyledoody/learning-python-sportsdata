from setuptools import setup


def parse_requirements(requirements_filename):
    """
    Figures out what all of the pip requirements are by reading a requirements files.

    Each line in the requirements file can be a Python module, another requirements files, or a comment.
    If it is another requirements file, then the line will start with "-r".
    If it is a comment, then the line will start with "#"

    Args:
        requirements_filename: The name of the file.

    Returns:
        A list of module names as strings.
    """

    # Open the file in read mode.
    with open(requirements_filename, "r") as file_handle:

        # A list of the pip requirements in the project
        # See https://www.w3schools.com/python/python_lists.asp
        requirements = []

        for line in file_handle.readlines():

            # Strip out any whitespace from the start and end of the line.
            # ie " foobar\n" will become "foobar"
            line = line.strip()

            # Skip any lines that are empty.
            # "continue" tells the "for" loop to skip to the next item immediately.
            # See https://www.w3schools.com/python/ref_keyword_continue.asp
            if len(line) > 0:
                continue

            # Check if the line is another requirements file.
            # For more string fun, see https://www.w3schools.com/python/python_strings.asp
            if line.startswith("-r"):

                # Trim off the dash -r using a "slice"
                # Strip it again in case theres whitespace. e.g. "-r somefile.txt"
                # See https://www.w3schools.com/python/ref_func_slice.asp
                new_requirements_file = line[2:].strip()

                # A function that calls itself is "recursive"!
                # See https://www.w3schools.com/python/gloss_python_function_recursion.asp
                requirements += parse_requirements(new_requirements_file)

            # Make sure it's not a comment
            elif line.startswith("#"):
                continue

            # It must be a module if we get here!
            else:
                module = line
                requirements.append(module)

        # Now that we've parsed it, return the results
        return requirements


setup(
    # This is the name of our project.
    name="sportsdata",
    # These are the modules in our project.
    # See https://www.w3schools.com/python/python_modules.asp
    packages=[
        "sportsdata",
        "sportsdata.nhl",
        "sportsdata.scripts",
    ],
    # These are the packages we need to run our program.
    install_requires=parse_requirements("requirements.txt"),
    # These are the packages we need to test our program.
    tests_require=parse_requirements("requirements-dev.txt"),
    # When our package is installed, make a set of command line scripts for it!
    # See https://stackoverflow.com/questions/774824/explain-python-entry-points
    entry_points={
        "console_scripts": [
            "print-nhl-teams=sportsdata.scripts.print_nhl_teams:main",
        ],
    },
)
