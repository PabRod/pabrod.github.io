AUTHOR = 'Pablo Rodríguez Sánchez'
SITENAME = 'PabRod'
SITEURL = ""

PATH = "content"

TIMEZONE = 'Europe/Rome'

DEFAULT_LANG = 'en'

THEME = '/home/pablo/pelican-themes/Flex/'
# Consider also mg and Peli-Kiera,
# see configuration file (https://github.com/alexandrevicenzi/Flex/blob/master/docs/pelicanconf.py)

# Feed generation is usually not desired when developing

FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (
    ("Pelican", "https://getpelican.com/"),
    ("Python.org", "https://www.python.org/"),
    ("Jinja2", "https://palletsprojects.com/p/jinja/"),
    ("You can modify those links in your config file", "#"),
)

# Social widget
SOCIAL = (
    ("envelope", "mailto:pablo.rodriguez.sanchez@gmail.com"),
    ("github", "https://github.com/PabRod"),
    ("twitter", "http://twitter.com/DonMostrenco"),
    ("linkedin", "https://www.linkedin.com/in/pabrod"),
    ("instagram", "https://instagram.com/pablo.rodriguez.sanchez/"),
    ("mastodon", "https://paquita.masto.host/@DonMostrenco"),
    ("orcid", "https://orcid.org/0000-0002-2855-940X"),
    ('rss', SITEURL + '/pages/feeds-list-en.html'),
)

DEFAULT_PAGINATION = 10

# Plug ins
MARKDOWN = {
    'extension_configs': {
        'markdown.extensions.codehilite': {'css_class': 'highlight'},
        'markdown.extensions.extra': {},
        'markdown.extensions.meta': {},
        "markdown_mermaidjs": {},
    },
    'output_format': 'html5',
}

# Uncomment following line if you want document-relative URLs when developing
# RELATIVE_URLS = True
