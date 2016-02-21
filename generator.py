import random;

formats = open('formats').read().split('\n');

types = ['names', 'nouns', 'units', 'updowns', 'persons', 'ages', 'n2ouns', 'futures', 'verbs', 'adjectives'];

for i in types:
	exec(i+' = open("'+i+'").read().split(",");');

def generateHeadline():
	format = random.choice(formats);
	for i in types:
		exec('format = format.replace("$'+i[:-1].upper()+'$", "'+random.choice(eval(i))+'");');
	return format.replace("$NUMBER$", str(random.randrange(100)));

print generateHeadline();