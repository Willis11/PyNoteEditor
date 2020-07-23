#!/usr/bin/python
import os;

def menu():
    print("Welcome to the PyNoteEditor");
    print("To write a new file press w");
    print("To read a file press r");
    print("To get a list of text files press l")
    print("To exit the PyNoteEditor press e");
    menuChoice = raw_input();
    if(menuChoice == "w"):
        print("Please enter a file title");
        text = raw_input("Title: ");
        write(text);
    elif(menuChoice == "r"):
        print("Please enter a file title to read");
        rtext = raw_input("Title: ");
        read(rtext);
    elif(menuChoice == "e"):
        exit();
    elif(menuChoice == "l"):
        listFiles();
    else:
        menu();

def write(title):
    beginWriting = True;
    print("To stop writing type '/e'");
    f = open(title +".txt", "w");
    while(beginWriting == True):
        text = raw_input("Line: ");
        if(text == "/e"):
            beginWriting = False;
            f.close();
            menu();
        else:
            f.write(text + "\n");

def read(title):
    exitReading = False;
    f = open(title +".txt", "r");
    fileText = f.read();
    print(fileText);
    while(exitReading == False):
        text = raw_input("Type '/e' to go back to menu: ");
        if(text == "/e"):
            menu();

def listFiles():
    exitReading = False;
    fileList = os.listdir('../PyNoteEditor');
    for i in fileList:
        print(i);
    while(exitReading == False):
        text = raw_input("Type '/e' to go back to menu: ");
        if(text == "/e"):
            menu();

menu();
