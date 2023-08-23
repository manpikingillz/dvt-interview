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
