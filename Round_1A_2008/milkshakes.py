""" Check if each customer can be satisfied
    If a customer can't be satisfied, return his id
    Else return None
"""
def get_unsatisfied_customer(flavors, customers, n_customers):
    for i in range(n_customers):
        # check if he can get what he wants
        satisfied = False
        # a flavor is a tuple : (flavor_id, malted_or_not)
        for flavor in customers[i]:
            if flavors[flavor[0]-1] == flavor[1]:
                satisfied = True
                break
        if not satisfied:
            return i
    return None

""" If the flavors contains a malted flavor, return the ID of the flavor
    Else, return None
"""
def get_customer_malted_flavor(flavors):
    for flavor in flavors:
        if flavor[1] == 1:
            return flavor[0]
    return None

f_name = "B-large-practice"
f_in = open(f_name + ".in", "r")
f_out = open(f_name + ".out", "w")

# for each test case
for test_case in range(int(f_in.readline().strip())):
    n = int(f_in.readline().strip())    # number of flavors
    m = int(f_in.readline().strip())    # number of customers
    # create the list of flavors, UNMALTED initially
    flavors = [0] * n
    # read customers and save their flavors
    customers = [None] * m
    for i in range(m):
        # data[0] is the number of flavor he likes
        # the other elements are pairs : p[j] is the flavor id and p[j+1] is malted or unmalted 
        data = list(map(int, f_in.readline().strip().split()))
        nb_flavors_he_like = data[0]
        # remember each flavor he likes
        customer_flavors = [None] * nb_flavors_he_like
        j = 1
        while j <= nb_flavors_he_like:
            customer_flavors[j - 1] = (data[j*2 - 1], data[j * 2])
            j += 1
        customers[i] = customer_flavors
    # check if there is an unsatified customer
    unsatified = get_unsatisfied_customer(flavors, customers, m)
    flag = False
    while unsatified != None and not flag:
        # check if he has a malted flavor
        malted_flavor = get_customer_malted_flavor(customers[unsatified])
        if malted_flavor == None:
            flag = True
        else:
            flavors[malted_flavor - 1] = 1
            unsatified = get_unsatisfied_customer(flavors, customers, m)
    
    # if flag => it's impossible. Else, print the flavors configuration
    answer = "IMPOSSIBLE" if flag else ' '.join([str(f) for f in flavors])
    f_out.write("Case #{}: {}\n".format(test_case+1, answer))