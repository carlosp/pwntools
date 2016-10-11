# -*- coding: utf-8 -*-
#
# pwntools documentation build configuration file, created by
# sphinx-quickstart on Wed May 28 15:00:52 2014.
#
# This file is execfile()d with the current directory set to its containing dir.
#
# Note that not all possible configuration values are present in this
# autogenerated file.
#
# All configuration values have a default; values that are commented out
# serve to show the default.

import os
import subprocess
import sys

build_dash = tags.has('dash')

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
sys.path.insert(0, os.path.abspath('../..'))

import pwnlib

# -- General configuration -----------------------------------------------------

# If your documentation needs a minimal Sphinx version, state it here.
#needs_sphinx = '1.0'

# Add any Sphinx extension module names here, as strings. They can be extensions
# coming with Sphinx (named 'sphinx.ext.*') or your custom ones.
extensions = [
    'pwnlib.internal.dochelper',
    'sphinx.ext.autodoc',
    'sphinx.ext.doctest',
    'sphinx.ext.linkcode',
    'sphinx.ext.autosummary',
    'sphinx.ext.coverage',
    'sphinx.ext.todo',
    'sphinx.ext.intersphinx',
    'sphinxcontrib.autoprogram',
    'sphinxcontrib.napoleon'
]

doctest_global_setup = '''
import sys, os
os.environ['PWNLIB_NOTERM'] = '1'
os.environ['PWNLIB_RANDOMIZE'] = '0'
import pwnlib
pwnlib.context.context.reset_local()
pwnlib.context.ContextType.defaults['log_level'] = 'ERROR'
pwnlib.context.ContextType.defaults['randomize'] = False
pwnlib.term.text.when = 'never'
pwnlib.log.install_default_handler()
pwnlib.log.rootlogger.setLevel(1)

# Sphinx modifies sys.stdout, and context.log_terminal has
# a reference to the original instance.  We need to update
# it for logging to be captured.
class stdout(object):
    def __getattr__(self, name):
        return getattr(sys.stdout, name)
    def __setattr__(self, name, value):
        return setattr(sys.stdout, name, value)
pwnlib.context.ContextType.defaults['log_console'] = stdout()
'''

autodoc_member_order = 'alphabetical'

# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

doctest_test_doctest_blocks = True

# The suffix of source filenames.
source_suffix = '.rst'

# The encoding of source files.
source_encoding = 'utf-8-sig'

# The master toctree document.
master_doc = 'index'

# General information about the project.
project = u'pwntools'
copyright = u'2016, Gallopsled et al.'

# The version info for the project you're documenting, acts as replacement for
# |version| and |release|, also used in various other places throughout the
# built documents.
#
# The short X.Y version.
release = pwnlib.__version__
version = release.rsplit('.', 1)[0]

# The language for content autogenerated by Sphinx. Refer to documentation
# for a list of supported languages.
#language = None

# There are two options for replacing |today|: either, you set today to some
# non-false value, then it is used:
#today = ''
# Else, today_fmt is used as the format for a strftime call.
#today_fmt = '%B %d, %Y'

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
exclude_patterns = []

# The reST default role (used for this markup: `text`) to use for all documents.
#default_role = None

# If true, '()' will be appended to :func: etc. cross-reference text.
#add_function_parentheses = True

# If true, the current module name will be prepended to all description
# unit titles (such as .. function::).
#add_module_names = True

# If true, sectionauthor and moduleauthor directives will be shown in the
# output. They are ignored by default.
#show_authors = False

# The name of the Pygments (syntax highlighting) style to use.
pygments_style = 'sphinx'

# A list of ignored prefixes for module index sorting.
#modindex_common_prefix = []


# -- Options for HTML output ---------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
html_theme = 'default'

# Theme options are theme-specific and customize the look and feel of a theme
# further.  For a list of options available for each theme, see the
# documentation.
#html_theme_options = {}

# Add any paths that contain custom themes here, relative to this directory.
#html_theme_path = []

# The name for this set of Sphinx documents.  If None, it defaults to
# "<project> v<release> documentation".
#html_title = None

# A shorter title for the navigation bar.  Default is the same as html_title.
#html_short_title = None

# The name of an image file (relative to this directory) to place at the top
# of the sidebar.
#html_logo = None

# The name of an image file (within the static path) to use as favicon of the
# docs.  This file should be a Windows icon file (.ico) being 16x16 or 32x32
# pixels large.
#html_favicon = None

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = []

# If not '', a 'Last updated on:' timestamp is inserted at every page bottom,
# using the given strftime format.
#html_last_updated_fmt = '%b %d, %Y'

# If true, SmartyPants will be used to convert quotes and dashes to
# typographically correct entities.
#html_use_smartypants = True

# Custom sidebar templates, maps document names to template names.
#html_sidebars = {}

# Additional templates that should be rendered to pages, maps page names to
# template names.
#html_additional_pages = {}

# If false, no module index is generated.
html_domain_indices = not build_dash

