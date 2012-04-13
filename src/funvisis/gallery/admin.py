import os
import zipfile

from django.conf import settings
from django.contrib.admin import ModelAdmin
from django import forms
from django.core.files.uploadedfile import SimpleUploadedFile
from django.core.files.base import ContentFile
from django.template.defaultfilters import slugify

from photologue.models import Gallery
from photologue.models import Photo
from photologue.models import ImageModel

from fvislib.utils.djangorelated import open_zip_file, load_zip_file, verify_image

# Photologue image path relative to media root
PHOTOLOGUE_DIR = getattr(settings, 'PHOTOLOGUE_DIR', 'photologue')

class GalleryZipForm(forms.ModelForm):
    zipfile = forms.FileField(required=False)
    #cleaned_data = { 'photos': [] }    

    class Meta:
        model = Gallery


class FvisGalleryAdmin(ModelAdmin):
    
    form = GalleryZipForm
    filter_horizontal = ('photos',)

    def get_title(self, gallery, photo_name):
        return gallery.title + photo_name

    def get_slug(self, gallery, photo_name):
        return slugify(self.get_title(gallery, photo_name))

    def get_tags(self, photo_name):
        return ''

    def save_model(self, request, obj, form, change):
        files = {}
        if 'zipfile' in request.FILES :
            photolist = load_zip_file(request.FILES['zipfile'])
            files = photolist
        obj.save()
        photos = []
        for photo_name in files:
            if not verify_image(files[photo_name]):
                continue
            title = self.get_title(obj, photo_name)
            slug = self.get_slug(obj, photo_name)
            tags = self.get_tags(photo_name)
            photo = Photo(title=title,
               title_slug=slug,
               caption=title,
               is_public=obj.is_public,
               tags=tags)
            photo.image.save(photo_name, ContentFile(files[photo_name]))
            photo.save()
            photos.append(photo)
        cleaned_data = self.form.clean(form)
        for photo in photos:
            cleaned_data['photos'].append(photo)
        return obj


