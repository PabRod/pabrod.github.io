AUTHOR = 'Pablo Rodríguez Sánchez'
SITENAME = 'PabRod'
SITEURL = ""
SITESUBTITLE = 'Applied mathematician. Science storyteller'
SITELOGO = '/images/profile.png'
FAVICON = '/images/favicon.ico'

PATH = "content"
STATIC_PATHS = ['images', 'pdfs']

TIMEZONE = 'Europe/Amsterdam'

DEFAULT_LANG = 'en'

THEME = 'themes/Flex' # See configuration file (https://github.com/alexandrevicenzi/Flex/blob/master/docs/pelicanconf.py)

GITHUB_URL = GITHUB_CORNER_URL = "https://github.com/PabRod" # Both names might be required for some themes

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Menu
DISPLAY_PAGES_ON_MENU = True
DISPLAY_CATEGORIES_ON_MENU = False
USE_FOLDER_AS_CATEGORY = False # Maybe change this after deciding folder structure
MAIN_MENU = True
HOME_HIDE_TAGS = True

# Social widget
SOCIAL = (
    ("envelope", "mailto:pablo.rodriguez.sanchez@gmail.com"),
    ("github", GITHUB_URL),
    ("linkedin", "https://www.linkedin.com/in/pabrod"),
    ("instagram", "https://instagram.com/pablo.rodriguez.sanchez/"),
    ("mastodon", "https://paquita.masto.host/@DonMostrenco"),
    ("twitter", "http://twitter.com/DonMostrenco"),
    ("orcid", "https://orcid.org/0000-0002-2855-940X"),
    ('rss', SITEURL + '/pages/feeds-list.html'),
)

DEFAULT_PAGINATION = 10

# Plug-ins
PLUGINS = None # Load them from the namespace
MARKDOWN = {
    'extension_configs': {
        'markdown.extensions.codehilite': {'css_class': 'highlight'},
        'markdown.extensions.extra': {},
        'markdown.extensions.meta': {},
        "markdown_mermaidjs": {},
    },
    'output_format': 'html5',
}
PYGMENTS_STYLE = "monokai" # See list at https://pygments.org/styles/

# Uncomment following line if you want document-relative URLs when developing
# RELATIVE_URLS = True

CC_LICENSE = {
    "name": "Creative Commons Attribution-ShareAlike 4.0 International License",
    "version": "4.0",
    "slug": "by-sa",
    "icon": True,
    "language": "en",
}

from datetime import datetime
COPYRIGHT_YEAR = datetime.now().year