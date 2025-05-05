import pygame, pygame.locals, random, dill

class Game():
    def __init__(self, 
                    backgroundImage,
                    default_screenSize         = None,
                    default_inputBoxSize       = None,
                    default_centerInput        = None,
                    default_positionName       = None,
                    default_positionStart      = None,
                    default_positionGameOver   = None,
                    default_positionEsc        = None,
                    default_positionRestart    = None,
                    default_positionHighScores = None,
                    default_positionFinalScore = None,
                    default_positionScoreList  = None,
                    default_positionPlayers    = None,
                    default_positionBack       = None,
                    default_score              = None,
                    default_fontName           = None,
                    default_fontSize           = None
                ):
        '''
            Input:
                backgroundImage             : the path of the background image. Example: "Backgrounds/space.png"
                    string                  

                default_sceenSize           : window dimension (default (800,600) )
                    tuple    

                default_inputBoxSize        : input box dimension (default (400, 250, 140, 32) )
                    tuple           

                default_centerInput         : position of input text inside inputBox (default (5,5))
                    tuple

                default_positionName        : position of the insert name button (default (300,300) )
                    tuple 

                default_positionStart       : position of the start button (default (300,300) )
                    tuple 
                    
                default_positionGameOver    : position of the game over text (default (300,100) )
                    tuple 

                default_positionEsc         : position of the esc button (default (600,550) )
                    tuple                     

                default_positionRestart     : position of the restart button (default (300,350) )
                    tuple 

                default_positionHighScores  : position of the high scores text ( default (300, 100))
                    tuple                    

                default_positionFinalScore  : position of score text in the game over menu (default (300,200) )
                    tuple

                default_positionScoreList   : position of score list text (default (300,400) )
                    tuple         
                    
                default_positionPlayers     : position of players list (name ----- score) (default (300,150) )
                    tuple 

                default_positionBack        : position of the "back to start menu" button (default (300,550) )
                    tuple           
                
                default_score               : starting score (default (0) )
                    tuple
                
                default_fontName            : name of font used for text (default ("arial"))
                    string

                default_fontSize            : size of the text (default (30))
                    tuple

        '''

        if default_screenSize            is None : self.screenSize                    = (800,600)
        if default_inputBoxSize          is None : self.default_inputBoxSize          = (400,250, 140,30)
        if default_centerInput           is None : self.default_centerInput           = (5,5)
        if default_positionName          is None : self.default_positionName          = (300,250)
        if default_positionStart         is None : self.default_positionStart         = (300,350)
        if default_positionGameOver      is None : self.default_positionGameOver      = (300,100)
        if default_positionEsc           is None : self.default_positionEsc           = (600,550)
        if default_positionRestart       is None : self.default_positionRestart       = (300,350)
        if default_positionHighScores    is None : self.default_positionHighScores    = (300,100)
        if default_positionFinalScore    is None : self.default_positionFinalScore    = (300,200)
        if default_positionScoreList     is None : self.default_positionScoreList     = (300,400)
        if default_positionPlayers       is None : self.default_positionPlayers       = (300,150)
        if default_positionBack          is None : self.default_positionBack          = (300,550)    
        if default_score                 is None : self.default_score                 = 0
        if default_fontName              is None : self.default_fontName              = "arial"
        if default_fontSize              is None : self.default_fontSize              = 30

        self.backgroundImage    =   backgroundImage

        pygame.init()
        self.clock = pygame.time.Clock()


    #   S A V E   T O   B I N A R Y   F I L E   ----------------------------------------------------------------------------------
    def save_to_binaryFile(self, obj, filename, path=''):
        '''
            Save object to file

            Input:
                obj         :   object to save (e.g. object form class, list, np.array, dict, ...)
                    object
                filename    :   file name
                    str
                
                path        :   path where file is saved
                    str
        '''

        name = path + filename
        file = open(name, "wb")
        dill.dump( obj, file)  # file
        file.close()

    #   L O A D   F R O M   B I N A R Y   F I L E   ------------------------------------------------------------------------------
    def load_from_binaryFile(self, filename, path=''):
        '''
            Save object to file

            Input:
                filename    :   file name
                    str
                
                path        :   path where file is saved
                    str
        '''

        name = path+filename
        file =  open( name, 'rb')
        obj = dill.load(file)
        file.close()

        return obj

    #   S E T   T I M E R   --------------------------------------------------------------------------------------------------   
    def setTimer (self, milliseconds):
        '''
            Set the timer event
                Input:
                    milliseconds    : milliseconds to which the timer will get off
        '''
        self.timer = pygame.event.custom_type()
        pygame.time.set_timer(self.timer, milliseconds)

    
    
    #   S E T   R A N D O M   V A R I A B L E S   ----------------------------------------------------------------------------   
    def setRandomVariables (self):
        '''
            Set random value to variables

        '''
        self.x = random.randrange(0, self.screenSize[0]/2 + 1)
        self.y = random.randrange(self.screenSize[1]/2, self.screenSize[1] - 200)

    #   S E T   F O N T   ---------------------------------------------------------------------------------------------------   
    def setFont(self, fontText, fontSize):
        '''
            Set the font used for text
                Input:
                    fontText    : font of the text
                        string

                    fontSize    : size of the font
                        tuple
        '''
        self.font = pygame.font.SysFont( fontText, fontSize )

    #   S E T   B A C K G R O U N D   I M A G E ------------------------------------------------------------------------------
    def setBackgroundImage(self, image):
        '''
            Set backgound image
                Input:
                    image       : path of the background image 
                        string
        '''
        loadedImage            = pygame.image.load( image ).convert_alpha()
        self.surfaceBackgroung = pygame.transform.smoothscale(loadedImage, self.screen.get_size())
        #   drawing background image on the screen
        self.screen.blit((self.surfaceBackgroung), (0,0))

    #   G E T   I N P U T   B O X --------------------------------------------------------------------------------------------
    def getInputBox(self):
        '''
            Set box for input player name
        '''
        pygame.draw.rect(self.screen, (255,255,255), self.inputRect)
        self.textSurface = self.baseFont.render(self.userText, True, (0, 0, 0)) 
      
        # render at position stated in arguments 
        self.screen.blit(self.textSurface, (self.inputRect.x + self.default_centerInput[0], self.inputRect.y + self.default_centerInput[1])) 
      
