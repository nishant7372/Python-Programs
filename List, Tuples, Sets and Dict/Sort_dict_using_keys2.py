def sort(dict):
    sorted_dict={}
    for i in sorted(dict.keys()):
        sorted_dict[i]=dict[i]
    
    return sorted_dict

    


if __name__=="__main__":
    dict = {"4":"545","3":"223","1":"244","2":"248"}
    print(sort(dict))
    
