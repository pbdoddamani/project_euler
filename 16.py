str_format = str(pow(2, 1000))
summation =  0
for i in str_format:
    summation += int(i)
print "summation of pow(2, 1000) is %s", summation
