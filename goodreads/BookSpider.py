import scrapy

class BookSpider(scrapy.Spider):
    name = 'BookSpider'
    start_urls = [
        'https://www.goodreads.com/list/show/21995.Best_21st_Century_Non_Fiction?page=1'
    ]

    def parse(self, response):
        for book in response.css('a.bookTitle'):
            yield response.follow(book, self.parse_book)

        for next_page in response.css('a.next_page'):
            yield response.follow(next_page, self.parse)

    def parse_book(self, response):
        title = response.css('[data-testid="bookTitle"]::text').get()
        author = response.css('.BookPageMetadataSection__contributor ::text').get()
        image = response.css('.BookCover__image img').attrib['src']
        description = response.css('.BookPageMetadataSection__description ::text').get()

        bookPagesFormat = response.css('[data-testid="pagesFormat"] ::text').get().split(',')
        pages = None
        book_format = None
        
        if len(bookPagesFormat) == 2:
            pages = int(bookPagesFormat[0].split()[0].strip())
            book_format = str(bookPagesFormat[1]).strip()

        genres = response.css('.BookPageMetadataSection__genreButton ::text').getall()

        yield {
            'title': title,
            'author': author,
            'image': image,
            'description': description,
            'pages': pages,
            'format': book_format,
            'genres': genres
        }