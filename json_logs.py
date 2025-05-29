import logging
import json
from flask import Flask, request

# JSON FORMATTER CONFIG
class JSONFormatter(logging.Formatter):
    def format(self, record):
        log_entry = {
            "timestamp": self.formatTime(record),
            "level": record.levelname,
            "message": record.getMessage(),
            "client_ip": request.remote_addr if request else "unknown",
            "endpoint": request.path if request else "unknown",
            "status_code": getattr(record, "status_code", "unknown")
        }
        return json.dumps(log_entry)

app = Flask(__name__)

log_file = "json.log"
file_handler = logging.FileHandler(log_file)
file_handler.setFormatter(JSONFormatter()) # SETTING JSON FORMATTER

app.logger.addHandler(file_handler)  # Logs to file
app.logger.setLevel(logging.INFO)

@app.route('/info')
def test_200():
    app.logger.info("Request successful", extra={"status_code": 200})
    return "OK", 200

@app.route('/warning')
def test_400():
    app.logger.warning("Client made a bad request", extra={"status_code": 400})
    return "Bad Request", 400

@app.route('/error')
def test_500():
    app.logger.error("Server encountered an error", extra={"status_code": 500})
    return "Internal Server Error", 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

