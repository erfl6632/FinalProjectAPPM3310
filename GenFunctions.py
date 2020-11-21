def ArrayToStatespace(lagVal, array){
    valid = False  #valid input?
    ODA = [] #one dimension array
    for i in array:
        for j in array[i]:
            ODA.append(array[i][j])
    dim = ODA.len() - lagVal
    stspA = [] # state space array
    for i in dim:
        for j in dim:
            stspA[i][j] = 

