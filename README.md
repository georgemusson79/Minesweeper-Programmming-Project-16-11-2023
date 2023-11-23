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
### Use Case Diagrams
#### <u>Main Loop</u>
![Main Loop](use%20case%20diagrams/mainLoop.png)
- Main Loop diagram showing the control flow of the game
- `MainMenu`, `AttrSelectionMenu` and `MainGame` are all separate classes which all contain the loop function which should be called every frame
- The loop function to be called is determined by the gameState variable
- These classes should be independent from each other, if they need to share data, the data should be moved to a shared globals.py file, such as gamestate



### Class Diagrams
![Main Menu](use%20case%20diagrams/MainMenu%20Class%20diagram.png)
![Button](use%20case%20diagrams/Button%20Class%20diagram.png)
![GameSetup](use%20case%20diagrams/GameSetup%20Class%20diagram.png)
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
|`MainMenu.render()`| Renders buttons and background to screen when called which is displayed when surface.update is called | As stated in 'What is supposed to happen' | N/A|
|`MainMenu.update()`|Calls `MainMenu.render()` and also handles mouse button clicks|As stated in 'What is supposed to happen'| N/A|
|When start button is clicked Menu allowing user to define board settings is loaded| Currently goes straight into a preset game as attribute menu hasnt been created yet| Create an attribute menu and have gameState be set to GAME_SETUP|



#### <u>MainGame class</u>
| What is Being Tested | What is supposed to happen | What did Happen | What to do now |
|----------------------|----------------------------|-----------------|----------------|
|`MainGame.__init__()`|Sets surface if a surface is passed and sets a font to default system font|As is stated in "What is supposed to happen" however has not been tested in other operating systems (has been tested in windows 10) so setting default system font may not work| N/A|
|`MainGame.generateBoard()`|Sets board dimensions for rendering and board attributes, raise a special exception called BoardException if parameters are invalid types, also raise exception if minecount as less than width*height or width or height is less than 1|As stated in "What was supposed to happen"|N/A|
|Board renders to screen| `MainGame.boardDims` takes a `pygame.Rect` in the form (x,y,w,h): The top left corner of the board should be at the pixel position x,y and the board should be w pixels wide and h pixels tall| The board is w pixels wide and h pixels tall, however the board doesnt appear in the right position; when x is changed y also increases, changing y does nothing, this was tested by calling `mainGame.generateBoard(15,15,40,pygame.Rect(50,25,550,550))` in `main.py`| In MainGame.render there was a spelling mistake: `yPos=(y*tileHeight)+self.boardDims.x` was changed to `yPos=(y*tileHeight)+self.boardDims.y` which fixed the issue, the board now renders in the correct place
|Player left clicks on board| If selected tile isnt flagged, tile is opened, if tile has 0 mines around it, recursively open tiles around it until mine count is at least 1, if mine give game over screen| As stated apart from game over screen which hasnt been implemented yet| Add game over screen and gameOver variable|
|Player left clicks or right clicks off board but on screen| If nothing is pressed, do nothing, if there is a button on the screen handle button click| Buttons can't be added into the mainGame class yet so they dont work| Created an array called buttons, this list is iterated over in update() and button.render and button.handle clicks() so buttons should work|
|Do buttons in MainGame work| Button should render to screen,Left click and right click button functions should work without affecting the board|Test button was added in `MainGame.__init__` with the line `self.buttons=[Button(surface,0,500,300,100,"assets/img/button1.png",leftClickFunc=test)]` adding a button the bottom left of the screen with a left click test function that would print a line to console, this worked however right click didnt work |There was an issue in button.handleClick at the line `if btn[2]: self.onRightClick()` this was set to `if btn[1]: self.onRightClick()` which actually checks for middle click, not right click|
|Testing right click in MainGame| When button in MainGame is right clicked test function should run once per right click this is the code for the button: `self.buttons=[Button(surface,0,500,300,100,"assets/img/button1.png",rightClickFunc=test)]`| Test was successful, test function successfully outputed to console once per right click| N/A|
|

#### <u>gameState</u>
| What is Being Tested | What is supposed to happen | What did Happen | What to do now |
|----------------------|----------------------------|-----------------|----------------|
|Can gameState be updated from another .py file| gameState can be updated in MainMenu on start button click| gameState is successfully updated| N/A|
#### <u>Main Loop</u>
| What is Being Tested | What is supposed to happen | What did Happen | What to do now |
|----------------------|----------------------------|-----------------|----------------|
|Will window stay open| Main loop keeps running while running is true, constantly setting the main surface to black and rendering the surface to the screen| As stated in "Whats supposed to happen"|Handle user input
|Does exit button work| Clicking on the x in the top right closes the program| As stated in "whats supposed to happen"| Test game states|
|Will changing the gameState load the corect screen| Setting to mainMenu will load the mainMenu screen and allow the user to click the buttons, loading the MainGame will load the MainGame screen and allow user to play the game etc, this will work no matter when you change the gameState| What was stated in "whats supposed to happen" as long as the specified class is initialised, which happens at the start of the programm| Main Loop is ready, continue to add other game state classes
#### <u>GameSetup</u>
| What is Being Tested | What is supposed to happen | What did Happen | What to do now |
|----------------------|----------------------------|-----------------|----------------|
| Rendering to screen|Test background and submit button renders to screen, button renders in the bottom middle|Background renders but button renders to the right|`buttonX=self.surface.get_width()/2+(buttonWidth/2)` was changed to `buttonX=self.surface.get_width()/2-(buttonWidth/2)` now button renders in the correct place, text fields now need to be added|