[![Sourcery](https://img.shields.io/badge/Sourcery-enabled-brightgreen)](https://sourcery.ai)

# Cleantextclip
Library to prepare text for machine learning and NLP tasks. Originated from CLIP model preparation, but a few more
rules were added.

## Installation
```bash
pip install -U ternaus_cleantext
```


Cleans text similar, but stricter than in the CLIP model:

1. Escapes HTML characters
2. Removes html tags
3. Removes URLs
4. Removes extra white spaces
5. Text to lower case 

```python
from ternaus_cleantext.ternaus_cleantext import clean_text
print(clean_text("This is a test https://ternaus.com <b>bold</b>"))
```
returns
`this is a test bold`
