# -*- coding: utf-8 -*-
# Use Class with tinker
# USE Python 3
# Charalambos Themistocleous
# 2016-2018

from grLexIPA import grLexIPA
from cgLexIPA import cgLexIPA
from arpabetIPA import arpabetIPA
from tagger import tagger
# from characters import character_freq
from normalize import normalize
from nltk import word_tokenize
from tkinter import *
from tkinter.filedialog import asksaveasfile, askopenfiles
import pyperclip
import os

root = Tk()

filename = None


def donothing():
    '''Do Nothing'''
    pass


def selectalltext():
    '''Selects all text in the document'''
    text.tag_add(SEL, "1.0", END)
    text.mark_set(INSERT, "1.0")
    text.see(INSERT)
    return 'break'


def paste():
    '''Paste Text'''
    text2paste = text.get(SEL_FIRST, SEL_LAST)
    # works for Text and Entry, at least; fails quietly
    os.system("echo '%s' | pbpaste" % text2paste)


def copy():
    '''Copy Text'''
    text2copy = text.get(SEL_FIRST, SEL_LAST)
    os.system("echo '%s' | pbcopy" % text2copy)


def cut():
    '''Cut Text'''
    text2copy = text.get(SEL_FIRST, SEL_LAST)
    os.system("echo '%s' | pbcopy" % text2copy)
    text.delete(SEL_FIRST, SEL_LAST)


def deletealltext():
    '''Delete all text'''
    text.delete(0.0, END)


def newFile():
    '''Create New File'''
    global filename
    filename = "Untitled"
    text.delete(0.0, END)  # delete text from the beginning to the End.


def saveFile():
    '''Save File'''
    f = asksaveasfile(mode='w', defaultextension=".txt")
    if f is None:
        return
    get_text = str(text.get(0.0, END))
    try:
        f.write(get_text)
        f.close()
    except:
        showerror(title="Error", message="Unable to save file...")


def saveAs():
    '''Save File'''
    f = asksaveasfile(mode='w', defaultextension=".txt")
    if f is None:
        return
    get_text = str(text.get(0.0, END))
    try:
        f.write(get_text)
        f.close()
    except:
        showerror(title="Error", message="Unable to save file...")


def openFile():
    '''Save File'''
    f = askopenfile(mode='r')
    t = f.read()
    text.delete(0.0, END)
    text.insert(0.0, t)


def grLexIPAtranaform():
    '''It converts a text in Greek orthography to IPA'''
    t = text.get(0.0, END)
    t = normalize(t)
    t = grLexIPA(t)
    text.delete(0.0, END)
    text.insert(0.0, t)


def cgLexIPAtranaform():
    '''It converts a text in Greek orthography to IPA using rules for Cypriot Greek'''
    t = text.get(0.0, END)
    t = normalize(t)
    t = cgLexIPA(t)
    text.delete(0.0, END)
    text.insert(0.0, t)


def arpabetIPAtranaform():
    '''It converts a text in ARPABET to IPA'''
    t = text.get(0.0, END)
    t = normalize(t)
    t = arpabetIPA(t)
    text.delete(0.0, END)
    text.insert(0.0, t)


def mytag():
    t = text.get(0.0, END)
    text.delete(0.0, END)
    text.insert(0.0, tagger(t))


def words():
    '''Count Words'''
    t = text.get(0.0, END)
    t = len(word_tokenize(t))
    messagebox.showinfo("Counts", "words: " + str(t))


def quitapplication():
    '''Quit Application'''
    root.quit()
    root.destroy()


# Next, create an application object.

root.title("Natural Language Processing")
root.minsize(width=500, height=500)
root.iconphoto(root, PhotoImage(file="icon.gif"))
text = Text(root, width=16, height=5, borderwidth=0,
            highlightcolor="white", font=("Helvetica", 16), wrap=WORD)
text.pack(side=LEFT, fill=BOTH, expand=YES)

# Add Scrollbar
yscrollbar = Scrollbar(root, orient=VERTICAL, command=text.yview)
yscrollbar.pack(side=RIGHT, fill=Y)
text["yscrollcommand"] = yscrollbar.set

# Let us create a nice menu bar
menubar = Menu(root)
applemenu = Menu(menubar, tearoff=0, name='apple')
applemenu.add_command(label="Preferences...", command=donothing)

filemenu = Menu(menubar, tearoff=0)
filemenu.add_command(label="New", command=newFile)
filemenu.add_command(label="Open", command=openFile)
filemenu.add_command(label="Save", command=saveFile)
filemenu.add_command(label="Save As...", command=saveAs)
filemenu.add_separator()
filemenu.add_command(label="Quit", command=quitapplication,
                     accelerator="Command+Q")

editmenu = Menu(menubar, tearoff=0)
editmenu.add_command(label="Undo", command=donothing)
editmenu.add_separator()
editmenu.add_command(label="Cut", command=cut, accelerator="Command+X")
editmenu.add_command(label="Copy", command=copy, accelerator="Command+C")
editmenu.add_command(label="Paste", command=paste, accelerator="Command+V")
editmenu.add_command(label="Delete", command=deletealltext,
                     accelerator="Command+D")
editmenu.add_command(label="Select All",
                     command=selectalltext, accelerator="Command+a")

formatmenu = Menu(menubar, tearoff=0)
formatmenu.add_command(label="Font", command=donothing)
formatmenu.add_separator()
formatmenu.add_command(label="Text", command=donothing)
formatmenu.add_command(label="Make Plain Text", command=donothing)

toolsmenu = Menu(menubar, tearoff=0)
toolsmenu.add_command(
    label="Convert to SMG IPA (Lexical Rules)", command=grLexIPAtranaform)
toolsmenu.add_command(
    label="Convert to SMG IPA (Postlexical Rules)", command=donothing)
toolsmenu.add_separator()
toolsmenu.add_command(
    label="Convert to CG IPA (Lexical Rules)", command=cgLexIPAtranaform)
toolsmenu.add_command(
    label="Convert to CG IPA (Postlexical Rules)", command=donothing)
toolsmenu.add_separator()
toolsmenu.add_command(
    label="Convert ARPAbet to IPA", command=arpabetIPAtranaform)
toolsmenu.add_separator()
toolsmenu.add_command(label="Tagger", command=mytag)
toolsmenu.add_separator()
# toolsmenu.add_command(label="Character Analysis", command=characters)
toolsmenu.add_command(label="Count Words", command=words)
toolsmenu.add_separator()
toolsmenu.add_command(label="Delete", command=donothing)
toolsmenu.add_command(label="Select All", command=selectalltext)

helpmenu = Menu(menubar, tearoff=0)
helpmenu.add_command(label="Help Index", command=donothing)
helpmenu.add_command(label="About...", command=donothing)

menubar.add_cascade(label="Phonetics", menu=applemenu)
menubar.add_cascade(label="File", menu=filemenu)
menubar.add_cascade(label="Edit", menu=editmenu)
menubar.add_cascade(label="Format", menu=formatmenu)
menubar.add_cascade(label="Tools", menu=toolsmenu)
menubar.add_cascade(label="Help", menu=helpmenu)

root.config(menu=menubar)
root.mainloop()
