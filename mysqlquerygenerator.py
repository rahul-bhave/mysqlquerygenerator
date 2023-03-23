import argparse

def generate_query(keyword, tables, criteria, group_by, order_by):
    # Determine the SQL query based on the given keyword
    if keyword == 'select':
        join_str = ''
        if len(tables) > 1:
            join_str = ' JOIN '.join(tables[:-1]) + ' ON ' + tables[-1]
        where_str = f'WHERE {criteria}' if criteria else ''
        group_by_str = f'GROUP BY {group_by}' if group_by else ''
        order_by_str = f'ORDER BY {order_by}' if order_by else ''
        query = f"SELECT * FROM { tables[0] }{join_str} {where_str} {group_by_str} {order_by_str};"
    elif keyword == 'insert':
        query = f"INSERT INTO {tables[0]} VALUES ({criteria});"
    else:
        query = f"SELECT * FROM {tables[0]} JOIN {tables[1]} USING ({criteria});"
    
    return query

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Generate SQL queries based on user inputs')
    parser.add_argument('keyword', choices=['select', 'insert', 'join'], help='The type of SQL query to generate')
    parser.add_argument('--tables', nargs=5, required=True, help='The names of the tables to query')
    parser.add_argument('--criteria', help='The join criteria for the query')
    parser.add_argument('--group-by', help='The column(s) to group the results by')
    parser.add_argument('--order-by', help='The column(s) to order the results by')
    args = parser.parse_args()

    query = generate_query(args.keyword, args.tables, args.criteria or '', args.group_by or '', args.order_by or '')
    print(query)