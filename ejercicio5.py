def hollow_triangle(height):
    #create an empty list to store each line of the triangle
    triangle = []
    #iterate from 1 to the value of height+1
    for i in range(1, height + 1):
        #if the current iteration is 1 or equal to the value of height
        if i == 1 or i == height:
            #append the triangle list with a string of # characters that is 2 times the value of height minus 1
            triangle.append('#' * (2 * height - 1))
        else:
            #otherwise append the triangle list with a string that starts and ends with _ characters
            #with the number of _ characters being height-i on the left and right
            #with a # in the middle, followed by _ characters
            #with the number of _ characters being 2*i-3
            triangle.append('_' * (height - i) + '#' + '_' * (2 * i - 3) + '#' + '_' * (height - i))
    #return the triangle list
    return triangle

print(hollow_triangle(6))
print(hollow_triangle(9))
