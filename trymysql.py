import pymysql as msq
db = msq.connect("tsan-vmjo","tsan","2333","employees")
csr = db.cursor();
csr.execute("select * from titles;")
print(csr.fetchone())
db.commit()
db.close()