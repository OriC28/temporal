
def ave_spd(t1, v1, v2):
	# minute --> hours
	t1 = t1/60
	# distance
	d = t1*v1
	# second time
	t2 = d/v2
	return int(2*d/(t1 + t2))


print(ave_spd(30, 8, 24))