# Programmming-Project-16-11-2023

## Description
The Aim of this project is to:
- Make a clone of the game "MineSweeper" in python, using the GUI library PyGame
- That will include a means of saving and loading the state of the game
- There will also be a means of setting custom parameters for the board
- Such parameters include the number of mines and the width of height of the board
- There will be a Main Menu that will give the user the option to start a new game or load a previous game
- In the actual game itself there will be an option to save the state of the board or to exit and save
- The board should be resizeable and should scale according to the size of the window
- If the user right clicks on the board it will place down a flag at the position which prevents that tile from being opened
- If the user right clicks at that point again it will remove the flag
- If the player left clicks on the board it should open the tile and reveal how many mines there are around the tile
- If the left clicks on a tile and it is a mine the game should end and prompt the user to wither try again or return to the main menu
- There should be a counter indicating the amount of mines there are on the board which decreases/increases when the player places/removes a flag
- This is to indicate how close the player is to finishing the game

## Requirements
- [Pygame](https://pypi.org/project/pygame/)
- [Python 3.0 Runtime Environment](https://www.python.org/downloads/)



## Design
### Main Loop
![Main Loop](use%20case%20diagrams/mainLoop.png)
- Main Loop diagram showing the control flow of the game
- `MainMenu`, `AttrSelectionMenu` and `MainGame` are all separate classes which all contain the loop function which should be called every frame
- The loop function to be called is determined by the gameState variable
- These classes should be independent from each other, if they need to share data, the data should be moved to a shared globals.py file, such as gamestate


## Implementation
### Testing
| What is Being Tested | What is supposed to happen | What did Happen | What to do now |
|----------------------|----------------------------|-----------------|----------------|

