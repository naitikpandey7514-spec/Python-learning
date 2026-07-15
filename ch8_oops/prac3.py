class student:
    def __init__(self,name,marks):
        self.name = name
        self.marks = marks
    def get_avg(self):
        sum = 0
        for val in self.marks:
            sum += val
        print("hey", self.name,"your avg marks is:",sum/3)        

s1 = student("naitik", [70,80,90])
s1.get_avg()

