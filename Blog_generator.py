import cohere

co = cohere.Client('Your API key')


def generateBlog(paragraph_topic):
    response = co.generate(
        model='command-xlarge-nightly',
        prompt=f"Write a paragraph about: {paragraph_topic}",
        max_tokens=300,
        temperature=0.5
    )
    return response.generations[0].text.strip()


print(generateBlog('Why NYC is better than your city.'))
