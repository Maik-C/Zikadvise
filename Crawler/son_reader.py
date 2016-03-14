import json
from sys import argv

script, filename, outname = argv

reader = open(filename)
data = reader.read()

data_parsed = []
writer = open(outname+'.txt', 'w')
for line in open(filename):
	data_parsed.append(json.loads(line))

#write everything from the JSON file to MySQL by separating with tabs
#each entry a new line
#current sorting: username userlanguage usermessage about #topic userlocation
#TODO make null --> \n 
for i in range(len(data_parsed)):
	try:
		print i
		if (data_parsed[i]['user']['lang'] == "en"):
			writer.write(data_parsed[i]['user']['screen_name']+"\t")
			writer.write(data_parsed[i]['user']['lang']+"\t")
			writer.write(repr(data_parsed[i]['text'])+"\t")
			writer.write(repr(data_parsed[i]['user']['location']) + "\n")
			writer.write("\n")
	except KeyError:
		continue
#print data_parsed['user'][0][0]
#writer.write(json.dumps(data_parsed, indent=4, sort_keys=True))
