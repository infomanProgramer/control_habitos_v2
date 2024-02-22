# tablaEquivalencias = open("TablaEquivalencias.csv", "r")
migracionDatos = open("MigracionData.csv", "r")




def getEquivalenteId(id_eq):
    tablaEquivalencias = open("TablaEquivalencias.csv", "r")
    rowTE = tablaEquivalencias.readline()
    idret = 0
    while rowTE != "":
        rowTEArray = rowTE.split(",")
        if rowTEArray[4] == id_eq:
            idret = rowTEArray[0]

        rowTE = tablaEquivalencias.readline()

    return str(idret)

def convertStringToDate(fecha):
    # print(fecha)
    dd = fecha.split("/")[0]
    mm = fecha.split("/")[1]
    yy = fecha.split("/")[2]
    if len(dd) == 1:
        dd = "0"+dd
    if len(mm) == 1:
        mm = "0"+mm
        
    newDate = "(SELECT date('"+str(yy)+"-"+str(mm)+"-"+str(dd)+" 00:00:00') as 'DATE()')"
    return newDate



query = "INSERT INTO SEGUIMIENTOHABITOS (ID_HABITO, ESTADO, FECHA_REGISTRO) VALUES "

# print("********************************")
# print(convertStringToDate("15/2/2024"))

migraRow = migracionDatos.readline()
while migraRow != "":
    migraFila = migraRow.split(",")
    query = query + "("+getEquivalenteId(migraFila[1])+",True, "+convertStringToDate(migraFila[0])+"), \n"
    migraRow = migracionDatos.readline()
query = query + ";"
#print(query)

archivoOutH = open('inserHabitos.sql', 'a')

archivoOutH.write(query)

archivoOutH.close()


