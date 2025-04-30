# monitoramento-backup-aws
monitoramento-backup-aws
# Monitoramento de Backups no S3 com AWS Lambda

Seguindo com meus estudos em AWS, criei este projeto para monitorar backups em um bucket S3.

## Como funciona

- Uma função Lambda verifica se há arquivos novos no bucket nas últimas 24 horas.
- Se não encontrar nenhum, envia um alerta por e-mail usando o SNS.

## Tecnologias usadas

- AWS Lambda  
- Amazon S3  
- Amazon SNS  
- Python

## Objetivo

Praticar integração de serviços AWS e criar uma automação simples com um caso de uso real.

---

👩‍💻 *Desenvolvido por Natasha Sales
