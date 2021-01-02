# api_forecast_advisor

# Para rodar a aplicação:

# Usando docker:

- No diretório forecast_advisor_app rodar o seguinte comando:

   $sudo bash start.sh

- A api ficará disponível para consumo através da porta 5000.

- Esse arquivo contém as rotinas para criar o container da aplicação e iniciar a mesma nesse container.

# Sem usar docker:

- Instale as dependências encontradas em requirements.txt

- No diretório forecast_advisor_app rodar o comando:

   $python main.py
   
- A api ficará disponível para consumo através da porta 5000.

# Consumo da api:

- http://localhost:5000/city?id=<ID_DA_CIDADE>

- Para buscar as condições climáticas de uma determinada cidade, enviar uma requisição com método GET
com o parâmetro id na url, seguindo o seguinte padrão:

http://localhost:5000/city?id=<ID_DA_CIDADE>

Exemplo:

Ao acessar:

http://localhost:5000/city?id=3477

São buscadas condições climáticas para a cidade de São Paulo e armazenadas no banco de dados.

A requisição à api apenas é executada caso não seja encontrado no banco de dados os dados climáticos
para o id requisitado na mesma data da requisição (data e id formam a chave primária no banco de dados).

Além disso, a api devolve um json como resultado.

A resposta está no formato json com o seguinte padrão:

{"country":	"BR  ",
"date":	"2021-01-02",
"id":	3477,
"maxtemp":	24,
"mintemp":	17,
"name":	"São Paulo",
"precipitation": 8,
"probability": 90,
"state": "SP"}

Uma lista com todos os ids válidos de cidade pode ser encontrada no arquivo forecast_advisor_app/app/api_tests/registered_ids.json

Caso seja passada uma url com um id inválido ou sem o parâmetro de id, o objeto será devolvido com o mesmo formato, porém com
o valor nulo para suas entradas.

# Para fazer análise das cidades consultadas

- http://localhost:5000/analysis?initial_date=<DATA_INICIAL>&final_date=<DATA_FINAL>

- A api irá devolver um objeto com o seguinte formato:

{'city': <CIDADE_MAIS_QUENTE>, 'average_precipitation': '<PRECIPITAÇÃO_MÉDIA_PARA_AS_CIDADES_NO_PERÍODO_CONSULTADO>'}

Caso não haja cidades nesse intervalo, ou haja um erro com a requisição, será devolvido o mesmo objeto com "None" nas entradas.

# Testes:

No diretório forecast_advisor_app, execute o seguinte comando:

- 1 - A rotina get_city_info_from_response é responsável por retirar somente as informações relevantes da resposta da api.
 esse teste verifica se as informações retiradas estão corretas.

   python -m unittest app/unitary_tests/test_get_city_info_from_response.py

- 2 - A rotina convert_from_date_string é responsável por convertar um string no formato aaaa-mm-dd (yyyy-mm-dd) em um
objeto do tipo date. Esse teste verifica se o resultado obtido com a conversão é o esperado.

   python -m unittest app/unitary_tests/convert_from_date_string.py

# Para realizar os testes abaixo, a api deve estar rodando na porta 5000.

- 3 - As respostas da api a uma requisição devem poder ser convertidas para o formato json. A rotina test_city,
verifica se, para uma cidade aleatória, a requisição pode ser convertida para o formato json.

   python -m unittest app/api_tests/test_city.py

- 4 - Verifica se a api vai devolver uma resposta serializável caso parâmetros de busca não sejam passados
para a rota analysis.

   python -m unittest app/api_tests/test_no_analysis_param.py

- 5 - Verifica se a api vai devolver uma resposta serializável caso o id seja um inteiro, porém a api não
tenha registros para a id passada.

   python -m unittest app/api_tests/test_no_id_city.py


Obs: a api do apiadvisor estava respondendo devolvendo apenas a previsão do tempo durante os próximos 7 dias,
e não 15 dias para a requisição ao endpoint:

http://apiadvisor.climatempo.com.br/api/v1/forecast/locale/<ID_DA_CIDADE>/days/15?token=<TOKEN>
