# FoccoERP Quotations Report XML Reader

Este é um leitor rápido e simples para o relatório de cotações do FoccoERP em XML.

<img src="https://raw.githubusercontent.com/rtalis/foccoerp_report_reader/main/templates/image.png" width="600" title="ilustração">
## Como usar

1. Clone este repositório para sua máquina local usando `git clone`.
2. Navegue até a pasta do projeto.
3. Install the required dependencies by running `pip install -r requirements.txt`.
3. Execute `python main.py` para iniciar o servidor Flask.
4. Abra um navegador e vá para `http://localhost:5000` para ver a interface do usuário.
5. Coloque o arquivo XML gerado a partir do relatorio de cotações do foccoERP na pasta uploads
~~5. Carregue seu arquivo XML usando o botão de upload.~~
6. Insira o valor de busca e selecione o tipo de busca.
7. Clique em 'Buscar' para ver os resultados.

## Funcionalidades

- Carrega arquivos XML do relatório de cotações do FoccoERP.
- Permite ao usuário buscar por um valor específico no arquivo XML.
- Exibe os resultados da busca para o usuário.

## Dependências

- Flask
- Werkzeug
- xml.etree.ElementTree
- os
- datetime

## Contribuições

Contribuições são sempre bem-vindas. Sinta-se à vontade para abrir uma issue ou enviar um pull request.

## Licença

Este projeto está licenciado sob a licença MIT. Veja o arquivo `LICENSE` para mais detalhes.
