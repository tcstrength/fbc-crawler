import os

class Stream():
    f = open("comments.txt", "a+")

def write(txt, endline="\n"):
    final = txt + endline
    print(final)
    Stream.f.write(final)

