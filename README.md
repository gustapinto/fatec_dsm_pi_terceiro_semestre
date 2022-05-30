# Anitrends

## Conhecendo o projeto
Uma pĺataforma de análise de dados de visualização de animes, fornecendo métricas e tendências para auxiliar lojistas e consumidores sobre em qual série de produtos (estoque) comprar. Para mais informações sobre o projeto visite:
- [Trello e próximos objetivos](https://trello.com/b/5XD3KYVv/kanban-quadro-modelo)
- [Design e guias de estilo](https://www.figma.com/file/nopgvzIdZ92Kc3PvaqbgIT/PI-3%C2%BA-Semestre?node-id=0%3A1)
- [Projeto e canva](https://www.figma.com/file/O8bvikSwLEkF7w6Aq6K0ai/PM-Canva)
- [Pesquisa e similares](https://www.figma.com/file/jG3r0KMTYdnobYxXMtczww/Pesquisa-de-similares)

## Instalando o projeto

### Consumidor
1. Clone esse repositório com o comando:<br/>
`git clone https://github.com/gustapinto/fatec_dsm_pi_terceiro_semestre.git`
2. Com o projeto clonado abra a pasta `consumidor/` no terminal
3. No terminal crie uma venv com o comando `python -m venv venv` e a ative a venv com os comandos:<br/>
3.1. Linux: `source venv/bin/activate`
4. Com a venv ativa instale os requesitos do projeto com o comando:<br/>`pip install -r requirements.txt`
5. Instale o MongoDB conforme as [instruções oficiais](https://www.mongodb.com/docs/manual/installation/)
6. Pronto! Agora basta executar o consumidor com o comando:<br/>`python main.py <connection string do mongo>`

### Site
1. Clone esse repositório com o comando:<br/>
`git clone https://github.com/gustapinto/fatec_dsm_pi_terceiro_semestre.git`
2. Com o projeto clonado abra a pasta `site/` no terminal
3. No terminal crie uma venv com o comando `python -m venv venv` e a ative a venv com os comandos:<br/>
3.1. Linux: `source venv/bin/activate`
4. Com a venv ativa instale os requesitos do projeto com o comando:<br/>`pip install -r requirements.txt`
5. Rode as *migrations* pendentes com o comando:<br/>
`python manage.py migrate`
6. Inicie o servidor de desenvolvimento Django com o comando:<br/>
`python manage.py runserver`
7. Pronto! Agora basta acessar a url `http://localhost:8000` em seu navegador
