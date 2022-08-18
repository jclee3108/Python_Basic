n = 5 

def func_A(level):
    if level >= n:
        return

    print(level, end=' ')
    func_A(level + 1)
    return 
    
func_A(0)