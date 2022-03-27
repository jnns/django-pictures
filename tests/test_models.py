from fractions import Fraction
from pathlib import Path

import pytest
from django.core.files.storage import default_storage
from PIL import Image

from pictures.models import PictureField, SimpelPicture
from tests.testapp.models import Profile, SimpleModel


class TestSimplePicture:

    picture_with_ratio = SimpelPicture(
        parent_name="testapp/simplemodel/image.jpg",
        file_type="WEBP",
        aspect_ratio=Fraction("4/3"),
        storage=default_storage,
        width=800,
    )

    picture_without_ratio = SimpelPicture(
        parent_name="testapp/simplemodel/image.jpg",
        file_type="WEBP",
        aspect_ratio=None,
        storage=default_storage,
        width=800,
    )

    def test_url(self):
        assert (
            self.picture_with_ratio.url
            == "/media/testapp/simplemodel/image/4_3/800w.webp"
        )

    def test_height(self):
        assert self.picture_with_ratio.height == 600
        assert not self.picture_without_ratio.height

    def test_name(self):
        assert Path(self.picture_without_ratio.name) == Path(
            "testapp/simplemodel/image/800w.webp"
        )
        assert Path(self.picture_with_ratio.name) == Path(
            "testapp/simplemodel/image/4_3/800w.webp"
        )

    def test_path(self):
        assert self.picture_with_ratio.path.is_absolute()

    def test_save(self):
        assert not self.picture_with_ratio.path.exists()
        self.picture_with_ratio.save(Image.new("RGB", (800, 800), (255, 55, 255)))
        assert self.picture_with_ratio.path.exists()

    def test_delete(self):
        self.picture_with_ratio.save(Image.new("RGB", (800, 800), (255, 55, 255)))
        assert self.picture_with_ratio.path.exists()
        self.picture_with_ratio.delete()
        assert not self.picture_with_ratio.path.exists()


class TestPictureFieldFile:
    @pytest.mark.django_db
    def test_save(self, image_upload_file):
        obj = SimpleModel(picture=image_upload_file)
        obj.save()

        assert default_storage.exists(obj.picture.name)
        assert obj.picture.aspect_ratios["16/9"]["WEBP"][100].path.exists()

    @pytest.mark.django_db
    def test_delete(self, image_upload_file):
        obj = SimpleModel(picture=image_upload_file)
        obj.save()

        name = obj.picture.name
        path = obj.picture.aspect_ratios["16/9"]["WEBP"][100].path
        assert default_storage.exists(name)
        assert path.exists()

        obj.picture.delete()
        assert not default_storage.exists(name)
        assert not path.exists()


