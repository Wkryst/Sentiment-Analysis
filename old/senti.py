# POS ID PosScore NegScore SynsetTerms Gloss
while 1:
	try:
		x = raw_input();
		y = x.split("\t")
		p = float(y[2])
		n = float(y[3])
		if (p == 0.0 and n == 0.0): continue
		if (p >= 0.125 and n == 0.0): print x
		if (p == 0.125 and n < 0.375): continue
		if (p == 0.0 and n >= 0.125): print x 
		if (p < 0.375 and n == 0.125): continue
		if (p >= 0.25 and n >= 0.25): continue
		print x
	except EOFError:
		break
	except:
		continue
