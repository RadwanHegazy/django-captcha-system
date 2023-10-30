from django.db import models
import ast

class ImageModel (models.Model) : 
    big_image = models.ImageField(upload_to='captcha-images/')
    small_image = models.ImageField(upload_to='small-images/')
    info = models.TextField()
    uuid = models.UUIDField(null=True,blank=True)

    def __str__(self) -> str :
        return f"{self.big_image.name}"
    
    def get_info_as_dict (self) -> dict :
        return ast.literal_eval(self.info)