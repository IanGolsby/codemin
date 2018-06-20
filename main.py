f = open('premin', 'r')

f_text = f.read()

f_text = f_text.replace(' ','')
f_text = f_text.replace('\n','')
f_text = f_text.replace('	','')
