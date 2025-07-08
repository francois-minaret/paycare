import boto3

# Initialisation du client S3
s3_client = boto3.client("s3")

# Définition des paramètres
# file_name = "unit-tests.xml"  # Nom du fichier XML généré par pytest
file_name = "results.xml"
bucket_name = "s3://s3lead-fmi/MLOPS"
s3_key = "unit-tests.xml"  # Chemin dans le bucket

# Upload du fichier
try:
    s3_client.upload_file(file_name, bucket_name, s3_key)
    print(
        f"✅ Fichier '{file_name}' envoyé avec succès sur 's3://s3lead-fmi/MLOPS/test-results/{s3_key}'"
    )
except Exception as e:
    print(f"❌ Erreur lors de l'upload sur S3 : {e}")
