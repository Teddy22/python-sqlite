import sqlite3

db = './classic_models.sqlite'  # located in current folder

conn = sqlite3.connect(db) # connect to db

crs = conn.cursor() # create cursor to retrieve data

query = 'PRAGMA TABLE_INFO(%s);' % 'Products'  # query gets columns for the 'Products' table
crs.execute(query)  # execute query
result = crs.fetchall()  # fetch all data records from query
conn.commit()

products_columns = []

for item in result:
    products_columns.append(item[1].__str__())  # add column name to list

products_columns.remove('productDescription')  # remove ProductDescription from columns considered

query = 'SELECT {0} FROM {1}'.format(",".join(products_columns), 'Products')  # new query to get 'Products' table records

crs.execute(query)
result = crs.fetchall()

for field in products_columns:
    print '{:50s}'.format(field),

for row in result:
    print ''
    for item in row:
       print '{:50s}'.format(item.__str__()),

conn.commit()
conn.close()