import csv
import os

import PIL
from autocrop import Cropper
from django.conf import settings
from PIL import Image

from utils.get_env_value import get_env_value


def create_csv_if_not_exists(csv_path):
  if not os.path.exists(csv_path):
    with open(csv_path, "w", newline="") as csvfile:
      csv_writer = csv.writer(csvfile)
      # Add headers or any initial data if needed
      csv_writer.writerow(["Cropped Image Path", "Non-Cropped Image Path"])


def is_image_path_present(csv_filename, image_path):
  try:
    with open(csv_filename, "r", newline="") as csvfile:
      csv_reader = csv.reader(csvfile)
      for row in csv_reader:
        if row and row[0] == image_path:
          return True
    return False
  except:
    return False


def cropManually(input_path):
  img = Image.open(input_path)
  img_width, img_height = img.size
  crop_size = min(img_width, img_height)
  left = (img_width - crop_size) // 2
  top = (img_height - crop_size) // 2
  right = left + crop_size
  bottom = top + crop_size
  return img.crop((left, top, right, bottom))


def cropImage(input_path, destination_path):
  if not os.path.exists(input_path):
    raise FileNotFoundError("Image file does not exist.")
  try:
    length = get_env_value("PROFILE_IMAGE_RESOLUTION")
    cropper = Cropper(face_percent=50, height=length, width=length)
    cropped_array = cropper.crop(input_path)
  except:
    cropper = Cropper()
    cropped_array = cropper.crop(input_path)

  original_image = Image.open(input_path)

  original_filename = os.path.basename(input_path)
  os.makedirs(destination_path, exist_ok=True)
  print(os.path.join(destination_path, original_filename))
  original_image.save(os.path.join(destination_path, original_filename))

  if cropped_array is not None and cropped_array.any():
    cropped_image = Image.fromarray(cropped_array)
    cropped_image.save(input_path)
  else:
    cropped_image = cropManually(input_path)
    cropped_image.save(input_path)
    raise Exception("can't crop this image")


def deleteProfileImage(image_path):
  # remove cropped image
  if os.path.exists(image_path):
    os.remove(image_path)

  # remove non-cropped image
  destination_path = settings.ORIGINAL_PROFILE_PICTURES_FOLDER
  non_cropped_image_path = os.path.join(
      destination_path, os.path.basename(image_path))
  if (os.path.exists(non_cropped_image_path)):
    os.remove(non_cropped_image_path)
