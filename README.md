# Programmming-Project-16-11-2023

## Description
The Aim of this project is to:
- Make a clone of the game "MineSweeper", which will allow the user to save and load the state of their game as well as let them set the dimensions of the board and mine count.

## Criteria
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
- If the left clicks on a tile and it is a mine the game should end and prompt the user to either try again or return to the main menu
- There should be a counter indicating the amount of mines there are on the board which decreases/increases when the player places/removes a flag
- This is to indicate how close the player is to finishing the game

- Classes are an essential part of this task: A class will be made for each game state and for each tile at the minimum
- A container is required: At least one container will be used in the form of a 2D array that will represent the board by storing the tiles
- The program must be able to read from and write to a file: This will be featured when loading and saving the state of the game
- The program must allow for user input: This will be achieved by having buttons for the user to click and text fields for the user to input the dimensions of the board
- The program must used loops and try catch blocks: A main loop will be created which will run every frame, handling rendering, user input and game updates, there will also be try-catch blocks when loading a file to ensure that if the user tries to load an invalid file it wont crash the program



## How to use
- Run the program by running `main.py`
- Command line arguments can be passed to set a custom resolution - the first argument is window width and window height

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

![Main Menu](use%20case%20diagrams/MainMenuDiagram.png)
- Main menu is the first state of the game and allows the user to play and load a game
![Button](use%20case%20diagrams/ButtonDiagram.png)
- Button provides pictures for the user to click on which will run a function
![GameSetup](use%20case%20diagrams/GameSetupDiagram.png)
- GameSetup allows for the user to set the attributes for the game board
![Label](use%20case%20diagrams/LabelDiagram.png)
- Label allows for rendering text to the screen
![TextField](use%20case%20diagrams/TextfieldDiagram.png)
- TextField allows user to input text
![MainGame](use%20case%20diagrams/MainGameDiagram.png)
![Game over Screen](use%20case%20diagrams/GameOverOverlay.png)

## Implementation
### Testing
#### <u>Button class</u>
| What is Being Tested | What is supposed to happen | What did Happen | What to do now |Success?|
|----------------------|----------------------------|-----------------|----------------|--------|
|`Button.setImg()` | If imgPath is valid, load the image and  save it to button.img, return True, if img is equal to None or a blank string return false |As stated in "what is supposed to happen"| Work on rendering the button to the screen | Y|
| `Button.render()` | When called button is rendered when surface.update() is called assuming button.active is True, button is scaled and rendered on screen according to button. x,y,w,h values| What is stated in 'What is supposed to happen' | Write code for click functionality| Y|
|`Button.isColliding()` | Returns true when function is called while cursor is inside the button, otherwise returns false | As stated in 'whats supposed to happen' | N/A | Y|
|`Button.leftClick()`, `Button.rightClick()` and `Button.handleClick()` | leftClick and rightClick will check if there is a left click or right click function then if there are arguments, run with the arguments passed, if no right click or left click function has been specified do nothing, handleclick combines this with button.isColliding: it will run the related function if the user clicks and the cursor is inside the button, otherwise do nothing | As stated in 'whats supposed to happen ' |N/A|Y|
| Does the button work | Button should be rendered to the screen when render function is called, if user clicks on button, button should call its function, if there is no function do nothing, if the user clicks outside of the button do nothing| As stated in 'What is supposed to happen' | Button is complete, move on to making the main menu |Y|
#### <u>MainMenu class</u>
| What is Being Tested | What is supposed to happen | What did Happen | What to do now |Success?|
|----------------------|----------------------------|-----------------|----------------|--------|
|`MainMenu.render()`| Renders buttons and background to screen when called which is displayed when surface.update is called | As stated in 'What is supposed to happen' | N/A|Y|
|`MainMenu.update()`|Calls `MainMenu.render()` and also handles mouse button clicks|As stated in 'What is supposed to happen'| N/A|Y|
Main menu start button|When start button is clicked Menu allowing user to define board settings is loaded| Currently goes straight into a preset game as attribute menu hasnt been created yet| Create an attribute menu and have gameState be set to GAME_SETUP|N|
Main menu start button 2 | When start button is clicked Menu allowing user to define board settings is loaded| Loads game setup menu allowing user to enter details and start game | Add load game button to main menu|Y|



