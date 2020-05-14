def solve(nh,nl):
    for i in range(nh+1):
        j = nh -1
        if 2*i+4*j == nl:
            return i,j
    return nh,nl


sol = solve(35,94)
print(sol)