
def difference(h1, m1, h2, m2): 
	
	
	t1 = h1 * 60 + m1 
	
	 
	t2 = h2 * 60 + m2 
	
	if (t1 == t2): 
		print("Both are same times") 
		return
	else: 
		
		
		diff = t2-t1 
		

	h = (int(diff / 60)) % 24
	

	m = diff % 60

	print(h, ":", m) 


if _name_ == "_main_": 
	
	difference(7, 20, 9, 45) 
	difference(15, 23, 18, 54) 
	difference(16, 20, 16, 20) 

