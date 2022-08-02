class MyNumbers:
    def __iter__(self):
        self.a=1
        return self
    def __next__(self):
        x=self.a
        self.a+=1
        return x

if __name__=="__main__":
    myClass = MyNumbers();
    myIter = iter(myClass)

    for i in range(20):
        print(next(myIter),end=", ")
   
