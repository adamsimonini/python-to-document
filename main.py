
# -*- coding: utf-8 -*-

from htmldocx import HtmlToDocx
import jinja2
from docxtpl import DocxTemplate

new_parser = HtmlToDocx()
new_parser.table_style = 'Light Shading Accent 4'
new_parser.parse_html_file("index.html", "download")

doc = DocxTemplate("templates/docx-table.docx")
context = {'some_content1': "JASON SIMONS", "some_content2": "MEXICO"}  # Where the magic happens
doc.render(context)
doc.save("output/generated_doc.docx")


tpl = DocxTemplate('templates/horizontal_merge_tpl.docx')
tpl.render({})
tpl.save('output/horizontal_merge.docx')
