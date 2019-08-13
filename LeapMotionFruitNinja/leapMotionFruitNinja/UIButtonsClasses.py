#this file contains the UI button classes for everything to do with the 
#homescreens and buttons. It contains sticky buttons, normal UI buttons,
#along with all the fucntions nessesary for those


class UIButton(object):

    def __init__(self, x, y, width, height, text, color, path, img):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.color = color
        self.text = text
        self.path = path #this is the 'path' or 'mode' the button will lead to
        self.img = img
        self.onButton = False
        self.loaded = False
        self.loadTime = 60 #an integer. A factor of time it takes for the load

        self.cursorX = None
        self.cursorY = None
        self.cursorDegree = 0.0
        self.maxDegree = 360.0
        self.dDegree = self.maxDegree / self.loadTime


    #Draws the button itself and the loading icon around the cursor if the
    #cursor is on it
    def draw(self, canvas):

        canvas.create_rectangle(self.x, self.y, self.x + self.width, self.y + self.height, fill = self.color)


        canvas.create_image(self.x, self.y, image = self.img, anchor = "nw")


        canvas.create_text(self.x + self.width/2, self.y + self.height/2, text = self.text)

        if not (self.cursorX == None and self.cursorY == None):
            canvas.create_arc(self.cursorX - 20, self.cursorY - 20,
             self.cursorX + 20, self.cursorY + 20, start = 0,
              extent = self.cursorDegree, fill = "blue", outline = "")


    def inButton(self, x, y):
        
        
        if x<self.x+self.width and x>self.x and y<self.y+self.height and y>self.y:
            self.onButton = True
            self.cursorX = x
            self.cursorY = y
            self.cursorDegree += self.dDegree

            if self.cursorDegree >= self.maxDegree:
                self.loaded = True
                self.cursorDegree = 0

        else:
            self.loaded = False
            self.onButton = False
            self.cursorDegree = 0
            self.cursorX = None
            self.cursorY = None



class StickyUIButton(UIButton):

    def __init__(self, x, y, width, height, text, color, pressedColor, img, imgPressed):
        super(StickyUIButton, self).__init__(x, y, width, height, text, color, pressedColor, img)
        self.pressedColor = pressedColor #the color of the button when its in
        self.pushed = False              #a pushed state
        self.img = img
        self.imgPressed = imgPressed
        

    def draw(self, canvas):

        currentColor = self.color if not self.pushed else self.pressedColor
        currentImage = self.img if not self.pushed else self.imgPressed
        
        canvas.create_rectangle(self.x, self.y, self.x + self.width, self.y + self.height, fill = currentColor)

        canvas.create_image(self.x, self.y, image = currentImage, anchor = "nw")

        canvas.create_text(self.x + self.width/2, self.y + self.height/2, text = self.text)

        if not (self.cursorX == None and self.cursorY == None):
            canvas.create_arc(self.cursorX - 20, self.cursorY - 20,
             self.cursorX + 20, self.cursorY + 20, start = 0,
              extent = self.cursorDegree, fill = "Blue", outline = "")

    def inButton(self, x, y):
        
        if x<self.x+self.width and x>self.x and y<self.y+self.height and y>self.y:
            self.onButton = True
            self.cursorX = x
            self.cursorY = y
            self.cursorDegree += self.dDegree
            
            if self.cursorDegree >= self.maxDegree:
                self.pushed = not self.pushed
                self.cursorDegree = 0
                return
            return

        
        self.onButton = False
        self.cursorDegree = 0
        self.cursorX = None
        self.cursorY = None




