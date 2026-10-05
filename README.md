# Genetic Algorithm Exam Scheduling

A Python application that creates an exam timetable by minimizing student scheduling conflicts with a Genetic Algorithm.

## Features

- Loads students, courses, and exam slots from the included Excel dataset.
- Generates course-to-slot schedules with a Genetic Algorithm.
- Penalizes same-slot conflicts, heavy same-day workloads, dense consecutive-day schedules, and use of more than five exam days.
- Prints the best fitness and final schedule and displays a convergence plot.

## Technologies & Tools

- **Python** — application and Genetic Algorithm implementation.
- **pandas** — reads the workbook data into the application.
- **openpyxl** — provides Excel workbook support for pandas.
- **Matplotlib** — plots the best fitness across generations.

## Algorithm

The application starts with 100 random chromosomes, where each gene assigns one course to one of 18 exam slots. It evaluates schedules with penalty-based fitness, selects parents through roulette-wheel selection, applies single-point crossover, and mutates genes at a 5% rate. After 200 generations, it returns the best schedule found.

## Prerequisites

- Python 3
- pip

## Getting Started

```bash
git clone https://github.com/ElyasNajeh/ExamSchedulingGA.git
cd ExamSchedulingGA
python -m pip install -r requirements.txt
python main.py
```

## Project Structure

```text
ExamSchedulingGA/
|-- data/
|   `-- ga_exam_timetable_dataset.xlsx  # Required scheduling input
|-- docs/
|   `-- COMP338_Project1.docx           # Project report
|-- geneticAlgorithm/
|   |-- fitness.py                      # Schedule penalties and fitness
|   `-- genetic_algorithm.py            # GA operations and execution loop
|-- models/
|   |-- chromosome.py                   # Candidate schedule model
|   |-- course.py                       # Course model
|   |-- slot.py                         # Exam-slot model
|   `-- student.py                      # Student model
|-- data_loader.py                      # Excel data loading
|-- main.py                             # Application entry point
|-- README.md
`-- requirements.txt
```

## Architecture

`main.py` coordinates the application: it loads workbook data through `data_loader.py`, runs the algorithm in `geneticAlgorithm/`, prints the resulting schedule, and plots convergence. The `models/` classes represent students, courses, slots, and chromosomes, while `data/` contains the required input and `docs/` contains the supporting project report.
