##Simple File open and read the data
# f = open("demo.txt", 'r')
# print(f.read())

##Simple File open and read the line
# f = open("demo.txt", 'r')
# print(f.readline())

##Simple File open and write the data
# f = open("write.txt", 'w')
# f.write("Something")

##Simple File open and append the data
# f = open("write.txt", 'a')
# f.write(" People")

##Simple File open and read and write the data in second file
##Read
# f = open("demo.txt", 'r')
##Write
# f1 = open("write.txt", 'w')
# for data in f:
#     f1.write(data)

##Open Image and Copy/paste image
# f = open("man-01.png", "rb")
# f1 = open("MyPic.png", "wb")

# for i in f:
#     f1.write(i)


# x = input("Enter Number: ")
# d = open("write.txt", 'a')
# data = d.write(x)
# if x in data:
#     print(data)
# else:
#     d = open("write.txt", 'r+')
#     data = d.truncate(x)

# votedData = open("demo.txt", "r")
# VotedData = votedData.read().split(sep=" ")
# for item in VotedData:
#         voter = item
#         print(voter)
