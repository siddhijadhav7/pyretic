class MyError()
	try:
		print "Exception Handling example"
		i1=int(raw_input("Enter first number: "))
		i2=int(raw_input("Enter second number: "))
		res=i1/i2
		print "result of division of ",i1," and ",i2," is : ",res
		import Employee
	except ImportError:
	  print "Imported file not found"
	except KeyboardInterrupt:
	  print "You pressed ctrl+c ..therefore program is terminated"
	except ZeroDivisionError:
	  print "you are trying to divide by zero"
	except:
	  print "Intrrupt occurred"
	else:
	  print "program is executed without any exception"



