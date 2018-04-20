class Song:
    def __init__(self,title,author,length):
        self.title = title
        self.author = author
        self.length = length

    def getlength(self):
        return self.length

    def getTitle(self):
        return self.title

    def getAuthor(self):
        return self.author
