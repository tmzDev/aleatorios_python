import sqlite3

coman = sqlite3.connect('cadastro.db')
c = coman.cursor()

c.execute('CREATE TABLE IF NOT EXISTS produto(nome text, preco integer, cat text)')


#c.execute(f'INSERT INTO produto VALUES ("caderno", 30, "papelaria")')
#c.execute(f'INSERT INTO produto VALUES ("mesa", 500, "moveis")')
#c.execute('INSERT INTO produto VALUES ("lapis", 2, "papelaria")')

coman.commit()

requi = 'SELECT * FROM produto'
for i in c.execute(requi):
    print(f'-- {i}')
    