#### <u>MainGame class</u>
| What is Being Tested | What is supposed to happen | What did Happen | What to do now |Success?|
|----------------------|----------------------------|-----------------|----------------|--------|
|`MainGame.__init__()`|Sets surface if a surface is passed and sets a font to default system font|As is stated in "What is supposed to happen" however has not been tested in other operating systems (has been tested in windows 10) so setting default system font may not work| N/A| Y|
|`MainGame.generateBoard()`|Sets board dimensions for rendering and board attributes, raise a special exception called BoardException if parameters are invalid types, also raise exception if minecount as less than width*height or width or height is less than 1|As stated in "What was supposed to happen"|N/A|Y|
|Board renders to screen| `MainGame.boardDims` takes a `pygame.Rect` in the form (x,y,w,h): The top left corner of the board should be at the pixel position x,y and the board should be w pixels wide and h pixels tall| The board is w pixels wide and h pixels tall, however the board doesnt appear in the right position; when x is changed y also increases, changing y does nothing, this was tested by calling `mainGame.generateBoard(15,15,40,pygame.Rect(50,25,550,550))` in `main.py`| In MainGame.render there was a spelling mistake: `yPos=(y*tileHeight)+self.boardDims.x` was changed to `yPos=(y*tileHeight)+self.boardDims.y` which fixed the issue, the board now renders in the correct place| Y (fixed)
|Player left clicks on board| If selected tile isnt flagged, tile is opened, if tile has 0 mines around it, recursively open tiles around it until mine count is at least 1, if mine give game over screen| As stated apart from game over screen which hasnt been implemented yet| Add game over screen and gameOver variable|Incomplete|
|Player left clicks or right clicks off board but on screen| If nothing is pressed, do nothing, if there is a button on the screen handle button click| Buttons can't be added into the mainGame class yet so they dont work| Created an array called buttons, this list is iterated over in update() and button.render and button.handle clicks() so buttons should work|Y(fixed)|
|Do buttons in MainGame work| Button should render to screen,Left click and right click button functions should work without affecting the board|Test button was added in `MainGame.__init__` with the line `self.buttons=[Button(surface,0,500,300,100,"assets/img/button1.png",leftClickFunc=test)]` adding a button the bottom left of the screen with a left click test function that would print a line to console, this worked however right click didnt work |There was an issue in button.handleClick at the line `if btn[2]: self.onRightClick()` this was set to `if btn[1]: self.onRightClick()` which actually checks for middle click, not right click|Y (fixed)|
|Testing right click in MainGame| When button in MainGame is right clicked test function should run once per right click this is the code for the button: `self.buttons=[Button(surface,0,500,300,100,"assets/img/button1.png",rightClickFunc=test)]`| Test was successful, test function successfully outputed to console once per right click| N/A|Y|
|Player left clicks on board 2| As stated in player left clicks on board| As stated in "what is supposed to happen"| N/A|Y|


#### <u>gameState</u>
| What is Being Tested | What is supposed to happen | What did Happen | What to do now |Success?|
|----------------------|----------------------------|-----------------|----------------|--------|
|Can gameState be updated from another .py file| gameState can be updated in MainMenu on start button click| gameState is successfully updated| N/A|Y|
#### <u>Main Loop</u>
| What is Being Tested | What is supposed to happen | What did Happen | What to do now |Success?|
|----------------------|----------------------------|-----------------|----------------|--------|
|Will window stay open| Main loop keeps running while running is true, constantly setting the main surface to black and rendering the surface to the screen| As stated in "Whats supposed to happen"|Handle user input|Y|
|Does exit button work| Clicking on the x in the top right closes the program| As stated in "whats supposed to happen"| Test game states|Y|
|Will changing the gameState load the corect screen| Setting to mainMenu will load the mainMenu screen and allow the user to click the buttons, loading the MainGame will load the MainGame screen and allow user to play the game etc, this will work no matter when you change the gameState| What was stated in "whats supposed to happen" as long as the specified class is initialised, which happens at the start of the programm| Main Loop is ready, continue to add other game state classes|Y|

