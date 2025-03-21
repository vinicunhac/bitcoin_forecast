import json
import requests
import boto3
from botocore.exceptions import NoCredentialsError

def lambda_handler(event, context):
    # URL da API que você deseja consumir
    api_url = "https://fastapi-embrapa-73b6grsrr-vinicius-projects-3b0d12e4.vercel.app"
    
    # Fazendo a requisição para a API
    response = requests.get(api_url)
    
    if response.status_code == 200:
        data = response.json()
        
        # Nome do bucket no S3 e do arquivo
        s3_bucket = "btc-data-bronze"
        s3_key = "dados/dados.json"
        
        s3 = boto3.client('s3')
        
        try:
            # Convertendo o conteúdo para JSON e enviando para o S3
            s3.put_object(Bucket=s3_bucket, Key=s3_key, Body=json.dumps(data))
            return {
                'statusCode': 200,
                'body': json.dumps('Dados salvos com sucesso no S3!')
            }
        except NoCredentialsError:
            return {
                'statusCode': 403,
                'body': json.dumps('Credenciais AWS não configuradas!')
            }
            
    else:
        return {
            'statusCode': response.status_code,
            'body': json.dumps('Erro ao consumir API!')
        }