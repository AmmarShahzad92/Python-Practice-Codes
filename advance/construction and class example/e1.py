class car:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model
    
    def show_details(self):
        print(self.brand,"\n",self.model)

c1 = car("honda", "cd70")
c1.show_details()