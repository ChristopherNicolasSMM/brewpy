CREATE TABLE IF NOT EXISTS lupulo (
  nome VARCHAR(45)  NOT NULL  ,
  origem VARCHAR(45)    ,
  fabricante VARCHAR(45)    ,
  tipo VARCHAR(45)    ,
  formato VARCHAR(45)    ,
  acido_alfa DECIMAL    ,
  acido_beta DECIMAL    ,
  preco DECIMAL    ,
  observacoes VARCHAR(500)    ,
  mirceno DECIMAL    ,
  humuleno DECIMAL    ,
  cariofileno DECIMAL    ,
  farnesseno DECIMAL    ,
  b_pipeno DECIMAL    ,
  linalol DECIMAL    ,
  geraniol DECIMAL    ,
  outros_oleos DECIMAL    ,
  comp_ox_total DECIMAL      ,
PRIMARY KEY(nome));



CREATE TABLE IF NOT EXISTS malte (
  nome VARCHAR(45)  NOT NULL  ,
  origem VARCHAR(45)    ,
  fabricante VARCHAR(45)    ,
  tipo VARCHAR(45)    ,
  quantidade_max INTEGER    ,
  cor INTEGER    ,
  preco DECIMAL    ,
  extrato_ibu DECIMAL    ,
  potencial_sg DECIMAL    ,
  poder_diastatico DECIMAL    ,
  proteina DECIMAL    ,
  aproveitamento DECIMAL    ,
  usar_mostura BOOL    ,
  usar_fervura BOOL    ,
  nao_fermentavel BOOL    ,
  observacao VARCHAR(500)      ,
PRIMARY KEY(nome));



CREATE TABLE IF NOT EXISTS registro (
  cpf VARCHAR(14)  NOT NULL  ,
  nome VARCHAR(45)    ,
  email VARCHAR(50)    ,
  senha VARCHAR(50)      ,
PRIMARY KEY(cpf));



CREATE TABLE IF NOT EXISTS levedura (
  nome VARCHAR(45)  NOT NULL  ,
  sigla VARCHAR(10)    ,
  laboratorio VARCHAR(45)    ,
  preco DECIMAL    ,
  formato VARCHAR(45)    ,
  floculacao VARCHAR(45)    ,
  viabilidade DECIMAL    ,
  gramas_pacote DECIMAL    ,
  cebulas_bilhoes_unidade DECIMAL    ,
  atenuacao DECIMAL    ,
  temperatura DECIMAL    ,
  familia VARCHAR(45)    ,
  observacoes VARCHAR(500)      ,
PRIMARY KEY(nome));



CREATE TABLE IF NOT EXISTS fermentacao (
  descricao_fermentacao VARCHAR(45)  NOT NULL  ,
  dias INTEGER    ,
  temperatura DECIMAL    ,
  variacao DECIMAL    ,
  etapa VARCHAR(45)      ,
PRIMARY KEY(descricao_fermentacao));



CREATE TABLE IF NOT EXISTS adjunto (
  nome VARCHAR(45)  NOT NULL  ,
  tipo VARCHAR(45)    ,
  fabricante VARCHAR(45)    ,
  max_litro INTEGER    ,
  preco DECIMAL    ,
  indicacao_breve VARCHAR(200)    ,
  observacoes VARCHAR(500)      ,
PRIMARY KEY(nome));



CREATE TABLE IF NOT EXISTS receita (
  nome VARCHAR(45)  NOT NULL  ,
  fermentacao_descricao_fermentacao VARCHAR(45)  NOT NULL  ,
  cervejeiro VARCHAR(45)    ,
  versao INTEGER    ,
  tipo_receita VARCHAR(45)  NOT NULL  ,
  estilo VARCHAR(45)    ,
  data_criacao DATE    ,
  tempo_fervura DECIMAL    ,
  volume_lote DECIMAL    ,
  volume_pre_fervura DECIMAL    ,
  volume_pos_fervura DECIMAL    ,
  real_og DECIMAL    ,
  real_fg DECIMAL    ,
  real_ibu DECIMAL    ,
  real_abv DECIMAL    ,
  real_srm DECIMAL    ,
  anotacoes VARCHAR(500)    ,
  perfil_mostura VARCHAR(45)    ,
  perfil_fermentacao VARCHAR(45)    ,
  total_graos DECIMAL    ,
  total_lupulo DECIMAL    ,
  taxa_amargor DECIMAL      ,
PRIMARY KEY(nome)  ,
  FOREIGN KEY(fermentacao_descricao_fermentacao)
    REFERENCES fermentacao(descricao_fermentacao)
      ON DELETE NO ACTION
      ON UPDATE NO ACTION);


CREATE INDEX IF NOT EXISTS receita_FKIndex1 ON receita (fermentacao_descricao_fermentacao);



CREATE TABLE IF NOT EXISTS itens_receita (
  nome VARCHAR(45)  NOT NULL  ,
  receita_nome VARCHAR(45)  NOT NULL  ,
  ordem INTEGER    ,
  quantidade DECIMAL    ,
  unidade VARCHAR(3)    ,
  tipo VARCHAR(45)    ,
  IBU DECIMAL    ,
  momento VARCHAR(45)      ,
PRIMARY KEY(nome)  ,
  FOREIGN KEY(receita_nome)
    REFERENCES receita(nome)
      ON DELETE NO ACTION
      ON UPDATE NO ACTION);


CREATE INDEX IF NOT EXISTS Insumo_receita_FKIndex1 ON itens_receita (receita_nome);



CREATE TABLE IF NOT EXISTS rampa_mostura (
  id_rampa_mostura INTEGER  NOT NULL  ,
  receita_nome VARCHAR(45)  NOT NULL  ,
  tempo TIMESTAMP    ,
  temperatura INTEGER      ,
PRIMARY KEY(id_rampa_mostura, receita_nome)  ,
  FOREIGN KEY(receita_nome)
    REFERENCES receita(nome)
      ON DELETE NO ACTION
      ON UPDATE NO ACTION);


CREATE INDEX IF NOT EXISTS rampa_mostura_FKIndex1 ON rampa_mostura (receita_nome);




