import requests
import json
import pandas as pd 
import schedule
import time
import pyodbc
import logging


logger = logging.getLogger()

conn= pyodbc.connect('Driver={ODBC Driver 17 for SQL Server};'
                    'Server=sql-server-db;'
                    'Database=combine;'
                    'UID=sa;' 
                    'PWD=MyPassword123!;'
                    'Encrypt=no;'
                    )

# # Generate random values
# date1 = '2023-04-11'  # Replace with your desired date value
# time1 = '10:30:00'    # Replace with your desired time value
# volume = 1200#random.randint(1, 1000)
# btc_price = 10000#random.uniform(10000, 20000)
# open_interest = 5#random.randint(1, 100)
# mark_price = 568 #random.uniform(1000, 2000)
# instrument_name = 'BTC-Option'  # Replace with your desired instrument name


link='https://www.deribit.com/api/v2/public/get_book_summary_by_currency?currency=BTC&currency=ETH&kind=option'
cursor=conn.cursor()
print(cursor)
# cursor.execute("INSERT INTO Combine.dbo.Options_API ([date1],[time1], [volume],[btc_price],[open_interest],[mark_price],[instrument_name]) values(?,?,?,?,?,?,?)", date1, time1, volume, btc_price, open_interest, mark_price, instrument_name)

# # Commit the changes to the database
# conn.commit()

# # Print a confirmation message
# print("Data inserted successfully!")


def write_to_excel():
    response_API=requests.get(link)
    data=response_API.text
    parse_json= json.loads(data)
    #print(parse_json)
    currency=parse_json['result']
    #print(currency)
    # logger.info(f"Currency Value: {currency}")
    #print("currency = ", currency)
    multiple_level_data=pd.json_normalize(parse_json,record_path=['result'])
    multiple_level_data['date1']=pd.to_datetime(multiple_level_data['creation_timestamp'],unit='ms').dt.date
    multiple_level_data['time1']=pd.to_datetime(multiple_level_data['creation_timestamp'],unit='ms').dt.time
    #multiple_level_data['time1']+=pd.Timedelta(hours=5)

    print(multiple_level_data)
    for index, row in multiple_level_data.iterrows():
        cursor.execute("INSERT INTO Combine.dbo.Options_API ([date1],[time1], [volume],[btc_price],[open_interest],[mark_price],[instrument_name]) values(?,?,?,?,?,?,?)", row.date1, row.time1, row.volume, row.underlying_price, row.open_interest, row.mark_price, row.instrument_name)
#         #logger.info(f"Index:  {index}, Row: {row}")   
#         #print('index:', {index}, 'Row:', {row})
        conn.commit() 
# schedule.every(1).minutes.do(write_to_excel)
# print(schedule.run_pending())
#time.sleep(1)

# def send_data_to_mssql():
#     while True:
#         schedule.run_pending()
#         time.sleep(1)

# if __name__ == "__main__":
#     write_to_excel()
#     send_data_to_mssql()
#     logging.basicConfig(level=logging.DEBUG)

if __name__ == "__main__":
    logging.basicConfig(level=logging.DEBUG)
    schedule.every(1).minutes.do(write_to_excel)
    while True:
        schedule.run_pending()
        time.sleep(1)
