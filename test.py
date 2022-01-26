class Oi:
    def __init__(self):
        self.oi = 1

def change(x: Oi):

    x.oi = "oi"

a = Oi()
print(a.oi)
change(a)
print(a.oi)