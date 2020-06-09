from dao import dao

def getProductById(idProduct):
	product = dao.getProductById(idProduct)
	return product

