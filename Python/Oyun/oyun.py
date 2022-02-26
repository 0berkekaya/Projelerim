import random

class Creator_Functions:

    def Hunter_Creator():
        start_Level=random.randint(1,5)
        return GameObjects.Hunter_Object(start_Level)

        
    def Monster_Creator(available_hunter_level):
        print("Canavar Üretildi.")
        return GameObjects.Monster_Object(available_hunter_level)





class GameObjects:

    class Hunter_Object:
        def __init__(self,level):
            self.name="Avcı "+str(level)
            self.level=int(level)
            self.damage=level*5
            self.kill=0
            self.heart=level*10
    
    class Monster_Object:
        def __init__(self,level):
            self.name="Canavar"+str(level)
            self.level=level
            self.damage=level*3
            self.heart=level*6


class MyInventory:
    hunters=[]
    gold=0
    level=0
    totalKill=0

class Controller:
    def Point():
        print("as")

class Functions:

    def InventoryClear():
        MyInventory.hunters.clear()
        MyInventory.gold=0
        MyInventory.level=0
        MyInventory.totalKill=0


    def Menu(ans):

        menuBank={

            1:
            MyInventory.hunters.count
            ,
            2:"Sanane",
            4:"Merhba"
        }

        return menuBank[ans]






    def Game():
        
        myInventory=MyInventory()

        print("Hoşgeldin")
        print("Savaşman için sana 1 adet avcı vereceğim.")

        myInventory.hunters.append(Creator_Functions.Hunter_Creator())
        
        print("Bu avcı ile canavarları temizle ve altın kazan.")



        while True:

            print(Functions.Menu(int(input("Seçim : "))))







Functions.Game()