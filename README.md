# DataHarvesters
Various web scrapers for collecting data

## How to run

Create a virtual environment
```console
python -m venv env
```

[Activate](https://docs.python.org/3/library/venv.html#how-venvs-work) the environemnt and install the dependencies
```console
pip install -r requirements.txt
```

### goodreads

```console
scrapy runspider goodreads/BookSpider.py -O output/books.json
```
