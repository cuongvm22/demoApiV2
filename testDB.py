import psycopg2
# url = 'postgres://bllhxwinnrtatp:36d150bf8b14c95e7f1c0aae43a43e3d9234f37424fef3fa7639d2746fcb2630@ec2-34-230-231-71.compute-1.amazonaws.com:5432/d46ukn7g8c5ns7'
url = 'postgres://mectmbkibsfmhe:96e6298e4c0c7de2c7b003824b16a58bc1b184991d07c0e1e8287cd14ef5225c@ec2-107-22-216-123.compute-1.amazonaws.com:5432/dd2pjqmbdvg5fh'
conn = psycopg2.connect(url, sslmode = 'require')
cur = conn.cursor()
cur.execute('select * from information_schema.tables')
print(cur.fetchone())