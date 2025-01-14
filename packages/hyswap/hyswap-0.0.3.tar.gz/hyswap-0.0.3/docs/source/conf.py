# -*- coding: utf-8 -*-

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
# Since we aren't installing package here, we mock imports of the dependencies.

# Relative paths so documentation can reference and include demos folder
import os
import sys
from importlib.metadata import version

# path to repository head
sys.path.insert(0, os.path.abspath('../..'))

# Project Information
project = 'hyswap'
release = version(project)
version = '.'.join(release.split('.')[:2])
author = 'USGS'

# -- General configuration ------------------------------------------------

# Add any Sphinx extension module names here, as strings.
extensions = [
    'sphinx.ext.autodoc',
    'sphinx.ext.doctest',
    'sphinx.ext.autosummary',
    'sphinx.ext.napoleon',
    'sphinx.ext.todo',
    'sphinx.ext.coverage',
    'sphinx.ext.viewcode',
    'matplotlib.sphinxext.plot_directive',
    'sphinx.ext.githubpages'
]

# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

# suffix of source documents
source_suffix = '.rst'

# The master toctree document.
master_doc = 'index'

# The language for content autogenerated by Sphinx. Refer to documentation
# for a list of supported languages.
#
# This is also used if you do content translation via gettext catalogs.
# Usually you set "language" from the command line for these cases.
language = 'en'

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This patterns also effect to html_static_path and html_extra_path
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']

# The name of the Pygments (syntax highlighting) style to use.
pygments_style = 'default'

# If true, `todo` and `todoList` produce output, else they produce nothing.
todo_include_todos = True

# Napoleon settings
napoleon_google_docstring = False
napoleon_numpy_docstring = True
napoleon_include_init_with_doc = False
napoleon_include_private_with_doc = False
napoleon_include_special_with_doc = True
napoleon_use_admonition_for_examples = False
napoleon_use_admonition_for_notes = False
napoleon_use_admonition_for_references = False
napoleon_use_ivar = False
napoleon_use_param = True
napoleon_use_rtype = True

# Autosummary / Automodapi settings
autosummary_generate = True
automodapi_inheritance_diagram = False
autodoc_default_options = {
    'members': True,
    'inherited-members': False,
    'private-members': True
}

# doctest
doctest_global_setup = '''
import hyswap
from hyswap import exceedance
from hyswap import rasterhydrograph
from hyswap import utils
from hyswap import percentiles
from hyswap import cumulative
from hyswap import plots
from hyswap import runoff
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import dataretrieval
'''

# mpl plots - metadata for the documentation plots
plot_basedir = 'pyplots'
plot_html_show_source_link = False
plot_formats = ['png', ('hires.png', 300)]
plot_pre_code = '''
import numpy as np
import matplotlib
from matplotlib import pyplot as plt
import hyswap
import dataretrieval
'''

# -- Options for HTML output ----------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.

html_theme = 'bizstyle'

# Theme options are theme-specific and customize the look and feel of a theme
# further.  For a list of options available for each theme, see the
# documentation.

html_theme_options = {
    "rightsidebar": True
}

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ['_static']

# -- Options for linkcheck -------------------------------------------

# Links to not "check" because they are problematic for the link checker
# typically DOI links don't work
linkcheck_ignore = [
    r'https://doi.org/10.3133/wsp1542A',
    r'https://doi.org/10.1029/2022WR031930',
    r'https://pypi.org/project/hyswap/'
]

linkcheck_exclude_documents = [
    r'meta/disclaimer*',
    r'meta/contributing*',
    r'meta/installation*'
]
