import redis
import requests, random, datetime, json

r = redis.StrictRedis(host='localhost', port=6379, db=1, decode_responses=True)
url = 'https://18.223.102.40/server/client/'
client_id = 1
token = '1hkSOF:wM_maJGAYNuDHHtAS3HaV51vLfo'
headers = {'Accept': 'application/json', 'Content-Type': 'application/json'}

def send_data(timestamp, value):
    data = json.dumps({'id': client_id, 'timestamp': timestamp, 'value': value, 'token': token})
    response = requests.post(url, headers = headers, data = data, verify=False)
    return response

if __name__ == "__main__":
    timestamp = datetime.datetime.now().timestamp()
    value = int(random.random()*100000)
    try:
        response = send_data(timestamp, value)
        if response.status_code != 200:
            r.hmset(client_id, {timestamp: value})
        else:
            if r.exists(client_id):
                unsent_data = r.hkeys(client_id)
                for ts in unsent_data:
                    value = r.hget(client_id, ts)
                    response = send_data(float(ts), int(value))
                    if response.status_code == 200:
                        r.hdel(client_id, ts)
    except:
        r.hmset(client_id, {timestamp: value})

