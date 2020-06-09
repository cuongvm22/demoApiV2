from product.models import Product


def getProductById(productId):
	product = Product.objects.filter(id = productId)
	return product
