# TASK n3

# input: vector x of numbers (int, floats)

# sum of vector elements

def _sum(x):
    sum = 0
    for el in x: #take every element in a vector and add up to sum variable
        sum += el
    return sum

# product of vector elements

def _prod(x):
    prod = 1
    for el in x:
        prod *= el
    return prod

# mean value of vector

def _mean(x):
    return _sum(x)/len(x) # divide sum by length of vector 

# max value in a vector

def _max(x):
    max = x[0]
    for el in x:
        if el > max:
            max = el
    return max

# first index at which we get max value in vector

def _max_ind(x):
    max = _max(x)
    for i in range(len(x)):
        if x[i] == max:
            return i

# vector of indexes with max value in a vector

def _max_ind_vect(x):
    max = _max(x)
    res = []
    for i in range(len(x)):
        if x[i] == max:
            res.append(i)
    return res

# indexes of non-zero elements in a vector

def _nz_val_ind(x):
    return [i for i in range(len(x)) if x[i] != 0]

# partial sums of vector elements

def _part_sums(x):
    res = []
    for i in range(1, len(x)+1):
        res.append(_sum(x[:i]))
    return res

# partial products of vector elements
def _part_prods(x):
    res = []
    for i in range(1, len(x)+1):
        res.append(_prod(x[:i]))
    return res

# main() function is only called when you execute the script as "python3 vector_funcs.py"

def main():
    print(_part_sums([1, 2, 3, 4, 5, 6]))
    print(_part_prods([1, 2, 3, 4, 5, 6]))
    print(_nz_val_ind([0,4, -3, 0, 1, 9, 0, 82, 7]))

if __name__ == '__main__':
    main()
