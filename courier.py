import wap
import sys
import os
import re

def grep(string,list):
    expr = re.compile(string)
    return filter(expr.search,list)

### WA Setup
appid = 'W4RKR2-56RUYWVGRR'
server = 'http://api.wolframalpha.com/v2/query?'
WAengine = wap.WolframAlphaEngine(appid, server)

### Input from command line argument
lines = [line.strip() for line in open(sys.argv[1], 'r')] #Strips newline
output = open('result.txt', 'w')						  #Opens output file
lines = [words.replace(' ', '+') for words in lines]	  #Replaces space with + for WA
lines = [words.replace('arrow', '\\to') for words in lines]

### Query Creation
#WAquery = wap.WolframAlphaQuery("2+2", appid)
#WAquery = wap.WolframAlphaQuery("\lim_{t+\\to+0}\\frac{e^{2t}-1}{e^{t}}", appid)
WAquery = wap.WolframAlphaQuery(lines[1], appid)
#WAquery.AddAssumption('MathWorld')	#Assumption
#WAquery.AddPodID('Result')			#Turn onto only show Result Pod
WAquery.ScanTimeout = '10.0'		#Timeout
WAquery.Async = False				#Async Result collection
WAquery.ToURL()


### Testing output
print "Query:"
print WAquery.Query
print ""

### Format result
result = WAengine.PerformQuery(WAquery.Query)
var=grep('plaintext', result)
print "VAR: "+ var

#if re.search('<plaintext>', result):
	#print re.search('^<plaintext>$', result, re.M).group()
#for line in result:
	#if re.search('<plaintext>', result):
	#	sys.stdout.write(line)
		
### Write result to file
#output.write(result)
WAresult = wap.WolframAlphaQueryResult(result)

### Print result in Pods
#for pod in WAresult.Pods():
#	WApod = wap.Pod(pod)
#	WAsubpod = wap.Subpod(pod)
#	#print('\n%s: %s ' % (WApod.Title(), WApod.Subpods()))
#	print("Subpod")
#	print('\n%s: %s ' % (WAsubpod.Title(), WAsubpod.Plaintext()))
