
def createObjectDB(key, value, typeData):
    obj = {
        "key": key,
        "value": value,
        "typeData": typeData
    }
    return obj

def addNewItemDB(tableName, params):
    claves = "("
    valores = "("
    coma = ","
    for item in range(0, len(params), 1):
        if item == len(params)-1:
            coma = ""
        claves = claves + params[item]["key"]+coma
        if(params[item]["typeData"] == "T"):
            valores = valores + "'" +str(params[item]["value"])+"'"+coma
        else:
            valores = valores+str(params[item]["value"])+coma
    
    claves = claves + ")"
    valores = valores +")"
    query = "insert into " + tableName + " "+claves+" values "+valores
    #print(query)
    return(query)