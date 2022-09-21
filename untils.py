from db import execute_query


def filterByCityAndState(city: str, state: str):
    query_sql = '''
    SELECT CustomerId,FirstName,LastName,City,State from customers
    '''

    if city and state:
        query_sql += f" WHERE City = '{city}' AND State = '{state}';"
    elif city:
        query_sql += f" WHERE City = '{city}';"
    elif state:
        query_sql += f" WHERE State = '{state}';"
    return execute_query(query_sql, False)


def nameCounts():
    query_sql = '''
    SELECT FirstName, count(FirstName) as Count from customers GROUP BY FirstName;
    '''
    return execute_query(query_sql, False)


def ordersSum():
    query_sql = '''
    SELECT sum (UnitPrice * Quantity) as sum from invoice_items;
    '''
    return execute_query(query_sql, True)
