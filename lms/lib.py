import json

def saveData(data):
    with open('data.json', 'w') as outfile:
        json.dump(data, outfile, ensure_ascii=False)
    
def checkDataMon(data_mon, cauhoi, dapandung ):  
    count = 0

    for r in range (0,len(data_mon)) :
        if(data_mon[r]['cauhoi'] == cauhoi and data_mon[r]['dapandung']==dapandung  ):
                count += 1

    return count

def getDapanDung(data_mon, cauhoi ):  
    dapandung = []

    for r in range (0,len(data_mon)) :
        if(data_mon[r]['cauhoi'] == cauhoi):
           dapandung.append(data_mon[r]['dapandung'])      

    return dapandung
       


def checkKey(database, ma_mon):
    if ma_mon in database.keys():       
        pass
    else:
        data = {ma_mon:[]}
        database.update(data)
        saveData(database)


def getDataMon(ma_mon):
    with open('data.json', encoding='utf-8') as outfile:
        database = json.load(outfile)
        checkKey(database, ma_mon)

        return database


