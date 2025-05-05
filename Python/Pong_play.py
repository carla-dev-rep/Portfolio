from Pong_class import Pong


game = Pong(    backgroundImage     = "Backgrounds/space.png",
                ballImage           = "Images/ball.png",
                barImage            = "Images/bar.png",
                brickImageRed       = "Images/brickRed.png",
                brickImageYellow    = "Images/brickYellow.png",
                brickImageGreen     = "Images/brickGreen.png",
                portalImage         = "Images/portal.png",
                soundBounce         = "Effects/boing.wav",
                soundHit            = "Effects/hit.wav" 
                )

game.play()