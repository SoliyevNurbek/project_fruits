from csv import reader
def get_total_price(data:str)->float:
    """
    This function returns the total price of the fruits

    args:
        data: CSV file with the fruits data
    returns:
        float: fruits total price
    """
    f=reader(open(data).read().split())
    s=0.0
    for i in f:
        if i[1].isdigit():
            s+=float(i[1])
    return s
print(get_total_price("fruits.csv"))
    