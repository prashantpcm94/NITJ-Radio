from Tkinter import *
import FileDialog as tk
import tkMessageBox as tk2
import pygame
import tkFileDialog
playlist1 = []
playlist2 = []

class Application(Frame):
    
    def __init__(self,master):
        tk.Frame.__init__(self, master)
        
        #self.create_widgets()
        self.playlistbox1 = Listbox(self, width = 40, height = 10, selectmode = SINGLE)
	self.playlistbox2 = Listbox(self, width = 40, height = 10, selectmode = SINGLE) #TODO: ---> BROWSE, MULTIPLE, EXTENDED (p.379)
        for song in playlist1:
            self.playlistbox1.insert(END, song)
        for song in playlist2:
            self.playlistbox2.insert(END, song)
            
        self.grid(rowspan=5, columnspan=5)
        self.playlistbox1.grid(row = 1,column=1)
	self.playlistbox2.grid(row = 1,column=2)
        self.playButton1 = Button(self, text = 'Play', command = self.play1)
	self.playButton2 = Button(self, text = 'Play', command = self.play2)
        self.addButton1 = Button(self, text = 'Add To Playlist 1', command = self.add1)
	self.addButton2 = Button(self, text = 'Add To Playlist 2', command = self.add2)
        self.playButton1.grid(row=4, column = 0)
        self.playButton2.grid(row=4, column = 2)
        self.addButton1.grid(row=4, column = 1)
	self.addButton2.grid(row=4, column = 3)
        self.pack()
        
        #pygame initialize
        pygame.init()

    def play1(self):
        if(len(playlist1) == 0):
            tk2.showinfo('Notice', 'No songs in your playlist!\nClick Add to add songs.')
        else:    
            pygame.mixer.music.stop()
            selectedSongs = self.playlistbox1.curselection()
            global playlistbox
            playIt = playlist1[int(selectedSongs[0])]
            pygame.mixer.music.load(playIt)
            pygame.mixer.music.play(0, 0.0)
    
    def play2(self):
        if(len(playlist2) == 0):
            tk2.showinfo('Notice', 'No songs in your playlist!\nClick Add to add songs.')
        else:    
            pygame.mixer.music.stop()
            selectedSongs = self.playlistbox2.curselection()
            global playlistbox
            playIt = playlist2[int(selectedSongs[0])]
            pygame.mixer.music.load(playIt)
            pygame.mixer.music.play(0, 0.0)
            

    def loop(self):
        pygame.mixer.music.stop()
        pygame.mixer.music.play(-1,0.0)

    def add1(self):
        file = tkFileDialog.askopenfilenames(parent=root,title='Choose a file')  
        songsTuple = root.tk.splitlist(file)   #turn user's opened filenames into tuple
        songsList = list(songsTuple)        #convert to list
        #Add the full filename of songto playlist list, and a shortened version to the listBox
        for song in songsList:              
            playlist1.append(song);          
            tempArray = song.split('/')     
            songShort = tempArray[len(tempArray)-1]
            self.playlistbox1.insert(END, songShort)

    def add2(self):
        file = tkFileDialog.askopenfilenames(parent=root,title='Choose a file')  
        songsTuple = root.tk.splitlist(file)   #turn user's opened filenames into tuple
        songsList = list(songsTuple)        #convert to list
        #Add the full filename of songto playlist list, and a shortened version to the listBox
        for song in songsList:              
            playlist2.append(song);          
            tempArray = song.split('/')     
            songShort = tempArray[len(tempArray)-1]
            self.playlistbox2.insert(END, songShort)

        
root = Tk()
root.title('NIT Jalandhar Radio Console')
root.geometry('1000x200')
app = Application(root)
app.mainloop()
