import stencila, asyncio
from dataclasses import dataclass, field
from datetime import datetime
from typing import List, Optional, Literal
from stencila.types import *
from stencila.convert import to_json, to_path, to_string, from_to



def main():
  # Content is created programmatically using Python bindings
  # This would be done in the Stencila editor using the UI instead

  # Each section is its own object. 
  introduction = Section(
    section_type=SectionType.Introduction,
    content=[
      Heading(Text("Introduction"), level=0),
      Paragraph(content=[Text("""Welcome to our LivePublication demonstration! The landscape of scientific research is ever-evolving, and with it, the way we share and consume scientific knowledge needs to progress. Traditional scientific publishing, with its static format, often struggles to effectively convey the dynamic nature of modern computational research. This article represents initial steps toward enabling and standardising methods of integrating distributed scientific workflows with top level narrative text, building a pipeline from workflow execution, to publication outputs.""")])
    ]
  )

  temp = [
  Heading(
          content=[
            Text("Introduction")
          ]
        ),
        Paragraph(content=[Text("""Welcome to our LivePublication demonstration! The landscape of scientific research is ever-evolving, and with it, the way we share and consume scientific knowledge needs to progress. Traditional scientific publishing, with its static format, often struggles to effectively convey the dynamic nature of modern computational research. This article represents initial steps toward enabling and standardising methods of integrating distributed scientific workflows with top level narrative text, building a pipeline from workflow execution, to publication outputs.""")]),
        Paragraph(
          content=[
            Text("""The LivePublication framework aims to enable live, 
                 reactive publications while simultaneously enhancing 
                 transparency, repeatability, and collaborative scientific 
                 research. In order to achive this, LivePublication 
                 leverages custom Globus action providers"""),
            Link(content="AP overview",
                target="https://action-provider-tools.readthedocs.io/en/latest/"),
            Link(content="(custom AP)",
                target="https://github.com/LivePublication/LP_GlobusAP_Template"),
            Text("""to simultaniously perform work within workflows, and generate descriptive 
                 RO-Crates.""")
          ],
          id="UUID-2"
        ),
        Paragraph(
          content=[
            Text("""Subsequently, these individual artefacts come together to 
                 form an 'orchestration crate'. This crate offers a comprehensive 
                 description of the workflow execution, cataloging inputs, outputs, 
                 methods, and associated metadata.""")
          ],
          id="UUID-3"
        ),
        Paragraph(
          content=[
            Text("""The generated orchestration crate serves as a data model for 
                 publications, exemplified by this website, which offers live updates 
                 to figures, metrics, and other metadata. The design, captured metadata, 
                 and integration techniques with the publication are all areas 
                 currently being refined. For a deeper exploration of this method, 
                 refer to"""),
                 Link(content=[Text("this article")], 
                      target="https://livepublication.github.io/LP_Pub_DistCompPub/")
          ],
          id="UUID-4"
        ),
        Paragraph(
          content=[
            Text("""For an overview of the publication pipeline behind this article, 
                 see @fig-globus-overview. It's important to mention that the methods 
                 featured within Layer 3, pertaining to publication and presentation, 
                 are showcased for demonstration only. We are actively researching 
                 the transition from the orchestration crate to the final compiled 
                 article.""")
          ],
          id="UUID-5"
        ),
        Figure(
          content=[],
          url="globus-overview.svg"
        )
]

  Institutions = {
    "Canterbury": Organization(name="University of Canterbury", description=Text("A university in Christchurch, New Zealand")),
    "Auckland": Organization(name="University of Auckland", description=Text("A university in Auckland, New Zealand")),
    "MBIE": Organization(name="Ministry of Business, Innovation and Employment", description=Text("A government department in Wellington, New Zealand"))
  }

  Authors = {
    "Augustus Ellerm": Person(name="Augustus Ellerm", affiliations=[Institutions["Canterbury"]]),
    "Benjamin Adams": Person(name="Benjamin Adams"),
    "Mark Gahegan": Person(name="Mark Gahegan"),
  }

  # Create an Article container & set metadata fields
  article=Article(
    title=[Text("Language identification method comparison")],
    authors=[Authors["Augustus Ellerm"], Authors["Benjamin Adams"], Authors["Mark Gahegan"]],
    keywords=["Example", "LID", "Computational Linguistics"],
    abstract=[Paragraph(content=[Text("""This article presents an early look at how the LivePublication framework can enable live, updating components and generative content for computationally driven sciences. Presented is a language identification performance task, comparing the accuracy of two methods (langdetect and fastText).""")])],
    description=Text("A test article constructed with the stencila python bindings"),
    funded_by=[MonetaryGrant(funders=[Institutions["MBIE"]])],
    date_created=Date(datetime(2023, 11, 20).isoformat()),
    date_modified=Date(datetime.now().isoformat()),
    content=[]
  )


  # assert isinstance(article, Article)
  # assert isinstance(article, CreativeWork)
  # assert isinstance(article, Thing)
  # assert isinstance(article.content[0], Paragraph)
  # assert isinstance(article.content[0].content[0], Text)

  json = asyncio.run(to_string(article, format="md"))

  
  with open("Article.md", "w") as file:
    file.write(json)
  


if __name__ == "__main__":
  main()

