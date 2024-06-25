# API-banco-de-dados
Sistema de banco de dados e consolidação.

Recepção de Dados:

  - banco1: Recebe dados do Banco 1 e os armazena na lista dados_base.
  - banco2: Recebe dados do Banco 2 e os armazena na lista dados_cliente.
  - banco3: Recebe dados do Banco 3 e os armazena na lista regras_negocio.

🛠️ Consolidação e Aplicação de Regras:

  - Consolidar: Consolida todos os dados recebidos em um único dicionário JSON.

Aqui é onde a mágica acontece: os dados de dados_base, dados_cliente e regras_negocio são combinados para análise e processamento adicional.

📤 Envio de Arquivos CSV:

  - enviar_arquivo: Esta rota verifica a existência de um arquivo CSV local (arquivo_lote.csv) e o envia para um servidor especificado. Utilizamos a biblioteca requests para realizar essa transferência, assegurando que os dados sejam enviados de forma segura e eficiente.

Este projeto demonstra como é possível utilizar Flask para construir uma API robusta para integração e processamento de dados, destacando o poder da linguagem Python na automação e manipulação de grandes volumes de informações.

🌟 Tecnologias Utilizadas:

  - Flask para construção das rotas e manipulação de requisições.
  - Requests para envio de arquivos HTTP.
  - JSON para fácil manipulação e consolidação de dados.

Com a integração e automação dos dados, empresas podem tomar decisões mais informadas e rápidas, garantindo uma operação mais eficiente e dados mais precisos. 🚀💡
