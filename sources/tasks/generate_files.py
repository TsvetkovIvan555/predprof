for i in range(27):
    for j in range(3):
        if(i < 10):
            file_title = "task_0" + str(i)
        else:
            file_title = "task_" + str(i)
        file_title += "_" + str(j) + "_000000" + ".txt"
        f = open(file_title, 'w')
        s = "This is task of type " + str(i+1) + " with difficulty " + str(j+1) + " and answer 1" + "\n"
        f.write(s)
        s = "1" + "\n"
        f.write(s)
        s = "Explanation" + "\n"
        f.write(s)        
        f.close()