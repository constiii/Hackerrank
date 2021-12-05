def formingMagicSquare(s, combis):

    # initialize minimum costs
    min_cost = int(99999)

    # evaluate minimum cost for each magical square combination
    for combi in combis:
        combi_cost = int(0)

        for i in range(0, len(combi)):
            for j in range(0, len(combi[i])):

                value_s = int(s[i][j])
                value_combi = int(combi[i][j])
                combi_cost += int(abs(value_s - value_combi))

        if combi_cost < min_cost:
            min_cost = combi_cost
        else:
            pass
    
    return min_cost

if __name__ == "__main__":
    s = [[5, 3, 4], [1, 5, 8], [6, 4, 2]]
    combis = [
         [[8, 1, 6], [3, 5, 7], [4, 9, 2]],
         [[6, 1, 8], [7, 5, 3], [2, 9, 4]],
         [[4, 9, 2], [3, 5, 7], [8, 1, 6]],
         [[2, 9, 4], [7, 5, 3], [6, 1, 8]], 
         [[8, 3, 4], [1, 5, 9], [6, 7, 2]],
         [[4, 3, 8], [9, 5, 1], [2, 7, 6]], 
         [[6, 7, 2], [1, 5, 9], [8, 3, 4]], 
         [[2, 7, 6], [9, 5, 1], [4, 3, 8]],
         ]
    print(formingMagicSquare(s, combis))
