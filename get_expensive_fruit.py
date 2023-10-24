from csv import reader
def get_expensive_fruit(data: str) -> str:
    """
    This function returns the name of the most expensive fruit

    args:
        data: CSV file with the fruits data
    returns:
        str: name of the most expensive fruit
    """
    f=reader(open(data).read().split())
    s=-5426984125412541.0
    l=['']
    for i in f:
        if i[1].isdigit():
            if int(s)<int(i[1]) or float(s)<float(i[1]):
                s=i[1]
                l[0]=i[0]
    return l[0]
print(get_expensive_fruit("fruits.csv"))


