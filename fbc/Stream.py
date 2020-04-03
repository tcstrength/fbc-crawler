import os

class Stream():
    f = open("comments.txt", "a+", encoding="utf-8")

def write(txt, endline="\n"):
    final = txt + endline
    # print(final.encode("utf-8"))
    Stream.f.write(final)

