import wikipedia

title = input("Enter page title:")
while title != "":
    try:
        wikipedia.search(title)
        page = wikipedia.page(title, autosuggest=False)
        print(page.title)
        wikipedia.summary(title, sentences=3)
        print(wikipedia.summary(title, sentences=3))
    except wikipedia.exceptions.DisambiguationError as DisambiguationError:
        print("We need a more specific title. Try one of the following, or a new search:")
        print(DisambiguationError.options)
    except wikipedia.exceptions.PageError as PageError:
        print(PageError)
    title = input("\nEnter page title:")
print("Thank you.")