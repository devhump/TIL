headline = input()
# headline = "The_headline_is_the_text_indicating_the_nature_of_the_article_below_it."


for char in headline:

    if char.isalpha():
        if char.islower():
            headline = headline.replace(char, chr(ord(char)-32))

print(headline)
