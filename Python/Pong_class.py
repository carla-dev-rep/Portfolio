import pygame, pygame.locals, random
from Game_class import Game

class Pong(Game):
    def __init__(self, 
                backgroundImage,
                ballImage,
                barImage,
                brickImageRed,
                brickImageYellow,
                brickImageGreen,
                portalImage,
                soundBounce,
                soundHit,
                default_startingBall       = None,
                default_startingBar        = None,
                default_velocity           = None,
                default_ballVelocity       = None,
                default_barVelocity        = None,
                default_brickVelocity      = None,
                default_maxScore           = None,
                default_portalNumber       = None,
                default_lineSpacing        = None,
                default_timeStart          = None,
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
                default_positionScore      = None,
                default_positionPlayers    = None,
                default_positionBack       = None,
                default_score              = None,
                default_fontName           = None,
                default_fontSize           = None
                ):
                
        super().__init__(backgroundImage,
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
                    )
        
        if default_startingBall          is None : self.default_startingBall          = (self.screenSize[0]/2, self.screenSize[1]/4)
        if default_startingBar           is None : self.default_startingBar           = (self.screenSize[0]/2, self.screenSize[1]-40)
        if default_velocity              is None : self.default_velocity              = [0,0]
        if default_ballVelocity          is None : self.default_ballVelocity          = [8,8]
        if default_barVelocity           is None : self.default_barVelocity           = [10,0]  
        if default_brickVelocity         is None : self.default_brickVelocity         = 2   
        if default_maxScore              is None : self.default_maxScore              = 10
        if default_lineSpacing           is None : self.default_lineSpacing           = 50
        if default_portalNumber          is None : self.default_portalNumber          = 2
        if default_timeStart             is None : self.default_timeStart             = 500
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
        if default_positionScore         is None : self.default_positionScore         = (350,15 )
        if default_positionPlayers       is None : self.default_positionPlayers       = (300,150)
        if default_positionBack          is None : self.default_positionBack          = (300,550)    
        if default_score                 is None : self.default_score                 = 0
        if default_fontName              is None : self.default_fontName              = "arial"
        if default_fontSize              is None : self.default_fontSize              = 30



        self.ballImage          = ballImage
        self.barImage           = barImage
        self.brickImageRed      = brickImageRed
        self.brickImageYellow   = brickImageYellow
        self.brickImageGreen    = brickImageGreen
        self.portalImage        = portalImage
        self.soundBounce        = soundBounce
        self.soundHit           = soundHit

    #   S E T   S C O R E   --------------------------------------------------------------------------------------------------
    def setScore(self, score):
        '''
            Initialization of the score
                Input:
                    score       : score number
                        tuple
        '''
        self.setFont(self.default_fontName, self.default_fontSize)
        self.scoreText = self.font.render("Score: " + str(score), True, (255,255,255))
        self.screen.blit(self.scoreText, self.default_positionScore)

    
    #   S E T   B A L L   I M A G E ------------------------------------------------------------------------------------------
    def setBallImage(self, image):
        '''
            Set ball image
                Input:
                    image       : path of the ball image 
                        string
        '''
        loadedImage           = pygame.image.load( image ).convert_alpha()
    #    self.setTimer(self.default_timeStart)
    #    self.ballVelocity = self.default_ballVelocity
        self.allBall          = pygame.sprite.Group()

        self.ball             = pygame.sprite.Sprite(self.allBall)
        self.ball.image       = pygame.transform.scale2x(loadedImage)
        self.ball.rect        = self.ball.image.get_rect()
        self.ball.rect.center = self.default_startingBall

    #   S E T   B A R   I M A G E   ------------------------------------------------------------------------------------------     
    def setBarImage(self, image):
        '''
            Set bar image
                Input:
                    image       : path of the bar image 
                        string
        '''
        self.allBar          = pygame.sprite.Group()

        self.bar             = pygame.sprite.Sprite(self.allBar)
        self.bar.image       = pygame.image.load( image ).convert_alpha()
        self.bar.rect        = self.bar.image.get_rect()
        self.bar.rect.center = self.default_startingBar

    #   S E T   B R I C K   I M A G E   --------------------------------------------------------------------------------------
    def setBrickImage(self, *args):
        '''
            Set brick image
                Input:
                    image       : path of the brick image 
                        string
        '''    
        for image in args: 
            self.brickImages.append(pygame.image.load( image ).convert_alpha())

        self.allBricks  =   pygame.sprite.Group()
        self.setTimer(random.randrange(200, 2501))
    
    #   S E T   P O R T A L   I M A G E   ------------------------------------------------------------------------------------
    def setPortalImage(self, image, position):
        '''
            Set portal image
                Input:
                    image       : path of the portal image 
                        string
        '''
        self.surfacePortal = pygame.image.load( image ).convert_alpha()
        self.rectPortal    = self.surfacePortal.get_rect()
        #   portal image position
       # x1 = random.randrange(0, ((self.screenSize[0]- self.rectPortal[0]) - 100) +1) 
       # y1 = random.randrange(0, ((self.screenSize[1]- self.rectPortal[1]) - 100) +1)
       # self.rectPortal.topleft = (x1, y1)
        self.rectPortal.topleft = (position)

        #self.screen.blit(self.surfacePortal, self.rectPortal)

   #   S E T   S O U N D   --------------------------------------------------------------------------------------------------
    def setSound(self, sound):
        '''
            set sound effects for ball hitting the corner and ball hitting the bar
                Input:
                    sound       : path of the sound effect
                        string
        '''
        self.sound = pygame.mixer.Sound(sound)
        self.sound.play()

 
    #   R E S E T   G A M E   ------------------------------------------------------------------------------------------------
    def resetGame(self):
        '''
            Reset: position and velocity of both bar and ball, score number, bar and portal image, player input

        '''
        #   reset bar image
        self.setBarImage(self.barImage)
        #   reset position
        self.setBallImage(self.ballImage)
        #   reset velocity
        self.ballVelocity     = self.default_velocity
        self.barVelocity      = self.default_velocity

        #   reset score
        self.score            = self.default_score

        #   reset portal image
        self.setPortalImage(self.portalImage, (0,0))

        self.setRandomVariables()

        self.setBrickImage(self.brickImageRed, self.brickImageYellow, self.brickImageGreen)

        #   reset input event for bar movement
        self.pressed = None

        self.setTimerBall(1000)


    #   R E S E T   P L A Y E R   --------------------------------------------------------------------------------------------
    def resetPlayer(self):
        '''
            Reset player name

        '''  
        self.baseFont  = pygame.font.Font(None, 30) 
        self.userText  = ''
        self.inputRect = pygame.Rect(self.default_inputBoxSize)
        self.name      = ''

    #   P R I N T   S C O R E S   --------------------------------------------------------------------------------------------
    def printScores(self):
        '''
            Prints the top 5 scores of all the players
        '''        
        lineSpacing = 0
        
        #   sort the scores based on the values and take the top 5.
        top_scores = sorted(self.players.items(), key=lambda item: item[1], reverse=True)[:5]
        
        for name, score in top_scores:
            self.setFont(self.default_fontName, self.default_fontSize)
            self.highScores = self.font.render(f"{name}      -------     {score}", True, (255, 255, 255))
            self.screen.blit(self.highScores, (self.default_positionPlayers[0], self.default_positionPlayers[1] + lineSpacing))
            lineSpacing += self.default_lineSpacing

    
    #   G E T   N E W   B A R   R E C T   ------------------------------------------------------------------------------------
    def getNewBarRect(self):
        '''
            Get the right rect for the smaller bars
                Input:

        '''
        self.bar.rect         = self.bar.image.get_rect()
        self.bar.rect.topleft = (self.xRect, self.yRect) 

    #   G A M E   ------------------------------------------------------------------------------------------------------------
    def game(self, pressed):
        '''
            Check for collision between: ball and bar, ball and portal, ball and screen sides, bar and screen sides
            Input:
                pressed     :   event type of the bar movement

        '''
        #   check if bar reaches right or left sides of screen width
        if self.bar.rect.left < 0 or self.bar.rect.right > self.screen.get_width():
            #   invert x component
            self.barVelocity[0] = 0
        
        #   check if ball reaches right or left sides of screen width
        if self.ball.rect.left <= 0 or self.ball.rect.right >= self.screen.get_width():
            #   invert x component
            self.ballVelocity[0] *= -1
            self.setSound(self.soundBounce)
        #   check if ball reaches the top of screen height 
        if self.ball.rect.top <= 0: 
            #   invert y component
            self.ballVelocity[1] *= -1
            self.setSound(self.soundBounce)
        #   check if ball reaches the bottom of screen height
        if self.ball.rect.bottom > self.screen.get_height():
            self.game_state         = "game_over"
            self.players[self.name] = self.score
            sorted(self.players, key=self.players.get, reverse=True)
            #self.resetPlayer()
            self.gameOverMenu()
            return   

        #   check if ball collides with bar: if true, ball bounces off bar
        #if self.bar.rect.colliderect(self.ball.rect) and self.ballVelocity[1] > 0:
        if (self.bar.rect.collidepoint(self.ball.rect.bottomleft) or self.ball.rect.collidepoint(self.ball.rect.bottomright)) and  self.ballVelocity[1] > 0:
            self.ballVelocity[1] *= -1
            self.setSound(self.soundHit)           
        
        #   score number check in order to change bar image to a smaller one
        if self.score >= self.default_maxScore and self.score < self.default_maxScore*2:
            self.bar.image=pygame.transform.smoothscale(self.bar.image, (32,16))
            self.getNewBarRect()
        elif self.score >= self.default_maxScore*2:
            self.bar.image=pygame.transform.smoothscale(self.bar.image, (16,16))
            self.getNewBarRect()
             
        #   update position of both ball and bar
        self.ball.rect.x += self.ballVelocity[0]
        self.ball.rect.y += self.ballVelocity[1]

        #   bar movement left or right
        if pressed ==pygame.locals.K_LEFT and self.bar.rect.left > 0:
            self.bar.rect.x -= self.default_barVelocity[0]
        elif pressed == pygame.locals.K_RIGHT and self.bar.rect.right < self.screen.get_width():
            self.bar.rect.x += self.default_barVelocity[0] 

        self.xRect = self.bar.rect[0]
        self.yRect = self.bar.rect[1]

        #   screen update
        self.screen.blit((self.surfaceBackgroung), (0,0))
        self.allBall.draw(self.screen)
        self.allBar.draw(self.screen)

        #   draw default_portalNumber of portals
        self.portalNumber = 0
        portalDistance    = 0
        for self.portalNumber in range (self.default_portalNumber):
            self.setPortalImage(self.portalImage, (self.x + portalDistance, self.y))
            self.screen.blit(self.surfacePortal, self.rectPortal)
            #self.setRandomVariables()
            portalDistance += 300
            #   check if ball collides with portal: if true, draw ball in random position
            if pygame.Rect.colliderect(self.ball.rect, self.rectPortal):
                x2 = random.randrange(0, self.screenSize[0]-50)
                y2 = random.randrange(0, (self.screenSize[1]-200))
                self.ball.rect.topleft = (x2, y2)

        if self.rectPortal.left < 0  or self.rectPortal.right > self.screen.get_width():
            self.setRandomVariables()
            self.setPortalImage(self.portalImage, (self.x, self.y))

        for self.brick in self.allBricks:
            self.brick.rect.x += self.default_brickVelocity
            if self.brick.rect.left > self.screen.get_width():
                self.brick.kill()
            if self.ball.rect.colliderect(self.brick.rect):
                self.ballVelocity[1] *= -1
                self.setSound(self.soundHit)
                self.brick.kill()
                self.score += 1

        self.allBricks.draw(self.screen)
        self.setScore(self.score)

   #   G A M E   S T A T E   ------------------------------------------------------------------------------------------------
    def gameState(self, event):
        '''
            Get movement of bar (left or right)
                Input:
                    event       :   type of the event that happened on the screen
                        tuple
        '''
        if event.type == pygame.locals.KEYDOWN and event.key in (pygame.locals.K_LEFT, pygame.locals.K_RIGHT):
            self.pressed = event.key
        if event.type == pygame.locals.KEYUP and event.key == self.pressed:
            self.pressed = None

    #   I N I T I A L I Z A T I O N   ----------------------------------------------------------------------------------------
    def initialization(self):
        '''
            Initialization of all images

        '''
        self.setBackgroundImage(self.backgroundImage)
        self.setBallImage(self.ballImage)
        self.setBarImage(self.barImage)
        self.setPortalImage(self.portalImage, (0,0))
        self.setRandomVariables()
        self.setTimer(self.default_timeStart)
        self.setTimerBall(1000)
        self.setBrickImage(self.brickImageRed, self.brickImageYellow, self.brickImageGreen)

    #   D R A W   B R I C K S   ----------------------------------------------------------------------------------------------
    def drawBricks(self):
        '''
            Draw all the brick in random position in the top half of the screen
        '''
        self.setTimer(self.default_timeStart)
        self.brick = pygame.sprite.Sprite(self.allBricks)
        self.brick.image = self.brickImages[random.randrange(3)]
        self.brick.rect  = self.brick.image.get_rect()
        self.maxy = self.screen.get_height()/2 - self.brick.rect.height
        self.brick.rect.topright = (-1, random.randrange(10, self.maxy))


    #   S E T   T I M E R   --------------------------------------------------------------------------------------------------   
    def setTimerBall (self, milliseconds):
        '''
            Set the timer event
                Input:
                    milliseconds    : milliseconds to which the timer will get off
        '''
        self.timerBall = pygame.event.custom_type()
        pygame.time.set_timer(self.timerBall, milliseconds)

    #   P L A Y   ------------------------------------------------------------------------------------------------------------
    def play(self):
        '''
            Play pong game      :   move bar with left and right arrows to catch ball
                                    if ball goes through portal              --> ball appears in random position
                                    if ball reaches the bottom of the screen --> Game Over

        '''
        self.screen = pygame.display.set_mode(self.screenSize)
        pygame.display.set_caption("Pong")
        
        self.brickImages = []
        #   initialization
        self.initialization()

        #   reset
        self.resetGame()
        self.resetPlayer()

        self.done       = False
        self.game_state = "start_menu"

        #   it contains all the scores
        self.players = self.load_from_binaryFile('Database')

        while not self.done:
            #   events cycle
            for event in pygame.event.get():

                if event.type == pygame.locals.QUIT     :   self.done = True

                if event.type == self.timerBall         :   self.ballVelocity = self.default_ballVelocity

                if event.type == self.timer             :   self.drawBricks()

                #   start menu state        
                if self.game_state == "start_menu"      :   self.startState( event )
                                
                #   game over state
                elif self.game_state == "game_over"     :   self.gameOverState( event )
                
                #   high score state
                elif self.game_state == "high_scores"   :   self.highScoreState( event )
                            
                #   game state        
                elif self.game_state == "game"          :   self.gameState( event )

            
            if self.game_state == "game"                :   self.game(self.pressed)

            if self.done : self.save_to_binaryFile(self.players, 'database')

            pygame.display.flip()
            #   set frames per seconds (fps)
            self.clock.tick(30)   

        #   quit game
        pygame.quit()