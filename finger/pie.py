from matplotlib import pyplot as plt
import MySQLdb
import xlsxwriter



def entropy(list):
    myset =set(list)
    result=0
    for e in myset :
        f = float(list.count(e))/len(list)
        result+=-1*f*math.log(f,2)
    return result


db = MySQLdb.connect("localhost","xz415","Lr495130811","fingerPrint" )
cursor = db.cursor()

workbook = xlsxwriter.Workbook('Mobile.xlsx')

ro = 0
col =0
worksheet5 = workbook.add_worksheet()
worksheet5.write('A1', 'Attributes', bold)
worksheet5.write('B1', 'Entropy', bold)

cursor.execute("SELECT * FROM finger_key")
results = cursor.fetchall()
list = []
for row in results:
    key = row[0]
    list.append(key)

    sql = 'SELECT ' +key+' FROM finger_db_request
# cursor.execute(sql1)
    # sql = 'SELECT OS FROM finger_db_request'
    cursor.execute(sql)
    values = cursor.fetchall()
    values_list =[]
    for e in values:
        value =e[0]
        values_list.append(value)
    # frequency_list = frequency(values_list)

    entro = entropy(values_list)
    worksheet5.write(ro, col, key)
    worksheet5.write(ro, col + 1,entro)
    ro += 1








