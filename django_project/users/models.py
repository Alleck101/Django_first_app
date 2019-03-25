from django.db import models
from django.contrib.auth.models import User
from PIL import Image


class Profile(models.Model):
	user = models.OneToOneField(User, on_delete=models.CASCADE)
	image = models.ImageField(default='default.jpg', upload_to='profile_pics')

	def __str__(self):
		return f'{self.user.username} Profile'


	"""
	↓ Save() redefinition.
	I redefined save method in user app, so that it will resize large images into smaller ones.
	If image H or W is greater than 300, it will be resized upon saving.

	PROBLEM SOLVED -> images stored on drive will be smaller and website will load faster.
	"""

	#TODO: Delete old images after updating to new
	def save(self):
		super().save()

		img = Image.open(self.image.path)

		if img.height > 300 or img.width > 300:
			output_size = (300, 300)
			img.thumbnail(output_size)
			img.save(self.image.path)


"""
!TODO!
class Bio(models.Model):
	user = models.OneToOneField(User, on_delete=models.CASCADE)
"""