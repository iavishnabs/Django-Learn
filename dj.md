## adding media files from backend

pip install pillow 

### models.py

* class table(inherit from model):
* img = models.imagefield(upload_to= 'productimages')

### settings.py

* MEDIA_URL = '/media/'
* MEDIA_ROOT = os.path.join(BASE_DIR,'uploads')

### urls.py in app folder

* from django.conf import settings
* from . conf.urls.static import static

* urlpatterns=[
] + static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)


### html file
* {% for i in items %}
* <img src="{{i.img.url}}" alt = ""/>
* {% endfor %}
