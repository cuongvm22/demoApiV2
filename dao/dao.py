from product.models import Product


def getProductById(productId):
	return Product.objects.filter(id = productId)
