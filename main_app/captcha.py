from PIL import Image, ImageDraw
from random import randint
import requests, uuid, urllib.request



class Captcha :

    def __init__(self, img_path) -> None :

        self.original_image = Image.open(img_path)
        self.original_image = self.original_image.resize(size=(200,200))

        self.w, self.h = self.original_image.size
        
        self.generate_captcha()

    def generate_captcha (self) :

        while True :
            try :
                box = (
                        randint(10, self.w) ,  
                        randint(10, self.h) ,
                        randint(self.w / 2, self.w) ,
                        randint(self.w / 2,self.h)
                    )
                self.object = self.original_image.crop(box)
                break
            except ValueError :
                pass

        self.correct_x = box[0]
        self.correct_y = box[1]


        rectangle = ImageDraw.Draw(self.original_image)

        rectangle.rectangle(box, fill ="#000") 
        big = self.original_image

        big_width = big.width
        big_height = big.height

        small = self.object

        small_width = small.width
        small_height = small.height

        self.get_obj_width = round(( small_width / big_width ) * 100) + 1
        self.get_obj_height = round(( small_height / big_height ) * 100) + 1

    def info (self) -> dict :
        context = {
            "object_x" : (self.correct_x , self.correct_x + 100 ),
            "object_y" : (self.correct_y , self.correct_y + 100 ),
            "object_width" : self.get_obj_width,
            "object_height" : self.get_obj_height,
        }

        return context
