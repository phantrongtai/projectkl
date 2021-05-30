from tkinter import *
from PIL import ImageTk,Image
from time import sleep

img = [0, 0, 0]

game = Tk()
game.title("Khủng long")
canvas = Canvas(master=game, width=600, height=300, background="white")
canvas.pack()

img[0]=ImageTk.PhotoImage(Image.open("photos/kl0.png"))
img[1]=ImageTk.PhotoImage(Image.open("photos/cloud.png"))
img[2]=ImageTk.PhotoImage(Image.open("photos/tree.png"))

dragon = canvas.create_image(0, 250, anchor=NW, image=img[0])
cloud = canvas.create_image(550, 100, anchor=NW, image=img[1])
tree = canvas.create_image(550, 250, anchor=NW, image=img[2])

canvas.update()

def moveCloud():
    global cloud
    canvas.move(cloud, -5, 0)
    if canvas.coords(cloud)[0]<-20:
        canvas.delete(cloud)
        cloud = canvas.create_image(550, 100, anchor=NW, image=img[1])
    canvas.update()

score = 0
text_score = canvas.create_text(550, 50, text="SCORE: " + str(score), fill="red", font=('Times', 15))

def moveTree():
    global tree, score, text_score
    canvas.move(tree, -3, 0)
    if canvas.coords(tree)[0]<-20:
        score = score + 1
        canvas.itemconfig(text_score, text="SCORE: " + str(score))
        canvas.delete(tree)
        tree = canvas.create_image(550, 250, anchor=NW, image=img[2])
    canvas.update()

check_jump = False

def jump():
    global check_jump
    if check_jump == False:
        check_jump = True
        for i in range(0, 30):
            canvas.move(dragon, 0, -5)
            moveCloud()
            moveTree()
            canvas.update()
            sleep(0.01)
        for i in range(0, 30):
            canvas.move(dragon, 0, 5)
            moveCloud()
            moveTree()
            canvas.update()
            sleep(0.01)
        check_jump = False

def keyPress(event):
    if event.keysym=="space":
        jump()

canvas.bind_all("<KeyPress>", keyPress)

gameOver = False

def check_gameOver():
    global gameOver
    coords_tree = canvas.coords(tree)
    coords_dragon = canvas.coords(dragon)
    if coords_dragon[1]>200 and coords_tree[0]<50:
        gameOver = True
        text_gameover = canvas.create_text(300, 150, text="GAME OVER", fill="blue", font=('Times', 20))
    game.after(100, check_gameOver)

check_gameOver() 

while not gameOver:
    moveCloud()
    moveTree()
    sleep(0.01)

game.mainloop()