#### <u>TextField</u>
| What is Being Tested | What is supposed to happen | What did Happen | What to do now |Success?|
|----------------------|----------------------------|-----------------|----------------|--------|
|Render to screen|Box gets rendered to screen based on x,y,w,h values| As stated in "what is supposed to happen"| Allow for text to be added and rendered|Y|
|Allow for text to be entered into box|If the user has their cursor over the box they can enter text up to the maxCharlimit, only characters that are allowed will be entered otherwise do nothing|Exception raised at line `for key,state in enumerate(keys):` in `TextField.py` at `handleKeys()` as `keys=pygame.key.get_pressed()` can't be enumerated over| For loop has been updated to be a range based loop between ascii characters 0-255, text is rendered correctly though|N|
|Handle text input|Backspace deletes text, typing text adds it to the box| Backspace works however normal characters dont work and cause a crash| the issue was key was a numeric value being checked to see if it was in a string, now the key is converted to a character using `pygame.get_name(key)` which fixed it|Y (fixed)|
|Pressing a key| If one key is pressed one character is created| If you tap it it creates one character however if you hold it for slightly too long it'll add too many characters| Add a cooldown time between character presses so holding the key doesnt create multiple characters|Y (fixed)|
|Only type if user has clicked on the box| If the users last click was on the text box and the user presses a key, enter text otherwise dont| As stated in "whats supposed to happen"| N/A|Y|
|Scale text| Each character scaled to be half the height of the box, if the pixel width of the inputted data is bigger than the text box scale to fit| As stated in "whats supposed to happen"| N/A|Y|
|Scale text test 2| As stated above| As stated in "what is supposed to happen" however if there is too much text it becomes hard to read, however since these textfields are only being used once with a small number of characters this isnt an issue for this project| TextField complete|Y|


#### <u>Label</u>
| What is Being Tested | What is supposed to happen | What did Happen | What to do now |Success?|
|----------------------|----------------------------|-----------------|----------------|--------|
|Label renders to screen| Text appears on screen at x,y position being w wide and h tall| As stated in "Whats supposed to happen"| Test different colours|Y|
|Text can be set to different colour|Run `setText()` or constructor setting colour to rgb value such as `(255,0,0)`. Text should be red| As stated in "Whats supposed to happen"| Label is finished|Y|

#### <u>GameSetup</u>
| What is Being Tested | What is supposed to happen | What did Happen | What to do now |Success?|
|----------------------|----------------------------|-----------------|----------------|--------|
| Rendering to screen|Test background and submit button renders to screen, button renders in the bottom middle|Background renders but button renders to the right|`buttonX=self.surface.get_width()/2+(buttonWidth/2)` was changed to `buttonX=self.surface.get_width()/2-(buttonWidth/2)` now button renders in the correct place, text fields now need to be added| Y (fixed)|
|Rendering to screen 2| 3 text fields render to screen with text above indicating what they do, with a submit button in the bottom center of the screen| As stated in "what is supposed to happen"| N/A|Y|
|Handle user input - inputting any non-numeric character| Character should be ignored and nothing is entered| As stated in "what is supposed to happen"| N/A|Y|
|Handle user input - inputting invalid numbers | Program displays error in consolen | Error is displayed in console, entering nothing also causes a crash |Handle when user enters nothing |N|
|Handle user input - user tries to write more than 2 characters in board width and board height and more than 4 characters in mine count text field | Any extra input is ignored unless user presses backspace to delete the end character | As stated in  "what is supposed to happen"| N/A|Y|
|Handle user input - Enter nothing| Error outputted to console and allow user to input value| As stated in "What is supposed to happen"| GameSetup complete|Y|

