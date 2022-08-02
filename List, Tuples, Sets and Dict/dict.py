
if __name__=="__main__":
    dict = {
        "firstName":"nishant",
        "lastName":"singh",
        "age":18,
    }
    dict["age"]=19                      #updation
    dict.update({"lastName":"tonger"})  #updation

    dict["bloodGroup"]="B+"             #creation
    dict.update({"rollNo.":"2001920100190"})  #creation

    a = dict.get("lastName")            #accessing
    b = dict["age"]                     #accessing
    c = dict.get("bloodGroup")          #accessing
    d = dict["rollNo."]                 #accessing

    print("LastName={}\nAge={}\nBloodGroup={}\nRollno.={}".format(a,b,c,d))

    dict.pop("age")                     #deletion --> item with the given key
    dict.popitem()                      #deletion --> last Item added
    
    print(dict)
