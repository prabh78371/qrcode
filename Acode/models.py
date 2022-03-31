from django.db import models
import qrcode
from io import BytesIO
from django.core.files import File
from PIL import Image,ImageDraw

# Create your models here.
class modelqrp(models.Model):
    name = models.CharField(max_length=15)
    code = models.ImageField(upload_to = 'images',blank=True)

    def save(self,*args, **kwargs):
        qr_image = qrcode.make(self.name)
        qroffset = Image.new('RGB',(310,310),'white')
        draw = ImageDraw.Draw(qroffset)
        qroffset.paste(qr_image)
        files_name=f'{self.name}-{self.id}qr.png'
        strem=BytesIO()
        qroffset.save(strem,'PNG')
        self.code.save(files_name,File(strem),save=False)
        qroffset.close()
        super().save(*args,**kwargs)
