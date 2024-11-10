from markdown_pdf import MarkdownPdf, Section

pdf = MarkdownPdf()
f = open("data_analysis/questions.md", "r")
markdown_content=f.read()
pdf.add_section(Section(markdown_content, toc=False))
pdf.save('output.pdf')