class MyHashMap():
    def __init__(self):
        self.hashm={}
    def put(self,key:int,value:int)->None:
        self.hashm[key]=value
    def get(self,key:int)->int:
        if key in self.hashm:
            return self.hashm[key]
        return -1
    def remove(self,key:int)->None:
        if key in self.hashm:
            del self.hashm[key]
        return None
            
        