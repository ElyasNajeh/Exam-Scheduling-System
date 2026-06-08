# Genetic Algorithm Exam Scheduling

This project implements a Genetic Algorithm (GA) to solve the Exam Timetabling Problem.

The goal is to assign each course to an exam slot while minimizing scheduling conflicts and penalties.

## Constraints

### Hard Constraints
- No student can have two exams at the same time.
- No student can have more than two exams in the same day.

### Soft Constraints
- Avoid assigning two exams to the same student on the same day.
- Avoid assigning four exams within two consecutive days.
- Minimize the number of exam days used.

## Genetic Algorithm Components

- Population Generation
- Fitness Evaluation
- Roulette Wheel Selection
- Single Point Crossover
- Mutation

## Project Structure

```
ExamSchedulingGA/
│
├── geneticAlgorithm/
│   ├── fitness.py
│   └── genetic_algorithm.py
│
├── models/
│   ├── chromosome.py
│   ├── course.py
│   ├── slot.py
│   └── student.py
│
├── data_loader.py
├── main.py
└── ga_exam_timetable_dataset.xlsx
```

## Dataset

The dataset contains:

- 95 Students
- 22 Courses
- 18 Available Exam Slots
- 6 Exam Days

## Run

```bash
python main.py
```

The program generates an exam schedule, displays the best fitness value found, prints the final schedule, and plots the convergence of the Genetic Algorithm.