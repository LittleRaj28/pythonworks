class Books:
    name=str
    author=str
    price=int
    pages=int
    def __init__(self,**kwargs):
        self.name=kwargs.get("name")
        self.author=kwargs.get("author")
        self.price=kwargs.get("price")
        self.pages=kwargs.get("pages")

    def __str__(self):
        return self.name

obj=Books(name="randaamoozham",author="mt vasudevan nair",price=590,pages=500)
print(obj)