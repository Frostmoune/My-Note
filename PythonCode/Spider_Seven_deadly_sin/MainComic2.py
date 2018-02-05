from Comic2 import *
import os

if not os.path.exists("Seven_deadly_sin"):
    os.mkdir("Seven_deadly_sin")

savepath = "Seven_deadly_sin"
nowcomic = Comic(savepath)
# html = nowcomic.getHtml("http://comic.kukudm.com/comiclist/1733/31848/1.htm")
# print (html)
# nowcomic.getTitle(html)
nowcomic.loadAllComic()
