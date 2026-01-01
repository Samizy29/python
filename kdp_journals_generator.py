from fpdf import FPDF
import os

# Create folder to save all PDFs
folder = "kdp_journals"
os.makedirs(folder, exist_ok=True)

# Standard KDP 6x9 inches = 432x648 points approx for PDF units (1 point = 1/72 inch)
PAGE_WIDTH = 432
PAGE_HEIGHT = 648
MARGIN = 36  # 0.5 inch margin

# Helper function to create blank lines
def draw_lines(pdf, num_lines=20):
    for _ in range(num_lines):
        pdf.cell(0, 12, "_"*60, ln=True)

# --------------------------
# 1. Daily Journal
pdf = FPDF(format=(PAGE_WIDTH, PAGE_HEIGHT))
pdf.set_auto_page_break(auto=True, margin=MARGIN)
pdf.set_font("Arial", "", 12)
for day in range(1, 31):
    pdf.add_page()
    pdf.set_font("Arial", "B", 16)
    pdf.cell(0, 10, f"Daily Journal - Day {day}", ln=True, align="C")
    pdf.ln(10)
    pdf.set_font("Arial", "", 12)
    draw_lines(pdf, 25)
pdf.output(os.path.join(folder, "daily_journal.pdf"))

# --------------------------
# 2. Gratitude Journal
prompts = ["I am thankful for:", "A positive thing that happened today:", "Someone who made me smile:"]
pdf = FPDF(format=(PAGE_WIDTH, PAGE_HEIGHT))
for day in range(1, 31):
    pdf.add_page()
    pdf.set_font("Arial", "B", 16)
    pdf.cell(0, 10, f"Gratitude Journal - Day {day}", ln=True, align="C")
    pdf.ln(10)
    pdf.set_font("Arial", "", 12)
    for prompt in prompts:
        pdf.cell(0, 10, prompt, ln=True)
        draw_lines(pdf, 3)
pdf.output(os.path.join(folder, "gratitude_journal.pdf"))

# --------------------------
# 3. Habit Tracker
habits = ["Exercise", "Meditation", "Read", "Water Intake"]
pdf = FPDF(format=(PAGE_WIDTH, PAGE_HEIGHT))
pdf.set_font("Arial", "", 12)
pdf.add_page()
pdf.set_font("Arial", "B", 16)
pdf.cell(0, 10, "Habit Tracker - 30 Days", ln=True, align="C")
pdf.ln(10)
pdf.set_font("Arial", "", 12)
for habit in habits:
    pdf.cell(40, 10, habit)
    for day in range(1, 31):
        pdf.cell(5, 10, "□", align="C")
    pdf.ln(10)
pdf.output(os.path.join(folder, "habit_tracker.pdf"))

# --------------------------
# 4. Fitness Journal
exercises = ["Date", "Workout", "Sets", "Reps", "Weight", "Notes"]
pdf = FPDF(format=(PAGE_WIDTH, PAGE_HEIGHT))
pdf.set_font("Arial", "", 12)
for day in range(1, 31):
    pdf.add_page()
    pdf.set_font("Arial", "B", 16)
    pdf.cell(0, 10, f"Fitness Journal - Day {day}", ln=True, align="C")
    pdf.ln(10)
    pdf.set_font("Arial", "B", 12)
    for e in exercises:
        pdf.cell(30, 10, e, border=1)
    pdf.ln(10)
    for _ in range(10):
        for _ in exercises:
            pdf.cell(30, 10, "", border=1)
        pdf.ln(10)
pdf.output(os.path.join(folder, "fitness_journal.pdf"))

