import os
import wget
import zipfile

# Download the zipped dataset
url = 'https://storage.googleapis.com/trainingdata-mlops/data.zip'
zip_name = "data.zip"
wget.download(url, zip_name)


import os
#out_image = 'out_005.png'
#url = 'http://mangadoom.co/wp-content/manga/5170/886/005.png'
os.system("wget -O {0} {1}".format(zip_name, url))


# Unzip it and standardize the .csv filename
with zipfile.ZipFile(zip_name, "r") as zip_ref:
	zip_ref.extractall()

os.remove(zip_name)
print('\nAll files are being extracted.')