# This file is only used if you use `make publish` or
# explicitly specify it as your config file.

import os
import sys

sys.path.append(os.curdir)
from pelicanconf import *

# If your site is available via HTTPS, make sure SITEURL begins with https://
SITEURL = "https://pabrod.github.io/pelican-test/"
RELATIVE_URLS = False

# RSS feeds generation
FEED_ALL_ATOM = "feeds/all.atom.xml"
TRANSLATION_FEED_ATOM = 'feeds/all-{lang}.atom.xml'
CATEGORY_FEED_ATOM = None
TAG_FEED_ATOM = 'feeds/tag-{slug}.atom.xml'
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

DELETE_OUTPUT_DIRECTORY = True

# Following items are often useful when publishing

# DISQUS_SITENAME = ""
# GOOGLE_ANALYTICS = ""
