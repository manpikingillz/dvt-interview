'''
Returns all stocks
 - /api/stocks
 - /api/stocks/?page=pageNumber

Returns results matching exact search key
 - /api/stocks/?key=value
 - /api/stocks/?key=value&page=pageNumber

 Returns results where search key contains value as substring
 - /api/stocks/search?key=value
 - /api/stocks/search?key=value&page=pageNumber

 Response: JSON
 Example response
 {
     page: 1
     per_page: 10
     total: 100
     data: [
         {
            "date": "5-January-2000",
            "open": 5265.09,
            "high": 5464.35,
            "low": 5184.48,
            "close": 5357.0
        },
        {
            "date": "6-January-2000",
            "open": 5424.21,
            "high": 5489.86,
            "low": 5391.33,
            "close": 5421.53
        },
     ]
 }

Sample Input:
    1-January-2000
    11-January-2000

Sample Output:
    5-January-2000 5265.09 5357.0
    6-January-2000 5424.21 5421.53
    7-January-2000 5358.28 5414.48
    11-January-2000 5513.04 5296.3
'''
import datetime
import requests


def openAndClosePrices(firstDate, lastDate):
    first_date = datetime.datetime.strptime(firstDate, '%d-%B-%Y')
    last_date = datetime.datetime.strptime(lastDate, '%d-%B-%Y')

    current_date = first_date

    while current_date <= last_date:
        date = current_date.strftime('%d-%B-%Y')
        response = requests.get(
            f'https://jsonmock.hackerrank.com/api/stocks?date={date}')
        current_date += datetime.timedelta(days=1)

        if response.status_code == 200:
            data = response.json()

            for item in data['data']:
                items = [item['date'], str(item['open']), str(item['close'])]
                print('   '.join(items))
        else:
            print("Error Occured: ", response.status_code)


if __name__ == "__main__":
    first_date = "8-March-2002"
    last_date = "15-March-2002"

    openAndClosePrices(first_date, last_date)
