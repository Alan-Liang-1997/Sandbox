import wikipedia

search_input = input('Enter a page title or search phrase:')
while search_input != '':
    try:
        page_input = wikipedia.page(search_input)
        print(page_input.title)
        print(wikipedia.summary(search_input))
        print(page_input.url)

    except wikipedia.exceptions.DisambiguationError as e:
        print(e.options)

    search_input = input('Enter a page title or search phrase:')
