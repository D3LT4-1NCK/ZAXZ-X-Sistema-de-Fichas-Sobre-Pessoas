-- SQL não roda se ter comentários na mesma linha que um comando.

-- Marco o modo para .csv (vai tentar ler no formato .csv, se houver erro na leitura, no caso, sair do esperado, ele vai lançar erro).
-- Por isso não enfie um json onde deve ser um csv.
.mode csv

-- Se a tabela já existe, apago ela, questão de segurança para evitar erros do próprio SQL (que é meio mal feito).
DROP TABLE IF EXISTS tabela;

-- Crio a tabela e importo ela.
.import infos.csv tabela

-- Deve ser colocado após o .import para que ele não "resete" as informações.
-- Imprime a tabela de forma organizada.
.mode box
-- Imprime títulos.
.headers on

-- Seleciono tudo da tabela, e por padrão, ele já imprime diretamente.
SELECT * FROM tabela;
