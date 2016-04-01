# this code reads all the keys in the translation file and finds, print duplicates
#
#

infile = open("clm.js")
#infile = open("dic.txt")
keylist =[]
counter = 0
for line in infile:
    pos1 = line.find('"')
    pos2 = line.find('"',pos1+1)
    pos3 = line.find('"',pos2+1)
    pos4 = line.find('"',pos3+1)
    #print "key :%s , value :%s" %(line[pos1+1:pos2],line[pos3+1:pos4])
    if line[pos1+1:pos2] in keylist:
        counter += 1
        print "%i) '%s' is a duplicate!" %(counter,line[pos1+1:pos2])
        
    else:   
        keylist.append(line[pos1+1:pos2])
infile.close()

    
