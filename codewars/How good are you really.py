def better_than_average(class_points, your_points):
    """You receive an array with your peers' test scores. Now calculate the average and compare your score!"""
    if sum(class_points)/len(class_points) <your_points:
        return  True
    else:
        return False
print(better_than_average([2, 3], 5))