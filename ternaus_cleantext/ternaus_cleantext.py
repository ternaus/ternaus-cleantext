import html
import ftfy
import re

CLEAN_HTML_TAGS = re.compile('<.*?>|&([a-z0-9]+|#[0-9]{1,6}|#x[0-9a-f]{1,6});')
CLEAN_URL = r'''(?i)\b((?:(https|http)?://|www\d{0,3}[.]|[a-z0-9.\-]+[.][a-z]{2,4}/)(?:[^\s()<>]+|\(([^\s()<>]+|(\([^\s()<>]+\)))*\))+(?:\(([^\s()<>]+|(\([^\s()<>]+\)))*\)|[^\s`!()\[\]{};:'".,<>?«»“”‘’]))'''


def basic_clean(text: str) -> str:
    text = ftfy.fix_text(text)
    return html.unescape(text).strip()


def whitespace_clean(text: str) -> str:
    return re.sub(r'\s+', ' ', text).strip()


def html_clean(raw_html: str) -> str:
    return re.sub(CLEAN_HTML_TAGS, '', raw_html)


def url_clean(text: str) -> str:
    return re.sub(CLEAN_URL, "", text)


def clean_text(text: str) -> str:
    text = basic_clean(text)
    text = html_clean(text)
    text = url_clean(text)
    return whitespace_clean(text).lower()
