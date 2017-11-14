import http.server

from GetControl import GetControl


class VerbHandler(http.server.BaseHTTPRequestHandler):

    def do_GET(self):
        """Respond to a GET request."""
        try:
            path = self.path

            # Based on the path we are given, do different functions
            control = GetControl()
            result = {
                '/PhoneOn': control.phoneOn,
                '/PhoneOff': control.phoneOff,
                '/PhoneHeartbeat': control.heartbeat,
                }[path]()

            # Out the results back to the server
            self.setHeader()
            self.wfile.write(str(result).encode())
        except Exception as e:
            self.setHeader()
            output = '{"Error":"%s"}\n'%(e)
            self.wfile.write(output.encode())
            raise e

    def do_POST(self):
        pass

    def setHeader(self):
        self.send_response(200)
        self.send_header("Content-type", "application/json".encode())
        self.end_headers()
