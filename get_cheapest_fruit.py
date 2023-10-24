from csv import reader
def get_cheapest_fruit(data: str) -> str:
    """
    This function returns the name of the cheapest fruit

    args:
        data: CSV file with the fruits data
    returns:
        str: name of the cheapest fruit
    """
    f=reader(open(data).read().split())
    s=5426984125412541
    l=['']
    for i in f:
        if i[1].isdigit():
            if int(s)>int(i[1]):
                s=i[1]
                l[0]=i[0]
    return l[0]
print(get_cheapest_fruit("fruits.csv"))