import boto3
import datetime
import os

# Inicializando os clientes da AWS
s3 = boto3.client('s3')
sns = boto3.client('sns')

# Configurações
BUCKET_NAME = 'meu-backup-monitorado'  
TOPIC_ARN = 'arn:aws:sns:us-east-1:539247476767:alerta-backup' 
HORAS = 24  

def lambda_handler(event, context):
    # Obtém o tempo atual e calcula o limite de 24 horas
    agora = datetime.datetime.utcnow()
    limite = agora - datetime.timedelta(hours=HORAS)

    # Listar objetos no S3
    arquivos_novos = s3.list_objects_v2(Bucket=BUCKET_NAME)

    if 'Contents' not in arquivos_novos:
        enviar_alerta()
        return

    # Filtra os arquivos que foram modificados nas últimas 24 horas
    arquivos_recentes = [
        obj for obj in arquivos_novos['Contents']
        if obj['LastModified'].replace(tzinfo=None) > limite
    ]

    if not arquivos_recentes:
        enviar_alerta()
    else:
        print(f"{len(arquivos_recentes)} arquivos encontrados nas últimas {HORAS}h.")

def enviar_alerta():
    # Envia um alerta SNS
    sns.publish(
        TopicArn=TOPIC_ARN,
        Subject='[ALERTA] Backup não detectado',
        Message=f'Nenhum arquivo novo foi encontrado no bucket {BUCKET_NAME} nas últimas {HORAS} horas.'
    )
