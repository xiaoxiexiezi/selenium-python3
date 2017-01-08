import linecache
import random
import sys
the_line = linecache.getline('/Users/tcw/qqq.txt',0)
print(the_line)
file1 = '/Users/tcw/qqq.txt'
file = open('/Users/tcw/qqq.txt')
for line in file:
    print(line,end='')

# file.close()
# file3 = open('/Users/tcw/qqq.txt')
# print(file3.readlines())
# file.close()

# the_lines = linecache.getlines('/Users/tcw/qqq.txt')[0:1]
# print(the_lines)
#
# qq = '/Users/tcw/qqq.txt'
# count = open(qq).readlines()
# print(count)


# def hello():
#     count1 = len(open('/Users/tcw/qqq.txt','\n').readlines()
#                  len2 = random.randint(0,count1-1)
#     return linecache.getline('/Users/tcw/qqq.txt',hellonum)
# if __name__=='__main__'
#     hello()
#
# print(hello())

#
# def random_read(read_file):
#     count = 0
#     for count, line in enumerate(open('/Users/tcw/qqq.txt', '\n')):
#         count += 1
#
#     line = random.randint(0, count - 1)
#
#     f = open('read_file', 'r').readlines()[line]
#     print(f)
#
#
# def main():
#     if len(sys.argv) != 2:
#         print('use: %s filename' % sys.argv[0])
#         sys.exit(1)
#     read_file = sys.argv[1]
#     random_read(read_file)
#
#
# if __name__ == "__main__":
#     random_read('/Users/tcw/qqq.txt')

# f=open('/Users/tcw/qqq.txt')
# randomLineNumber = int(input('Please input a random line no.:'))
# for i in range(randomLineNumber):
#     x=f.tell()# get the current position of the file
#     f.readline()
#     if x==f.tell():
#         print ("Error: The file only has %d lines, so, "%i+\
#                "it's impossible to get the line you want!!!")
#         exit(1)
# print (f.readline()[:-1])
# f.close()


z = '/Users/tcw/qqq.txt'

count = len(open(z,'rU').readlines())
print('总行数:' + str(count))

qqq = random.randint(1,count)

print(qqq)

count1 = linecache.getline(z,qqq)

count2 = count1[9:20]

print('当前--' + str(count1))

print(count2)
