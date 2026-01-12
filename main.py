import PIL.Image
img = PIL.Image.open("photo_2.jpg")
import PIL.ExifTags
exif= {
    PIL.ExifTags.TAGS[k]: v
    for k, v in img._getexif().items()
    if k in PIL.ExifTags.TAGS}
exif["GPSInfo"]

north = exif ["GPSInfo"][2]
east= exif ["GPSInfo"][4]

lat = north[0] + north[1] / 60 + north[2] / 3600
lon = east[0]+east[1]/60+east[2]/3600
lat,lon = float(lat), float(lon)
print(lat,lon)
