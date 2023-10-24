
from csv import reader
def get_frutis_name(data:str)->list:
    """
    This function returns the names of the fruits

    args:
        data: CSV file with the fruits data
    returns:
        list: list of fruits names
    """
    f=reader(open(data).read().split())
    l=[]
    for i in f:
        if i[0]!='name':
            l.append(i[0])
    return l
print(get_frutis_name("fruits.csv"))


    