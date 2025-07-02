import requests
from bs4 import BeautifulSoup
from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer
from reportlab.lib.styles import getSampleStyleSheet

# Get web page
page = requests.get("https://medium.com/@sim30217/uuid-734c0adfe44e", verify=False)
soup = BeautifulSoup(page.content, 'html.parser')

# Extract article
article_content = soup.find('article')
if article_content:
    page_text = article_content.get_text(separator="\n\n", strip=True)
else:
    page_text = "No content found."

# Create PDF
file_name = "sample.pdf"
doc = SimpleDocTemplate(file_name, pagesize=letter)
styles = getSampleStyleSheet()
story = []

# Split the text into paragraphs
for para in page_text.split("\n\n"):
    story.append(Paragraph(para, styles["Normal"]))
    story.append(Spacer(1, 12))  # Add some space between paragraphs

doc.build(story)
print(f"Saved nicely formatted PDF as {file_name}")
