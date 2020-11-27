def swap():
    filename1 = input("file name to swap data in :")
    filename2 = input("file name to swap data in :")

    filedata1 = open(filename1, "r")
    filedata2 = open(filename2, "r")

    for word1 in filedata1 :
        word1.split(" ")

    for word2 in filedata2 :
        word2.split(" ")

    with open(filename1 , "w") as a:
        a.write(word2)

    with open(filename2 , "w") as b:
        b.write(word1)     

    result1 = open(filename1, "r")
    result2 = open(filename2, "r")

    for results1 in result1:
        results1.split(" ")
    for results2 in result2:
        results2.split(" ")

    print( results1 )
    print( results2 )                   

swap();    