class TestPictureField:
    @pytest.mark.django_db
    def test_integration(self, image_upload_file):
        obj = SimpleModel.objects.create(picture=image_upload_file)
        assert obj.picture.aspect_ratios == {
            None: {
                "WEBP": {
                    800: SimpelPicture(
                        parent_name="testapp/simplemodel/image.jpg",
                        file_type="WEBP",
                        aspect_ratio=None,
                        storage=default_storage,
                        width=800,
                    ),
                    100: SimpelPicture(
                        parent_name="testapp/simplemodel/image.jpg",
                        file_type="WEBP",
                        aspect_ratio=None,
                        storage=default_storage,
                        width=100,
                    ),
                    200: SimpelPicture(
                        parent_name="testapp/simplemodel/image.jpg",
                        file_type="WEBP",
                        aspect_ratio=None,
                        storage=default_storage,
                        width=200,
                    ),
                    300: SimpelPicture(
                        parent_name="testapp/simplemodel/image.jpg",
                        file_type="WEBP",
                        aspect_ratio=None,
                        storage=default_storage,
                        width=300,
                    ),
                    400: SimpelPicture(
                        parent_name="testapp/simplemodel/image.jpg",
                        file_type="WEBP",
                        aspect_ratio=None,
                        storage=default_storage,
                        width=400,
                    ),
                    500: SimpelPicture(
                        parent_name="testapp/simplemodel/image.jpg",
                        file_type="WEBP",
                        aspect_ratio=None,
                        storage=default_storage,
                        width=500,
                    ),
                    600: SimpelPicture(
                        parent_name="testapp/simplemodel/image.jpg",
                        file_type="WEBP",
                        aspect_ratio=None,
                        storage=default_storage,
                        width=600,
                    ),
                    700: SimpelPicture(
                        parent_name="testapp/simplemodel/image.jpg",
                        file_type="WEBP",
                        aspect_ratio=None,
                        storage=default_storage,
                        width=700,
                    ),
                }
            },
            "3/2": {
                "WEBP": {
                    800: SimpelPicture(
                        parent_name="testapp/simplemodel/image.jpg",
                        file_type="WEBP",
                        aspect_ratio=Fraction(3, 2),
                        storage=default_storage,
                        width=800,
                    ),
                    100: SimpelPicture(
                        parent_name="testapp/simplemodel/image.jpg",
                        file_type="WEBP",
                        aspect_ratio=Fraction(3, 2),
                        storage=default_storage,
                        width=100,
                    ),
                    200: SimpelPicture(
                        parent_name="testapp/simplemodel/image.jpg",
                        file_type="WEBP",
                        aspect_ratio=Fraction(3, 2),
                        storage=default_storage,
                        width=200,
                    ),
                    300: SimpelPicture(
                        parent_name="testapp/simplemodel/image.jpg",
                        file_type="WEBP",
                        aspect_ratio=Fraction(3, 2),
                        storage=default_storage,
                        width=300,
                    ),
                    400: SimpelPicture(
                        parent_name="testapp/simplemodel/image.jpg",
                        file_type="WEBP",
                        aspect_ratio=Fraction(3, 2),
                        storage=default_storage,
                        width=400,
                    ),
                    500: SimpelPicture(
                        parent_name="testapp/simplemodel/image.jpg",
                        file_type="WEBP",
                        aspect_ratio=Fraction(3, 2),
                        storage=default_storage,
                        width=500,
                    ),
                    600: SimpelPicture(
                        parent_name="testapp/simplemodel/image.jpg",
                        file_type="WEBP",
                        aspect_ratio=Fraction(3, 2),
                        storage=default_storage,
                        width=600,
                    ),
                    700: SimpelPicture(
                        parent_name="testapp/simplemodel/image.jpg",
                        file_type="WEBP",
                        aspect_ratio=Fraction(3, 2),
                        storage=default_storage,
                        width=700,
                    ),
                }
            },
            "16/9": {
                "WEBP": {
                    800: SimpelPicture(
                        parent_name="testapp/simplemodel/image.jpg",
                        file_type="WEBP",
                        aspect_ratio=Fraction(16, 9),
                        storage=default_storage,
                        width=800,
                    ),
                    100: SimpelPicture(
                        parent_name="testapp/simplemodel/image.jpg",
                        file_type="WEBP",
                        aspect_ratio=Fraction(16, 9),
                        storage=default_storage,
                        width=100,
                    ),
                    200: SimpelPicture(
                        parent_name="testapp/simplemodel/image.jpg",
                        file_type="WEBP",
                        aspect_ratio=Fraction(16, 9),
                        storage=default_storage,
                        width=200,
                    ),
                    300: SimpelPicture(
                        parent_name="testapp/simplemodel/image.jpg",
                        file_type="WEBP",
                        aspect_ratio=Fraction(16, 9),
                        storage=default_storage,
                        width=300,
                    ),
                    400: SimpelPicture(
                        parent_name="testapp/simplemodel/image.jpg",
                        file_type="WEBP",
                        aspect_ratio=Fraction(16, 9),
                        storage=default_storage,
                        width=400,
                    ),
                    500: SimpelPicture(
                        parent_name="testapp/simplemodel/image.jpg",
                        file_type="WEBP",
                        aspect_ratio=Fraction(16, 9),
                        storage=default_storage,
                        width=500,
                    ),
                    600: SimpelPicture(
                        parent_name="testapp/simplemodel/image.jpg",
                        file_type="WEBP",
                        aspect_ratio=Fraction(16, 9),
                        storage=default_storage,
                        width=600,
                    ),
                    700: SimpelPicture(
                        parent_name="testapp/simplemodel/image.jpg",
                        file_type="WEBP",
                        aspect_ratio=Fraction(16, 9),
                        storage=default_storage,
                        width=700,
                    ),
                }
            },
        }

    def test_check_aspect_ratios(self):
        assert not PictureField()._check_aspect_ratios()
        errors = PictureField(aspect_ratios=["not-a-ratio"])._check_aspect_ratios()
        assert errors
        assert errors[0].id == "fields.E100"

    def test_check_width_height_field(self):
        assert not PictureField(aspect_ratios=["3/2"])._check_width_height_field()
        errors = PictureField(aspect_ratios=[None])._check_width_height_field()
        assert errors
        assert errors[0].id == "fields.E101"

    def test_check(self):
        assert not SimpleModel._meta.get_field("picture").check()
        assert Profile._meta.get_field("picture").check()