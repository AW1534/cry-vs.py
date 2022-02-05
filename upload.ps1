# store the directory of the script in a variable
$dir = Get-Location

# delete any existing distrobution files
Remove-Item "$dir/dist"

# install the latest version of dependencies
py -m pip install --upgrade twine
py -m pip install --upgrade build

# build the distribution
py -m build

# upload the distribution to PyPI
py -m twine upload --repository pypi dist/*
PAUSE