# --------------------------
# 5. Meal Planner
meals = ["Breakfast", "Lunch", "Dinner", "Snacks", "Calories", "Notes"]
pdf = FPDF(format=(PAGE_WIDTH, PAGE_HEIGHT))
for day in range(1, 31):
    pdf.add_page()
    pdf.set_font("Arial", "B", 16)
    pdf.cell(0, 10, f"Meal Planner - Day {day}", ln=True, align="C")
    pdf.ln(10)
    pdf.set_font("Arial", "B", 12)
    for m in meals:
        pdf.cell(30, 10, m, border=1)
    pdf.ln(10)
    for _ in range(10):
        for _ in meals:
            pdf.cell(30, 10, "", border=1)
        pdf.ln(10)
pdf.output(os.path.join(folder, "meal_planner.pdf"))

# --------------------------
# 6. Reading Journal
sections = ["Title:", "Author:", "Start Date:", "Finish Date:", "Rating (1-5):", "Notes:"]
pdf = FPDF(format=(PAGE_WIDTH, PAGE_HEIGHT))
for book in range(1, 21):
    pdf.add_page()
    pdf.set_font("Arial", "B", 16)
    pdf.cell(0, 10, f"Reading Journal - Book {book}", ln=True, align="C")
    pdf.ln(10)
    pdf.set_font("Arial", "", 12)
    for sec in sections:
        pdf.cell(0, 10, sec, ln=True)
        draw_lines(pdf, 4)
pdf.output(os.path.join(folder, "reading_journal.pdf"))

# --------------------------
# 7. Sudoku Puzzle Book
pdf = FPDF(format=(PAGE_WIDTH, PAGE_HEIGHT))
for puzzle in range(1, 21):
    pdf.add_page()
    pdf.set_font("Arial", "B", 16)
    pdf.cell(0, 10, f"Sudoku Puzzle {puzzle}", ln=True, align="C")
    pdf.ln(10)
    pdf.set_font("Arial", "", 12)
    for i in range(9):
        pdf.cell(0, 10, "□ □ □ □ □ □ □ □ □", ln=True)
pdf.output(os.path.join(folder, "sudoku_book.pdf"))

# --------------------------
# 8. Travel Journal
sections = ["Destination:", "Date:", "Highlights:", "Memorable Moments:", "Photos (paste here):"]
pdf = FPDF(format=(PAGE_WIDTH, PAGE_HEIGHT))
for trip in range(1, 21):
    pdf.add_page()
    pdf.set_font("Arial", "B", 16)
    pdf.cell(0, 10, f"Travel Journal - Trip {trip}", ln=True, align="C")
    pdf.ln(10)
    pdf.set_font("Arial", "", 12)
    for sec in sections:
        pdf.cell(0, 10, sec, ln=True)
        draw_lines(pdf, 4)
pdf.output(os.path.join(folder, "travel_journal.pdf"))

# --------------------------
# 9. Coloring Book
pdf = FPDF(format=(PAGE_WIDTH, PAGE_HEIGHT))
for page in range(1, 21):
    pdf.add_page()
    pdf.set_font("Arial", "B", 16)
    pdf.cell(0, 10, f"Coloring Page {page}", ln=True, align="C")
    pdf.ln(20)
    for _ in range(5):
        pdf.cell(0, 30, "⬜ ⬜ ⬜ ⬜ ⬜", ln=True)
pdf.output(os.path.join(folder, "coloring_book.pdf"))

# --------------------------
# 10. Academic Planner
subjects = ["Math", "Science", "History", "English", "Other"]
pdf = FPDF(format=(PAGE_WIDTH, PAGE_HEIGHT))
for week in range(1, 5):
    pdf.add_page()
    pdf.set_font("Arial", "B", 16)
    pdf.cell(0, 10, f"Weekly Academic Planner - Week {week}", ln=True, align="C")
    pdf.ln(10)
    pdf.set_font("Arial", "", 12)
    for subj in subjects:
        pdf.cell(40, 10, subj)
        for day in range(1, 8):
            pdf.cell(15, 10, "□", align="C")
        pdf.ln(10)
pdf.output(os.path.join(folder, "academic_planner.pdf"))

print("All 10 journals generated in folder:", folder)
