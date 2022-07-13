def main(x,y):
    """
    Given three integers, x, y, return the "(x+y)*2={answer}" string.
    Args:
        x: int
        y: int
    Returns:
        str: return answer.  "(x+y)*2={ifoda natijasi}" 
    """
    return "\"("+str(x)+"+"+str(y)+")*2="+str((x+y)*2)+"\""
print(main(2,3))