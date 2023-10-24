from csv import reader
def get_cheapest_fruit_id(data: str) -> int:
    """
    This function returns the index of the cheapest fruit

    args:
        data (str): CSV file with the fruits data
    returns:
        int: id of the cheapest fruit
    """
    f=reader(open(data).read().split())
    s=5426984125412541
    for i in f:
        if i[1].isdigit():
            if int(s)>int(i[1]):
                s=i[1]
    return s
print(get_cheapest_fruit_id("fruits.csv"))