#### <u>MainGame class- handling game overs</u>
| What is Being Tested | What is supposed to happen | What did Happen | What to do now |Success?|
|----------------------|----------------------------|-----------------|----------------|--------|
|User left clicks on mine|Game over screen pops up from the bottom saying "Game Over you lose" and presents the option to either retry or quit| As stated in "what is supposed to happen"| Testing if the user wins|Y|
|User opens all correct tiles (without mines) and places all flags|Game over screen pops up from the bottom saying "Game Over you win" and presents the option to either retry or quit| as stated in "whats supposed to happen"| Add functionality to buttons|Y|
|User opens all correct tiles without placing all flags/user places all flags without opening all correct tiles| Nothing happens| Nothing happens| N/A| Y|
|User clicks on retry| When user clicks on retry board should refresh with same board width, height and mine count but mines in different places| On click nothing happens| Button clicks on the game over screen were never being checked for, update function was created for gameOverOverlay which is now checked every frame while gameOver is true|Y (fixed)|
|User clicks quit| When user clicks quit they will be taken back the main menu, from there the game should operate as if it were opened for the first time| As stated in "whats supposed to happen" however in game setup the attributes are still in the text fields, although it is unintentional it will be left in because it means if the user wants to play the same game with the same attributes they can and if they want to change the attributes they still can, so this doesnt cause any problems|N/A|Y|
|What happens when a user clicks on a mine that has been flagged| Nothing happens| Mine is activated and user gets game over| Fixed bug by moving where the game checks if a tile is a mine into openTile, after checking if the tile has been flagged|Y (fixed)|
|User tries to click tile or buttons while game over screen is active| Nothing happens | Nothing happens|Game over screen complete|Y|

#### <u>MainGame class - flag counter</u>
| What is Being Tested | What is supposed to happen | What did Happen | What to do now |Success?|
|----------------------|----------------------------|-----------------|----------------|--------| 
|Counter renders to screen| Rendered to bottom middle of screen stating mine count at the start| As stated in "whats supposed to happen"| Test placing and removing flags|Y|
|User places flag| Flag counter decreases, will go into negative numbers if possible | As stated in "what is supposed to happen"| Test removing a flag|Y|
|User removes flag from board| Counter increases| Counter increases| Flag counter complete|Y|

#### <u>MainGame class - Save game and quit buttons</u>
| What is Being Tested | What is supposed to happen | What did Happen | What to do now |Success?|
|----------------------|----------------------------|-----------------|----------------|--------| 
|Quit button|Brings up game over screen saying "You lose"| As stated in "whats supposed to happen"|N/A|Y|
|Save game - saving to file| Opens file explorer and writes a .save file containing binary game data to the location specified| Exception: `TypeError: write() argument must be str, not bytes`, this was caused by opening the file in `w+` mode rather than `w+b` for handling binary|Try with `w+b` instead|N|
|Save game - saving to file 2| As stated above| As stated in "whats supposed to happen"|N/A|Y|
|Save game - user selects a file that already exits| Ask user if they want to overwrite if they say yes then save| As stated in "whats supposed to happen"| N/A| Y|
|Save game - user cancels without selecting file| File explorer closes and progam stops trying to save|Program crashes with `No such file or directory ''`|Program checks for blank string and if there is one returns false, if there is an exception an error is raised but program doesnt crash|Y|
|Load file - user attempts to load a saved file| State is loaded and program continues into main game with the loaded boar| As stated in "what is supposed to happen"| Test invalid/no file selected|Y|
|Load file - the user cancels before selecting a file| No error is outputted and program returns to main menu| As stated in "what is supposed to happen"| Test invalid files|Y|
|Load file - user loads a .save file that doesnt contain the correct data| Error outputted saying "Unable to load the file!" to console and program returns to main menu| As stated in "what is supposed to happen"| Save/load functionality is complete - All criteria met, program is complete|Y|
|User has opened some of the board and placed a few flags down then saves in a new file and loads| Game loads save correctly| Game freezes when trying to left click| Normally the game places mines after the users first turn, which is identified with openCount, openCount wasnt being saved to the file so when the user would load up the file the game would think it's the player's first move even when it wasnt causing a freeze, this has been fixed by passing openCount into the file|Y (fixed)|


## Critiques
Although this program generally works, there are a number of issues with it and the way it was developed:

- This program was only tested on one operating system and so may not function correctly on all machines, especially touchscreen devices
- The game does get difficult to control when setting the width and height of the board to a very high amount due to the tiles being so small and hard to click on, this was somewhat mitigated by limiting the width and height to 99 however it still can make it hard to play, in the future this could be avoided by allowing the user to zoom in on the board.
- Another issue is that error messages may be slightly obscured due to them appearing in the console and not in the game itself, this was done due to time constraints, however given more time it would be useful to display errors in the gui so that it's easier for the user to use the program.
- The resolution is difficult to change, being only modifiable by passing the resolution as an argument on startup, it would be helpful to have a menu in the game for changing the resolution.
