def sort(dict):
    sorted_dict={}
    for i in sorted(dict.values()):
        for k in dict.keys():
            if dict[k]==i:
                sorted_dict[k]=dict[k]
                break
    
    return sorted_dict

    


if __name__=="__main__":
    dict = {"4":"545","3":"223","1":"244","2":"248"}
    print(sort(dict))
    
