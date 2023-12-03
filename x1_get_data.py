import os
import wget
import zipfile
import gdown

# Download the zipped dataset 
# Remplacez 'your_file_id' par l'ID du fichier Google Drive que vous souhaitez télécharger
file_id = '1Mw4RsXcSd54oojfsR7aAFF5Kdiyf04Tt'

# Obtenez le lien de téléchargement direct à partir de l'ID du fichier
url = f'https://drive.google.com/uc?id={file_id}'
zip_name = "data.zip"
 
 
# Téléchargez le fichier en utilisant gdown
gdown.download(url, zip_name, quiet=False)


# Unzip it and standardize the .csv filename
with zipfile.ZipFile(zip_name, "r") as zip_ref:
	zip_ref.extractall()

os.remove(zip_name)
print('\nAll files are being extracted.') 

