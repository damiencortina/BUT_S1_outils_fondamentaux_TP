def transposee(A):
    a_transposee = []
    for lineKey, lineValue in enumerate(A) :
        for columnKey, columnValue in enumerate(lineValue) :
            if(lineKey == 0):
                a_transposee.append([])
            a_transposee[columnKey].append(columnValue)
    return a_transposee

def produit(A,B):
    C = []
    for lineKey, lineValue in enumerate(A):
        for columnKey, columnValue in enumerate(A):
            line = lineValue
            value = 0
            for
            