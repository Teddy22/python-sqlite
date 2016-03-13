import sys
import sqlite3

if len(sys.argv) > 1:
    print 'Product Line:', ' '.join(sys.argv[1:])

    product_line = ' '.join(sys.argv[1:])

    db = './classic_models.sqlite'  # located in current folder
    conn = sqlite3.connect(db) # connect to db
    crs = conn.cursor() # create cursor to retrieve data

    table_name = 'Products'

    ###### get tabe columns #######
    query = 'PRAGMA TABLE_INFO(%s);' % 'Products'  # query gets columns for the 'Products' table
    crs.execute(query)  # execute query
    result = crs.fetchall()  # fetch all data records from query
    conn.commit()

    products_columns = []

    for item in result:
        products_columns.append(item[1].__str__())  # add column name to list

    products_columns.remove('productDescription')  # remove ProductDescription from columns considered
    products_columns.remove('productLine')  # remove ProductLine from columns considered

    ######  get data  #######
    query = 'SELECT %s FROM %s WHERE ProductLine = \'%s\'' % (",".join(products_columns), table_name, product_line)  # query filters by ProductLine

    crs.execute(query)  # execute query
    result = crs.fetchall()  # fetch all data records from query
    conn.commit()

    for field in products_columns:
        print '{:50s}'.format(field),

    for row in result:
        print ''
        for item in row:
            print '{:50s}'.format(item.__str__()),

    conn.commit()
    conn.close()