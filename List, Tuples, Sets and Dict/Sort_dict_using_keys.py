from collections import OrderedDict

def sort(dict):
    dict = OrderedDict(sorted(dict.items()))
    return dict;


if __name__=="__main__":
    dict = {"4":"545","3":"223","1":"244","2":"248"}
    print(sort(dict))
    
