from django.db import models


class Tag(models.Model):
    tagName = models.CharField(max_length=100)
	
class Product(models.Model):
	seller = models.CharField(max_length=50)
	description = models.CharField(max_length=200)
	price = models.FloatField()
	item_condition = models.CharField(max_length=50)
	contact = models.CharField(max_length=200)
	post_date = models.DateField()
	product_image = models.CharField(max_length=200)

class ProductTags(models.Model):
	tags = models.ManyToManyField(Tag)
	products = models.ManyToManyField(Product)

class User(models.Model):
	username = models.CharField(max_length=50)
	password = models.CharField(max_length=50)
	name = models.CharField(max_length=50)

class Review(models.Model):
    users = models.ManyToManyField(User)
    products = models.ManyToManyField(Product)
    rating = models.IntegerField()
	
class ReviewRating(models.Model):
	reviews = models.ManyToManyField(Review)
	users = models.ManyToManyField(User)