import os
from PROJETO import server

if __name__ == '__main__':
    port = int(os.getenv("PORT"))
    server.run(host='0.0.0.0', port=port)
