# Programmming-Project-16-11-2023

## Description
The Aim of this project is to:
- Make a clone of the game "MineSweeper" in python, using the GUI library PyGame
- That will include a means of saving and loading the state of the game
- There will also be a means of setting custom parameters for the board
- Such parameters include the number of mines and the width of height of the board
- There will be a Main Menu that will give the user the option to start a new game or load a previous game
- In the actual game itself there will be an option to save the state of the board or to exit and save

## Requirements
- [Pygame](https://pypi.org/project/pygame/)
- [Python 3.0 Runtime Environment](https://www.python.org/downloads/)



## Design
### Main Loop Use Case Diagram
![Main Loop](use%20case%20diagrams/mainLoop.png)
- Main Loop diagram showing the control flow of the game, MainMenu
- AttrSelectionMenu and MainGame are all separate classes which all contain the loop function which should be called every frame
- These classes should be independent from each other, if they need to share data, the data should be moved to a shared globals.py file, such as gamestate