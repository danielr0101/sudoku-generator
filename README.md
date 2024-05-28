﻿# sudoku-generator
 
Project for Generating Automatic Sudoku PNGs
This project allows the automatic creation of PNG files of sudokus, ready for the creation of books or PDF files.

Required Packages
Make sure you have the following packages installed:

dokusan 0.1.0
numpy 1.26.4
matplotlib 3.9.0
Sudoku Generation
The main script is generar.py. To generate the sudokus, modify the parameters as needed and run the script. The PNG files will be saved in the root folder, with the sudokus and their solutions.

Language Configuration
A variable is defined to select the language in which the sudokus will be generated:

1 for Spanish
2 for English
In this case, the program is configured to generate sudokus in Spanish: idioma = 1.

Initial Page Configuration
It is established that the sudokus will start generating from page 3 of the document. This is useful for organizing the layout of the sudokus in a file, such as a PDF or a sudoku book: pagina_inicial = 3.

Number of Sudokus per Level
The number of sudokus to be generated for each difficulty level is specified:

Easy: 2
Medium: 2
Hard: 2
Expert: 0
Diabolical: 0
