from flask import Flask, request, redirect 
from redis import Redis
from appCass import save, load
from appRedis import cache, update

# Connect to Redis
redis = Redis(host="redis", db=0, socket_connect_timeout=2, socket_timeout=2)
app = Flask(__name__)
NOT_FOUND = "<h1>Not Found</h1>"
BAD_REQUEST = "<h1>Bad Request</h1>"
GOOD_REQUEST = "<h1>Got It!</h1>"


@app.route("/", methods=['GET'])
def health():
	return "Healthy", 200

app.route("/<short>", methods=['GET'])
def get(short):
    # Retrieve from cache
    long = cache(short)
    if long == NOT_FOUND:
        print(f"Retrieved from Redis: {long}")
        return NOT_FOUND, 404
    elif long:
        print(f"Retrieved from Redis: {long}")
        return redirect(long, code=307)

    # Retrieve from database
    long = load(short)
    if long is None:
        update(short, NOT_FOUND)
        return NOT_FOUND, 404
    update(short, long)
    return redirect(long, code=307)

@app.route("/", methods=['PUT'])
def put():
    short = request.args.get('short')
    long = request.args.get('long')
    if short is None or long is None:
        return BAD_REQUEST, 400

    save(short, long)
    response = cache(short)
    if response:
        print("Updating Redis")
        update(short, long)
    return GOOD_REQUEST, 201

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=80)

