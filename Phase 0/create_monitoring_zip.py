import os
import zipfile

# Paths
base_path = r"C:\Users\hp\Raasystem\RaasMatrix\ai\monitoring"
zip_path = r"C:\Users\hp\Raasystem\RaasMatrix\monitoring_package_final.zip"

# Create ZIP file
with zipfile.ZipFile(zip_path, 'w', zipfile.ZIP_DEFLATED) as zipf:
    for root, dirs, files in os.walk(base_path):
        for file in files:
            file_path = os.path.join(root, file)
            # preserve folder structure relative to monitoring folder
            arcname = os.path.relpath(file_path, base_path)
            zipf.write(file_path, arcname)

zip_path
