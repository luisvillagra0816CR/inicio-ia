# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'IA con Gemini y ChatGPT'
copyright = '2025, Luis Villagra'
author = 'Luis Villagra'
release = '1.0'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = [
    'recommonmark',
    #'myst_parser'
]

# myst_enabled_extensions = [
#     "dollarmath",
#     "html_image"
# ]

from recommonmark.transform import AutoStructify

templates_path = ['_templates']
exclude_patterns = []

language = 'es'

# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

# html_theme = 'alabaster'
# html_theme = 'classic'
html_theme = 'sphinx_rtd_theme' 

html_theme_options = {

    'style_nav_header_background': '#221a50',
}

html_static_path = ['_static']

url_repositorio = "https://google/"

def setup(app):
    app.add_config_value(
        'recomonmark_config', 
        {
            'url_resolver': lambda url: url_repositorio + url,
            'auto_toc_tree_section': 'Contenido'
        },
        True
    )

    app.add_transform(AutoStructify)
