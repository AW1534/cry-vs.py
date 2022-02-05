import json

project = 'cry-vs.py'
copyright = '2022, addikted'
author = 'addikted'
language = "en"

# The full version, including alpha/beta/rc tags
with open("../config.json") as f:
    config = json.load(f)

release = config["version"]

ogp_site_url = "http://cry-vs-py.readthedocs.io/"
ogp_type = "article"
ogp_custom_meta_tags = [
    '<meta property="og:ignore_canonical" content="true" />',
]

extensions = [
    "myst_parser",
    "sphinxext.opengraph",
    "sphinx_copybutton",
    "sphinx_panels",
]

# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']

# -- Options for HTML output -------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
html_theme = 'sphinx_book_theme'

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ['_static']

# main file
master_doc = 'index'


def setup(app):
    app.add_js_file("js/script.js")
