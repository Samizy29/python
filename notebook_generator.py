from reportlab.lib.pagesizes import inch
from reportlab.pdfgen import canvas

# -----------------------------
# 6 x 9 inches trim size
PAGE_WIDTH = 6 * inch
PAGE_HEIGHT = 9 * inch

# Margins (KDP safe)
INNER_MARGIN = 0.75 * inch
OUTER_MARGIN = 0.5 * inch
TOP_MARGIN = 0.5 * inch
BOTTOM_MARGIN = 0.5 * inch

# Line spacing (college-ruled feel)
LINE_SPACING = 0.3 * inch
NOTEBOOK_PAGES = 120

file_name = "my_notebook_6x9_kdp.pdf"
c = canvas.Canvas(file_name, pagesize=(PAGE_WIDTH, PAGE_HEIGHT))

# -----------------------------
# PAGE 1: TITLE PAGE
c.setFont("Helvetica-Bold", 22)
c.drawCentredString(PAGE_WIDTH / 2, PAGE_HEIGHT / 2 + 40, "My Notebook")

c.setFont("Helvetica", 14)
c.drawCentredString(PAGE_WIDTH / 2, PAGE_HEIGHT / 2, "Samuel Oni")

c.showPage()

# -----------------------------
# PAGE 2: COPYRIGHT PAGE
c.setFont("Helvetica", 10)

copyright_text = [
    "Copyright © 2026 Samuel Oni",
    "",
    "All rights reserved.",
    "",
    "No part of this book may be reproduced,",
    "stored in a retrieval system, or transmitted",
    "in any form or by any means without prior",
    "written permission of the publisher.",
    "",
    "Printed in the United States of America"
]

y = PAGE_HEIGHT - TOP_MARGIN - 40
for line in copyright_text:
    c.drawCentredString(PAGE_WIDTH / 2, y, line)
    y -= 14

c.showPage()

# -----------------------------
# NOTEBOOK PAGES (lined pages)
for page in range(NOTEBOOK_PAGES):
    y = PAGE_HEIGHT - TOP_MARGIN

    while y > BOTTOM_MARGIN:
        c.line(
            INNER_MARGIN,
            y,
            PAGE_WIDTH - OUTER_MARGIN,
            y
        )
        y -= LINE_SPACING

    c.showPage()

c.save()
print("My Notebook (6x9) created successfully.")
