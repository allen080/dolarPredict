# Previsão da Cotação do Dólar com Rede Neural LSTM
## Autor: Luan Fellipe (allen08)

## Descrição:
### Projeto de construção de uma aplicação de previsão da cotação do dólar usando redes neurais LSTM (Long Short-Term Memory) e Kubernetes. O modelo é alimentado com dados da cotação do dólar (2014 a 2024) e possui uma API (FastAPI) para previsões em tempo real dos valores.

## [*] Bibliotecas para execução
- pip install -r requirements.txt

### [*] Baixar dataset 
- python createDataset.py (atualizar a data do dataset para pegar os valores mais atuais (padrão: 2014 até 06/2024))

### [*] Treinar o modelo 
- python train_model.py

### Rodar a API
- uvicorn app:app --reload

## [*] Implantação do Kubernetes
- docker build -t dollar-prediction-api .
- docker push *repositorio*/dollar-prediction-api (subindo no docker hub)
- kubectl apply -f k8s/deployment.yaml
