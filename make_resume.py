import fitz
import os

path = os.path.join(os.path.dirname(__file__), "images", "resume.pdf")
doc = fitz.open()
page = doc.new_page(width=595, height=842)
text = (
    "MY PORTFOLIO\n"
    "Front-End Developer\n\n"
    "Email: info@example.com\n"
    "Location: Cairo, Egypt\n"
    "Phone: +20 123 456 7890\n\n"
    "SUMMARY\n"
    "Front-end developer passionate about building beautiful and\n"
    "functional websites using HTML and CSS.\n\n"
    "SKILLS\n"
    "HTML 90%\n"
    "CSS 80%\n"
    "JavaScript 70%\n"
    "UI/UX Design 75%\n\n"
    "EXPERIENCE\n"
    "Freelance Front-End Developer\n"
    "Built responsive personal and business websites with\n"
    "clean HTML5 and CSS3 layouts.\n"
)
page.insert_text((72, 72), text, fontsize=12, fontname="helv")
doc.save(path)
doc.close()
print("wrote", path)
