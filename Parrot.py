class Parot:
    species = "Bird"
    def __init__(self,name,age):
        self.name = name
        self.age = age

blu = Parot("Blu" , 10)
woo = Parot("woo" , 12)

print(blu.species)
print(woo.species)

print(blu.name,blu.age)
print(woo.name,woo.age)