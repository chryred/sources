try :
	print(param)
#except Exception as e:
except NameError as ne:
	print(ne)
except Exception as e:
	print(e)