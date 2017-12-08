#coding:utf-8
class home:
    def __init__(self,home_area):
        self.home_area = home_area
        self.left_area = home_area
        self.add_name = []
    def __str__(self):
        return "该房子面积是：%d平方米\n剩余面积是：%d平方米\n添加的物品：%s"%(self.home_area,self.left_area,str(self.add_name).decode("string_escape"))

    def add_bed(self,add):
        # self.left_area -= add.bed_area
        # self.add_name.append(add.bed_name)
        self.left_area -= add.get_area()
        self.add_name.append(add.get_name())

class bed:
     def __init__(self,bed_name,bed_area):
         self.bed_name = bed_name
         self.bed_area = bed_area
     def __str__(self):
         return "%s面积是：%d"%(self.bed_name,self.bed_area)
     def get_name(self):
         return self.bed_name
     def get_area(self):
         return self.bed_area

my_home = home(100)

my_bed = bed("席梦思",5)
my_bed1 = bed("不知道",3)

my_home.add_bed(my_bed)
my_home.add_bed(my_bed1)
print my_home
