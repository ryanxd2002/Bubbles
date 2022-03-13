from cmu_112_graphics import*
import random
################################################################################
def appStarted(app):
    app.score = 0
    app.timerDelay = 100
    app.bubbles = []
    app.radius = random.randint(25, 35)
    app.newBubbleTimer = 0
    app.poppedBubbles = []
    app.gameOver = False
    app.change = 5

def timerFired(app):
    if app.gameOver == True:
        return
    for x, y in app.bubbles:
        if y + 25 <= 0:
            app.gameOver = True
    app.radius = random.randint(25, 35)
    app.newBubbleTimer += 1
    if app.newBubbleTimer % 5 == 0:
        x = random.randint(25, app.width - 25)
        app.bubbles.append((x, app.height - 25))
    if app.newBubbleTimer % 10 == 0: 
        app.change += 1
    for (x, y) in app.bubbles:
        app.bubbles.append((x, y - app.change))
        app.bubbles.remove((x, y)) 


def mousePressed(app, event):
    for (x, y) in app.bubbles:
        if x - 25 < event.x < x + 25 and y - 25 < event.y < y + 25:
            app.bubbles.remove((x, y))
            app.poppedBubbles.append((x, y))
            app.score = app.score + 1

def keyPressed(app, event):
    if event.key == "r":
        appStarted(app)
def redrawAll(app, canvas):
        if app.gameOver == True:
            canvas.create_text(app.width // 2, app.height //2, 
                                text = f"GAME OVER \n SCORE: {app.score}",
                                font = "Arial 26 bold", fill = "black")
        else:
            canvas.create_text(app.width // 2, 20, 
                                text = f'Score: {app.score}', 
                                font = "Arial 26 bold", fill = 'black')
            for x, y in app.bubbles:
                canvas.create_oval(x + app.radius, y + app.radius, 
                                    x - app.radius, y - app.radius, 
                                    outline = "black", width = 3)
            for x, y in app.poppedBubbles:
                canvas.create_oval(x + app.radius, y + app.radius, 
                                    x - app.radius, y - app.radius, 
                                    outline = "black", width = 1)
runApp(width = 600, height = 600)