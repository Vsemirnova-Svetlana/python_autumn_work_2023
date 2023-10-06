x= ['abab','fhj','fop','xx','fnmvcboo','ww','bb','ubyuhy','ubz','ubi','aaa']
def sort(l):

    return len(set(l)), -ord(l[0]),-ord(l[-1])

print(sorted(x, key = sort, reverse=True))