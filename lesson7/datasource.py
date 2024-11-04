import requests
import sqlite3


def get_sitename() -> list[str]:
    conn = sqlite3.connect("AQI.db")
    with conn:
        cursor = conn.cursor()
        sql = '''
        SELECT DISTINCT sitename
        FROM records
        '''
        cursor.execute(sql)
        sitenames = [items[0] for items in cursor.fetchall()]

    return sitenames


def get_selected_data(sitename: str) -> list[list]:
    url = 'https://data.moenv.gov.tw/api/v2/aqx_p_488?api_key=e8dd42e6-9b8b-43f8-991e-b3dee723a52d&limit=1000&sort=datacreationdate%20desc&format=JSON'
    try:
        response = requests.get(url)
        response.raise_for_status()
        data = response.json()
    except Exception as e:
        print(e)
    else:
        outerlist = []
        for items in data['records']:
            if items['sitename'] == sitename:
                innerlist = [items['datacreationdate'], items['county'], items['aqi'],
                             items['pm2.5'], items['status'], items['latitude'], items['longitude']]
                outerlist.append(innerlist)

        return outerlist


def download_data():
    conn = sqlite3.connect("AQI.db")
    url = 'https://data.moenv.gov.tw/api/v2/aqx_p_488?api_key=e8dd42e6-9b8b-43f8-991e-b3dee723a52d&limit=1000&sort=datacreationdate%20desc&format=JSON'
    try:
        response = requests.get(url)
        response.raise_for_status()
        data = response.json()
    except Exception as e:
        print(e)
    else:
        sitenames = set()
        with conn:
            cursor = conn.cursor()
            for items in data['records']:
                sitename = items['sitename']
                county = items['county']
                aqi = int(items['aqi']) if items['aqi'] != '' else 0
                status = items['status']
                pm25 = float(items['pm2.5']) if items['pm2.5'] != '' else 0.0
                date = items['datacreationdate']
                lon = float(items['longitude']
                            ) if items['longitude'] != '' else 0.0
                lat = float(items['latitude']
                            ) if items['latitude'] != '' else 0.0
                sql = '''INSERT OR IGNORE INTO records(sitename,county,aqi,status,pm25,date,lat,lon)
                        values (?,?, ?, ?,?,?,?,?);
                '''
                cursor.execute(sql, (sitename, county, aqi, status,pm25,date,lat,lon))