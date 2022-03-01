            CREATE TABLE IF NOT EXISTS lupulo (
              id_lupulo INTEGER  NOT NULL  ,
              nome VARCHAR(45)    ,
              origem VARCHAR(45)    ,
              fabricante VARCHAR(45)    ,
              tipo VARCHAR(45)    ,
              formato VARCHAR(45)    ,
              acido_alfa DECIMAL    ,
              acido_beta DECIMAL    ,
              preco DECIMAL    ,
              observacoes VARCHAR(500)      ,
            PRIMARY KEY(id_lupulo));
            
            
            
            CREATE TABLE IF NOT EXISTS levedura (
              id_levedura INTEGER  NOT NULL  ,
              nome VARCHAR(45)    ,
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
            PRIMARY KEY(id_levedura));
            
            
            
            CREATE TABLE IF NOT EXISTS malte (
              id_malte INTEGER  NOT NULL  ,
              nome VARCHAR(45)    ,
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
              observacoes VARCHAR(500)    ,
              usar_mostura BOOL    ,
              usar_fervura BOOL    ,
              nao_fermentavel BOOL    ,
              aproveitamento INTEGER      ,
            PRIMARY KEY(id_malte));
            
            
            
            CREATE TABLE IF NOT EXISTS receita (
              id_receita INTEGER  NOT NULL  ,
              nome VARCHAR(45)      ,
            PRIMARY KEY(id_receita));
            
            
            
            CREATE TABLE IF NOT EXISTS adjunto (
              id_adjunto INTEGER  NOT NULL  ,
              nome VARCHAR(45)    ,
              tipo VARCHAR(45)    ,
              fabricante VARCHAR(45)    ,
              max_litro INTEGER    ,
              preco DECIMAL    ,
              indicacao_breve VARCHAR(200)    ,
              observacoes VARCHAR(500)      ,
            PRIMARY KEY(id_adjunto));
            
            
            
            CREATE TABLE IF NOT EXISTS rampa_mostura (
              id_rampa_mostura INTEGER  NOT NULL  ,
              receita_id_receita INTEGER  NOT NULL  ,
              tempo TIMESTAMP    ,
              temperatura INTEGER      ,
            PRIMARY KEY(id_rampa_mostura, receita_id_receita)  ,
              FOREIGN KEY(receita_id_receita)
                REFERENCES receita(id_receita)
                  ON DELETE NO ACTION
                  ON UPDATE NO ACTION);
            
            
			
			
            CREATE INDEX IF NOT EXISTS rampa_mostura_FKIndex1 ON rampa_mostura (receita_id_receita);
            
            
            
            CREATE TABLE IF NOT EXISTS fermentacao (
              id_fermentacao INTEGER  NOT NULL  ,
              receita_id_receita INTEGER  NOT NULL  ,
              dias INTEGER    ,
              temperatura DECIMAL    ,
              variacao DECIMAL    ,
              etapa VARCHAR(45)      ,
            PRIMARY KEY(id_fermentacao, receita_id_receita)  ,
              FOREIGN KEY(receita_id_receita)
                REFERENCES receita(id_receita)
                  ON DELETE NO ACTION
                  ON UPDATE NO ACTION);
            
            
            CREATE INDEX IF NOT EXISTS fermentacao_FKIndex1 ON fermentacao (receita_id_receita);
            
            
            
            CREATE TABLE IF NOT EXISTS malte_has_receita (
              malte_id_malte INTEGER  NOT NULL  ,
              receita_id_receita INTEGER  NOT NULL    ,
            PRIMARY KEY(malte_id_malte, receita_id_receita)    ,
              FOREIGN KEY(malte_id_malte)
                REFERENCES malte(id_malte)
                  ON DELETE NO ACTION
                  ON UPDATE NO ACTION,
              FOREIGN KEY(receita_id_receita)
                REFERENCES receita(id_receita)
                  ON DELETE NO ACTION
                  ON UPDATE NO ACTION);
            
            
            CREATE INDEX IF NOT EXISTS malte_has_receita_FKIndex1 ON malte_has_receita (malte_id_malte);
            CREATE INDEX IF NOT EXISTS malte_has_receita_FKIndex2 ON malte_has_receita (receita_id_receita);
            
            
            
            CREATE TABLE IF NOT EXISTS adicao_lupulo (
              id_adicao_lupulo INTEGER  NOT NULL  ,
              lupulo_id_lupulo INTEGER  NOT NULL  ,
              receita_id_receita INTEGER  NOT NULL  ,
              tempo INTEGER    ,
              quantidade INTEGER    ,
              momento VARCHAR(45)    ,
              dias INTEGER      ,
            PRIMARY KEY(id_adicao_lupulo, lupulo_id_lupulo, receita_id_receita)    ,
              FOREIGN KEY(lupulo_id_lupulo)
                REFERENCES lupulo(id_lupulo)
                  ON DELETE NO ACTION
                  ON UPDATE NO ACTION,
              FOREIGN KEY(receita_id_receita)
                REFERENCES receita(id_receita)
                  ON DELETE NO ACTION
                  ON UPDATE NO ACTION);
            
            
            CREATE INDEX IF NOT EXISTS adicao_lupulo_FKIndex1 ON adicao_lupulo (lupulo_id_lupulo);
            CREATE INDEX IF NOT EXISTS adicao_lupulo_FKIndex2 ON adicao_lupulo (receita_id_receita);
            
            
            
            CREATE TABLE IF NOT EXISTS adjunto_has_receita (
              adjunto_id_adjunto INTEGER  NOT NULL  ,
              receita_id_receita INTEGER  NOT NULL    ,
            PRIMARY KEY(adjunto_id_adjunto, receita_id_receita)    ,
              FOREIGN KEY(adjunto_id_adjunto)
                REFERENCES adjunto(id_adjunto)
                  ON DELETE NO ACTION
                  ON UPDATE NO ACTION,
              FOREIGN KEY(receita_id_receita)
                REFERENCES receita(id_receita)
                  ON DELETE NO ACTION
                  ON UPDATE NO ACTION);
            
            
            CREATE INDEX IF NOT EXISTS adjunto_has_receita_FKIndex1 ON adjunto_has_receita (adjunto_id_adjunto);
            CREATE INDEX IF NOT EXISTS adjunto_has_receita_FKIndex2 ON adjunto_has_receita (receita_id_receita);
            
            
            
            CREATE TABLE IF NOT EXISTS levedura_has_receita (
              levedura_id_levedura INTEGER  NOT NULL  ,
              receita_id_receita INTEGER  NOT NULL    ,
            PRIMARY KEY(levedura_id_levedura, receita_id_receita)    ,
              FOREIGN KEY(levedura_id_levedura)
                REFERENCES levedura(id_levedura)
                  ON DELETE NO ACTION
                  ON UPDATE NO ACTION,
              FOREIGN KEY(receita_id_receita)
                REFERENCES receita(id_receita)
                  ON DELETE NO ACTION
                  ON UPDATE NO ACTION);
            
            
            CREATE INDEX IF NOT EXISTS levedura_has_receita_FKIndex1 ON levedura_has_receita (levedura_id_levedura);
            CREATE INDEX IF NOT EXISTS levedura_has_receita_FKIndex2 ON levedura_has_receita (receita_id_receita);


