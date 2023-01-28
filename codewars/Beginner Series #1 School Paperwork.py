def paperwork(n, m):
    '''
    Your task is to calculate how many blank pages do you need. If n < 0 or m < 0 return 0.
    '''
    if n<0 or m<0:
        return 0
    else:
        return n*m
