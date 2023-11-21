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
- [Python 3.11 Runtime Environment](https://www.python.org/downloads/)
- [Windows 10 or higher (has not been tested for other operating systems)](https://www.microsoft.com/en-gb/software-download/windows10)



## Design
### Main Loop
![Main Loop](use%20case%20diagrams/mainLoop.png)
- Main Loop diagram showing the control flow of the game
- `MainMenu`, `AttrSelectionMenu` and `MainGame` are all separate classes which all contain the loop function which should be called every frame
- The loop function to be called is determined by the gameState variable
- These classes should be independent from each other, if they need to share data, the data should be moved to a shared globals.py file, such as gamestate


## Implementation
### Testing
#### <u>Button class</u>
| What is Being Tested | What is supposed to happen | What did Happen | What to do now |
|----------------------|----------------------------|-----------------|----------------|
|`Button.setImg()` | If imgPath is valid, load the image and  save it to button.img, return True, if img is equal to None or a blank string return false, if the file was unable to load/invalid path, raise an Exception, tell the user that files are missing and close the program | if path is invalid exception is raised however program will close without informing the user | Add that functionality to the button and work on rendering the button to the screen |
| `Button.render()` | When called button is rendered when surface.update() is called assuming button.active is True, button is scaled and rendered on screen according to button. x,y,w,h values| What is stated in 'What is supposed to happen' | Write code for click functionality|
|`Button.isColliding()` | Returns true when function is called while cursor is inside the button, otherwise returns false | As stated in 'whats supposed to happen' | N/A |
|`Button.leftClick()`, `Button.rightClick()` and `Button.handleClick()` | leftClick and rightClick will check if there is a left click or right click function then if there are arguments, run with the arguments passed, if no right click or left click function has been specified do nothing, handleclick combines this with button.isColliding: it will run the related function if the user clicks and the cursor is inside the button, otherwise do nothing | As stated in 'whats supposed to happen ' |N/A|
| Does the button work | Button should be rendered to the screen when render function is called, if user clicks on button, button should call its function, if there is no function do nothing, if the user clicks outside of the button do nothing| As stated in 'What is supposed to happen' | Button is complete, move on to making the main menu |
#### <u>MainMenu class</u>
| What is Being Tested | What is supposed to happen | What did Happen | What to do now |
|----------------------|----------------------------|-----------------|----------------|
|Handling instances where assets e.g. images are missing| Check for missing files on start and if something is missing alert the user and prompt user to close the program,carried out at the start of the program| Exception is raised and program crashes| Implement a list containing a list of file paths, check if there is a valid item at the file path, if so prompt user and close program otherwise continue to main menu |
|`MainMenu.__init__()`| Defines buttons: a list that contains 2 buttons to start and setup game, the start button sets gameState to MAIN_GAME, setup game sets state to GAME_SETUP, allowing the user to set attributes for MainGame class, variable bg is also defined which loads the background image for the main menu into memory and scales it to fill the window | As stated in 'What is supposed to happen' however while set up button does set gameState to GAME_SETUP the screen goes blank as no game setup menu exists yet| Create a game setup menu|
|`MainMenu.render()`| Renders buttons and background to screen when called which is displayed when surface.update is called | As stated in 'What is supposed to happen' | N/A|
|`MainMenu.update()`|Calls `MainMenu.render()` and also handles mouse button clicks|As stated in 'What is supposed to happen'| N/A|

#### <u>MainGame class</u>
| What is Being Tested | What is supposed to happen | What did Happen | What to do now |
|----------------------|----------------------------|-----------------|----------------|
|`MainGame.__init__()`|Sets surface if a surface is passed and sets a font to default system font|As is stated in "What is supposed to happen" however has not been tested in other operating systems (has been tested in windows 10) so setting default system font may not work| N/A|
|`MainGame.generateBoard()`|Sets board dimensions for rendering and board attributes, raise a special exception called BoardException if parameters are invalid types, also raise exception if minecount as less than width*height or width or height is less than 1|As stated in "What was supposed to happen"|N/A|
|`MainGame.scatterMines()`|Should place mines randomly around the board based on what MainGame.mineCount is set to, must be able to check if the randomly selected position is on the board and must also be able to check that the position isn't on an open tile or a tile that is already a mine, should be able to handle all board sizes, except where there are more mines than available tiles, in which case an exception should be raised|As stated in "What is supposed to happen", if there are more mines than tiles, exception is raised in generateBoard|N/A|