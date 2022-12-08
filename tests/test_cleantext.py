from hypothesis import given, example
from hypothesis.strategies import text
from pytest import mark

from ternaus_cleantext.ternaus_cleantext import html_clean, whitespace_clean, basic_clean, url_clean, clean_text


@mark.parametrize(["input_text", "output_text"], [("https://ternaus.com", "https://ternaus.com"),
                                                  ('this is a test <b>bold</b>', 'this is a test bold')])
def test_clean_html_tags(input_text, output_text):
    assert html_clean(input_text) == output_text, html_clean(input_text)


@given(text(alphabet="abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789 \n\t", max_size=100))
def test_whitespace_clean(s):
    assert whitespace_clean(s) == " ".join(s.split())


@mark.parametrize(["input_text", "output_text"],
                  [("test &#38;", "test &"), ("https://ternaus.com", "https://ternaus.com")])
def test_basic_clean(input_text, output_text):
    assert basic_clean(input_text) == output_text


@mark.parametrize(["input_text", "output_text"], [("test   https://ternaus.com Test", "test    Test"),
    ("test   http://ternaus.com Test", "test    Test")])
def test_url_clean(input_text, output_text):
    assert url_clean(input_text) == output_text


@mark.parametrize(["input_text", "output_text"],
                  [("<Container>Preambula </Container>   https://ternaus.com Test\t", "preambula test"),
                      ("test   http://ternaus.com Test ", "test test"), ])
def test_cleantext(input_text, output_text):
    assert clean_text(input_text) == output_text
