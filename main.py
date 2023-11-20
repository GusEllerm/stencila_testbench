import stencila, asyncio
from stencila.types import Article, CreativeWork, Paragraph, Text, Thing
from stencila.convert import to_json, to_path, to_string, from_to

def main():
  # Create an example paragraph
  example_paragraph = Paragraph(content=[Text("This is an example paragraph.")])

  # Create an article object
  article = Article(
    content=[example_paragraph],
    title="Example Article",
    description="This is an example article."
  )

  assert isinstance(article, Article)
  assert isinstance(article, CreativeWork)
  assert isinstance(article, Thing)
  assert isinstance(article.content[0], Paragraph)
  assert isinstance(article.content[0].content[0], Text)

  json = asyncio.run(to_string(article, format="json"))

  print(json)
  


  

if __name__ == "__main__":
  main()
