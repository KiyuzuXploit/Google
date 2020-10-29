#!/bin/user/python
# module
try:
    import os,sys,time,requests,bs4
    from bs4 import BeautifulSoup
    from time import sleep
except:
    os.system("pip install requests bs4")
# ulang
def ulang():
  print("\033[1;90m [\033[92m?\033[1;90m] \033[1;97mGunakan tools lagi?")
  print("\033[1;90m [\033[1;96my\033[1;90m/\033[1;96mt\033[1;90m]")
  ulg = input("\033[1;90m •\033[1;96m>\033[1;96m ")
  if ulg == "y":
    time.sleep(1.21)
    jelajahi()
  elif ulg == "t":
    print("\033[92m[\033[1;93m#\033[92m]\033[1;93m Terimakasih telah menggunakan tools ini ")
    print("\033[92m[\033[1;93m#\033[92m] \033[1;93mDadah...")
  else:
    print("\033[1;91m[X] \033[1;97mHARAP ISI INPUT DENGAN BENAR")
    time.sleep(1.2)
    ulang()
# jelajahi
def jelajahi():
    # banner
    banner = """
\033[1;96m
       __________  ____  ________    ______
      / ____/ __ \/ __ \/ ____/ /   / ____/
     / / __/ / / / / / / / __/ /   / __/
    / /_/ / /_/ / /_/ / /_/ / /___/ /___
    \____/\____/\____/\____/_____/_____/v2
                 \033[1;0m\033[1;41mSEARCHING\033[1;0m
\033[1;96m+\033[1;90m============================================\033[1;96m+
 \033[1;90m[\033[1;96m•\033[1;90m] \033[92mAuthor    \033[1;91m: \033[1;93mKiyuzu
 \033[1;90m[\033[1;96m•\033[1;90m] \033[92mFacebook  \033[1;91m: \033[1;93mYg Baca Pacarku
 \033[1;90m[\033[1;96m•\033[1;90m] \033[92mClan      \033[1;91m: \033[1;93mSquad Cyber Mafia
\033[1;96m+\033[1;90m============================================\033[1;96m+"""
    os.system("clear")
    print(banner)
    # input
    cari = input(" \033[1;90m[\033[1;95m+\033[1;90m] \033[1;96mSearch \033[1;91m> \033[1;92m")
    url = f"https://www.google.com/search?&q={cari}"
    r = requests.get(url)
    mencari = BeautifulSoup(r.text,"html.parser")
    a = mencari.find("div",class_="BNeawe").text
    # output
    print("\033[1;91m [•] \033[1;93mHasil \033[1;96m>\033[1;93m",a)
    ulang()
jelajahi()
