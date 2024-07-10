import mysql.connector
import http.server
import socketserver
import cgi
import os

class CustomHTTPRequestHandler(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):
        if self.path == "/":
            self.path = "./frontend/index.html"
            return http.server.SimpleHTTPRequestHandler.do_GET(self)
        else:
            return http.server.SimpleHTTPRequestHandler.do_GET(self)

    def do_POST(self):
        if self.path == "/upload":
            # Parse the form data
            form = cgi.FieldStorage(fp=self.rfile, headers=self.headers, environ={'REQUEST_METHOD': 'POST'})

            # Retrieve the file and name
            if "file" not in form:
                self.send_response(400)
                self.end_headers()
                self.wfile.write(b"Image name and file are required.")
                return

            file_field = form["file"]

            # Check if the file field is uploaded file
            if not file_field.file:
                self.send_response(400)
                self.end_headers()
                self.wfile.write(b"File upload failed.")
                return

            # Save the uploaded file to a directory
            upload_dir = "./uploads"
            os.makedirs(upload_dir, exist_ok=True)
            file_path = os.path.join(upload_dir, file_field.filename)
            with open(file_path, "wb") as f:
                f.write(file_field.file.read())

            # Insert the data into the database
        try:
            mydb = mysql.connector.connect(
                host="localhost",
                user="root",
                password="",  # Set your MySQL password
                database="imagika"
            )
            mycursor = mydb.cursor()

            # Insert data into the images table
            sql = "INSERT INTO images (file_path) VALUES (%s)"
            val = (file_path,)  # Make sure it's a tuple
            mycursor.execute(sql, val)
            mydb.commit()
            print(f"Inserted file path: {file_path}")

            mycursor.close()
            mydb.close()

            # Respond to the client
            self.send_response(200)
            self.end_headers()
            self.wfile.write(b"Image and path stored successfully.")
        except mysql.connector.Error as err:
            print(f"Database error: {err}")
            self.send_response(500)
            self.end_headers()
            self.wfile.write(f"Database error: {err}".encode())
    def response(self):
        self.email = getvalue("x")

    # insert into (id,...,location) vlaue(...,"localhost/uploads/imgname.extention")
    #  Configure and start the HTTP server
PORT = 9100
with socketserver.TCPServer(("", PORT), CustomHTTPRequestHandler) as httpd:
    print(f"Serving at port {PORT}")
    httpd.serve_forever()