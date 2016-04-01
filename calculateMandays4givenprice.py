"""
this script will suggest the offshore and onstie mandays for a given price
it is useful when you want to find mandays that give you closet total price to
your target price
"""
rate_offshore = 455
rate_onsite = 570
#MAX distance should be always less than offshore rate (which is the smaller of 2)
MAX_distance = 50
#assign the target price here
target_price = 221238

####################################
#mandy function calculate and prints out all the combinations of offshore/onstie mandays
#that are close to the expected price

def manday(price):
    off = price /rate_offshore
    on = price / rate_onsite
    distance = rate_onsite
    OK_rate = 0
    counter = 0
    #print "Max_offshore :%i, Max_onsite : %i" %(off,on)
    if price < rate_offshore:
        return -1
    for i in range(0,off+2):
        start = abs((price - (i * rate_offshore))/ rate_onsite)        
        for j in range(start,on+2):
            calc = i*rate_offshore + j*rate_onsite
            if (abs(price - calc) <= MAX_distance) : 
                 
                distance = abs(price - calc)
                if (distance == 0) :
                    OK_rate += 1 
                    out = " | distance :"+str(distance)  + "   <OK>("+str(OK_rate)+")"
                else:
                    out = " | distance :"+str(distance) 
                counter +=1
                print "%2i)"%(counter),"off:%4i (%6i)|On:%4i(%6i)"%(i,i*rate_offshore,j,j*rate_onsite), "|total = "+str(calc)+"|"+str(round(float(i)/(i+j),2)*100)+"% / "+str(round(float(j)/(i+j),2)*100)+"%"+ out             
            #counter +=1

manday(target_price)

 
