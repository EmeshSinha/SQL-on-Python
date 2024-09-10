import os as os

def newtable(tablename):
    command = "echo > databases/tables/"+tablename +".csv"
    print(command)
    os.system(command)