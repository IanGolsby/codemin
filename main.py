f = open('premin', 'r')

f_text = f.read()

f_text = f_text.replace('\n','')
f_text = f_text.replace('	','')

for c in f_text:
	if c == ' ':
		if f_text[f_text.index(c)-4:f_text.index(c) != 'var ' and f_text[f_text.index(c)-9:f_text.index(c) != 'function ':
				  f_text = f_text.replace(' ','')
