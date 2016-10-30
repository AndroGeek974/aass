import os
import math

src_link = "https://android.googlesource.com/platform/manifest/" # Setup googlesource link
ver = "android-7.1.0_r4" # Setup android ver you want

print("------------------------------------\n www.damien-boyer.com | www.github.com/AndroGeek974 \n------------------------------------")

def check():
    os.system("wget " + src_link) # dl the index of googlesource
    logs = open("index.html","r") # open it
    for ligne in logs: # loop on it to found the ver we want
        if ver in ligne:
            print("Android" + ver + "R4 is out !!!")
            os.system("rm index.html")
            dl() # if we found it, dl the sources
        else:
            print("Android" + ver + "not available...") # while not found, loop loop looooop
            os.system("rm index.html") #clean it everytime
            print("Updating logs...")
            check() # loop on check()
    logs.close() # close it

def never_giveup():
    os.system("cd " + ver + " && repo sync --force-sync") # Last try, last chance. Try to re-sync

def dl():
    print("ISD -- Initialize Source Download")
    os.system("mkdir " + ver) # Create the local repo
    os.system("cd " + ver + " && repo init -u " + src_link + " -b " + ver + " && repo sync --force-sync") # Initialize it & Download
    os.system("ls > hak.txt") # store source directory arborescence in hak.txt to see if there's not only that .repo
    hak = open("hak.txt","r") # open hak.txt
    whatever = "build" # searching for build/ in the folder
    for ligne in hak:
        if whatever in ligne:
            print("Repo Successfully Downloaded.") # If you found it, you have a lot of chances. You basically have your fully synced sources
        else:
            print("Repo NOT Successfully Downloaded.") # sorry but my coding skills aren't perfect
            never_giveup() # please

# Execute
check()