# If false, no index is generated.
html_use_index = not build_dash

# If true, the index is split into individual pages for each letter.
#html_split_index = False

# If true, links to the reST sources are added to the pages.
#html_show_sourcelink = True

# If true, "Created using Sphinx" is shown in the HTML footer. Default is True.
#html_show_sphinx = True

# If true, "(C) Copyright ..." is shown in the HTML footer. Default is True.
#html_show_copyright = True

# If true, an OpenSearch description file will be output, and all pages will
# contain a <link> tag referring to it.  The value of this option must be the
# base URL from which the finished HTML is served.
#html_use_opensearch = ''

# This is the file name suffix for HTML files (e.g. ".xhtml").
#html_file_suffix = None

# Output file base name for HTML help builder.
htmlhelp_basename = 'pwntoolsdoc'


# -- Options for LaTeX output --------------------------------------------------

latex_elements = {
# The paper size ('letterpaper' or 'a4paper').
#'papersize': 'letterpaper',

# The font size ('10pt', '11pt' or '12pt').
#'pointsize': '10pt',

# Additional stuff for the LaTeX preamble.
#'preamble': '',
}

# Grouping the document tree into LaTeX files. List of tuples
# (source start file, target name, title, author, documentclass [howto/manual]).
latex_documents = [
  ('index', 'pwntools.tex', u'pwntools Documentation',
   u'2016, Gallopsled et al.', 'manual'),
]

intersphinx_mapping = {'python': ('https://docs.python.org/2.7', None),
                       'paramiko': ('https://paramiko-docs.readthedocs.org/en/1.15/', None)}

# The name of an image file (relative to this directory) to place at the top of
# the title page.
#latex_logo = None

# For "manual" documents, if this is true, then toplevel headings are parts,
# not chapters.
#latex_use_parts = False

# If true, show page references after internal links.
#latex_show_pagerefs = False

# If true, show URL addresses after external links.
#latex_show_urls = False

# Documents to append as an appendix to all manuals.
#latex_appendices = []

# If false, no module index is generated.
#latex_domain_indices = True


# -- Options for manual page output --------------------------------------------

# One entry per manual page. List of tuples
# (source start file, name, description, authors, manual section).
man_pages = [
    ('index', 'pwntools', u'pwntools Documentation',
     [u'2016, Gallopsled et al.'], 1)
]

# If true, show URL addresses after external links.
#man_show_urls = False


# -- Options for Texinfo output ------------------------------------------------

# Grouping the document tree into Texinfo files. List of tuples
# (source start file, target name, title, author,
#  dir menu entry, description, category)
texinfo_documents = [
  ('index', 'pwntools', u'pwntools Documentation',
   u'', 'pwntools', 'CTF exploit writing toolkit.',
   'Miscellaneous'),
]

# Documents to append as an appendix to all manuals.
#texinfo_appendices = []

# If false, no module index is generated.
#texinfo_domain_indices = True

# How to display URL addresses: 'footnote', 'no', or 'inline'.
#texinfo_show_urls = 'footnote'

branch = release

try:
    git_branch = subprocess.check_output('git describe --tags', shell = True)
except subprocess.CalledProcessError:
    git_branch = '-'

try:
    if '-' in git_branch:
        branch = subprocess.check_output('git rev-parse HEAD', shell = True).strip()[:10]
except subprocess.CalledProcessError:
    pass

def linkcode_resolve(domain, info):
    if domain != 'py':
        return None
    if not info['module']:
        return None

    import importlib, inspect, types
    mod = importlib.import_module(info['module'])

    # Try to find the value
    val = mod
    for k in info['fullname'].split('.'):
        val = getattr(val, k, None)
        if val == None:
            break

    # Special case for shellcraft
    if info['module'].startswith('pwnlib.shellcraft.'):
        filename = 'pwnlib/shellcraft/templates/%s' % val._relpath

    # Case for everything else
    else:
        filename = info['module'].replace('.', '/') + '.py'

        if isinstance(val, (types.ModuleType, types.ClassType, types.MethodType, types.FunctionType, types.TracebackType, types.FrameType, types.CodeType)):
            try:
                lines, first = inspect.getsourcelines(val)
                filename += '#L%d-%d' % (first, first + len(lines) - 1)
            except IOError:
                pass

    return "https://github.com/Gallopsled/pwntools/blob/%s/%s" % (branch, filename)


# The readthedocs theme is used by the Dash generator. (Can be used for HTML too.)

if build_dash:

    # on_rtd is whether we are on readthedocs.org
    on_rtd = os.environ.get('READTHEDOCS', None) == 'True'

    if not on_rtd:  # only import and set the theme if we're building docs locally
        import sphinx_rtd_theme
        html_theme = 'sphinx_rtd_theme'
        html_theme_path = [sphinx_rtd_theme.get_html_theme_path()]

    # otherwise, readthedocs.org uses their theme by default, so no need to specify it
