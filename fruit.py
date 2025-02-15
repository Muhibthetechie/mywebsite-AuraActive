class fruit:
    taste = 'Sweet'
    def __init__(self,name,color):
        self.name = name
        self.color = color

apple =fruit('apple','red')
banana = fruit('banana','yellow')
mango = fruit('mango','yellow')

print(apple.taste)
print(apple.name,apple.color)
print(banana.name,banana.color)
print(mango.name,mango.color)