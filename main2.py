class Hero:
    name = ""
    def get_name(self):
        return self.name


h = Hero()
h.name = "佐々木"

a=3
b = 1 + 2
b = 3 
print(id(a))
print(id(b))