#   S T A R T   M E N U   ------------------------------------------------------------------------------------------------    
    def startMenu(self):
        '''
            Draw start menu - start button
        
        '''
        self.setBackgroundImage( self.backgroundImage )
        self.setFont(self.default_fontName, self.default_fontSize)
        self.insertName  = self.font.render("name: ", True, ((255,255,255)))
        self.startButton = self.font.render("press space to start", True, ((255,255,255)))
        self.escButton   = self.font.render("Esc - to quit", True, ((255,255,255)))
        #   draw start menu on the screen -->(button, position)
        self.screen.blit(self.startButton, self.default_positionStart)
        self.screen.blit(self.insertName, self.default_positionName)
        self.screen.blit(self.escButton, self.default_positionEsc)
        self.getInputBox()

        pygame.display.update()

    #   G A M E   O V E R   M E N U   ----------------------------------------------------------------------------------------
    def gameOverMenu(self):
        '''
            Draw game over menu - game over text, quit button, restart button
 
        '''
        self.setBackgroundImage( self.backgroundImage )
        self.setFont(self.default_fontName, self.default_fontSize)
        self.gameOverText  = self.font.render("Game Over", True, (255,255,255))
        self.restartButton = self.font.render("r - restart", True, (255,255,255))
        self.scoreList     = self.font.render("h - high scores", True, (255,255,255)) 
        self.newPlayer     = self.font.render("n - new player", True, (255,255,255))
        #   draw game over menu on the screen --> (button, position)
        self.screen.blit(self.gameOverText, self.default_positionGameOver)
        self.screen.blit(self.restartButton, self.default_positionRestart)
        self.screen.blit(self.scoreList, self.default_positionScoreList)
        self.screen.blit(self.scoreText, self.default_positionFinalScore)
        self.screen.blit(self.escButton, self.default_positionEsc)
        self.screen.blit(self.newPlayer, (300, 450))
        pygame.display.update()

    #   H I G H   S C O R E   M E N U   --------------------------------------------------------------------------------------    
    def highScoresMenu(self):
        '''
            Draw score list - list of the scores for each player

        '''
        self.setBackgroundImage( self.backgroundImage )
        self.setFont(self.default_fontName, self.default_fontSize)
        self.highScoresText  = self.font.render("H I G H   S C O R E S", True, (255,255,255))
        self.backButton      = self.font.render("b - back", True, (255,255,255))
        self.startMenuButton = self.font.render("s - start new game", True, (255,255,255))
        #   draw high scores menu on the screen --> (button, position)
        self.screen.blit(self.highScoresText, self.default_positionHighScores)
        self.screen.blit(self.backButton, (50, 550))
        self.screen.blit(self.escButton, self.default_positionEsc)
        self.screen.blit(self.startMenuButton, self.default_positionBack)

        self.printScores()
        
        pygame.display.update()


    #   S T A R T   S T A T E   ----------------------------------------------------------------------------------------------
    def startState(self, event):
        '''
            Get player name then start or quit the game based on the event type
                Input:
                    event      : identification number of the event that happened on the screen
                        tuple
         
        '''
        self.startMenu() 
        if event.type == pygame.locals.KEYDOWN and event.key != pygame.locals.K_SPACE and event.key != pygame.locals.K_ESCAPE:
            if event.key == pygame.locals.K_BACKSPACE:
                self.userText = self.userText[:-1]
                self.name = self.userText
            else : 
                self.userText += event.unicode
                self.name += str(chr(event.key))                        
        elif event.type == pygame.locals.KEYDOWN and event.key == pygame.locals.K_SPACE:
                self.players[self.name] = 0
                self.resetGame()
                self.game_state = "game"
        elif event.type == pygame.locals.KEYDOWN and event.key == pygame.locals.K_ESCAPE:
                self.done = True


    #   G A M E   O V E R   S T A T E   --------------------------------------------------------------------------------------
    def gameOverState(self, event):
        '''
            See high scores or restart or quit the game, based on the event type
                Input:
                    event      : identification number of the event that happened on the screen
                        tuple
         
        '''
        self.gameOverMenu()
        if event.type == pygame.locals.KEYDOWN:
            if   event.key  == pygame.locals.K_ESCAPE   :   self.done       = True
            elif event.key  == pygame.locals.K_n        :  
                self.resetPlayer()
                self.game_state = "start_menu"
            elif event.key  == pygame.locals.K_h        :   self.game_state = "high_scores"
            elif event.key  == pygame.locals.K_r        :
                self.resetGame()
                self.game_state = "game"

    #   H I G H   S C O R E   S T A T E   ------------------------------------------------------------------------------------
    def highScoreState(self, event):
        '''
            List of all the players high scores, quit the game or get back to start menu based on the event type
                Input:
                    event      : identification number of the event that happened on the screen
                        tuple
         
        '''
        self.highScoresMenu()
        if event.type == pygame.locals.KEYDOWN:
            if   event.key == pygame.locals.K_s        :  
                self.resetPlayer()
                self.game_state = "start_menu" 
            elif event.key == pygame.locals.K_b        :  self.game_state = "game_over"
            elif event.key == pygame.locals.K_ESCAPE   :  self.done       = True

