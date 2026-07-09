# 🖼️ IMAGIKA — Image Processing & Object Detection System

Imagika is a web-based image processing and object detection application developed using Python, OpenCV, YOLOv3, MySQL, and web technologies.

The application allows users to upload images, process them, detect objects present in the images, generate useful metadata, and manage their uploaded image history.

The project was developed to explore the practical integration of Computer Vision, Object Detection, Backend Development, Database Management, Authentication, and Web Development.

---

## 🎥 Project Demo

A video demonstration of the Imagika application is available here:

▶️ [Watch Imagika Project Demo](https://www.linkedin.com/posts/rushi-gohel-57a8b62a7_imagika-prototype-imageprocessing-ugcPost-7261026075432919040-_are/?utm_source=share&utm_medium=member_desktop&rcm=ACoAAEn-dq4BtWWIBujyDZHa5C8b2HkkWVsJtyw)

The demo shows the working application, including image uploading, object detection, and other major features of the system.

---

## 🚀 Project Overview

Imagika combines web development with computer vision to create an interactive image processing system.

Users can create an account, log in to the application, upload images, process those images using the YOLOv3 object detection model, and view the detected objects and generated information.

The application uses a custom Python HTTP server for handling web requests and MySQL for storing application data.

---

## ✨ Key Features

### 👤 User Authentication

- User Registration
- User Login
- Custom Authentication System
- Session Management
- Cookie-based Session Handling
- User Logout
- Database-based User Management

### 🖼️ Image Management

- Image Upload
- Image Storage
- Image Processing
- Uploaded Image History
- User-specific Image Management
- Image Data Storage in Database

### 🔍 Object Detection

- YOLOv3 Object Detection
- OpenCV-based Image Processing
- Detection of Multiple Objects
- Bounding Box Generation
- Object Label Detection
- Processed Image Generation

### 🏷️ Metadata Processing

- Detection-based Image Information
- Object Label Extraction
- Image Metadata Generation
- Storage of Image-related Information

### 👨‍💻 User Profile

- User Profile Management
- User-specific Uploaded Images
- Image History
- Database-connected User Information

### 📱 Web Interface

- Responsive Web Design
- Navigation System
- User-friendly Image Upload Interface
- Dynamic Result Display
- Bootstrap-based Responsive Layout

---

## 🛠️ Technologies Used

### Backend

- Python
- Python HTTP Server
- SocketServer
- MySQL Database
- Session Management
- Cookie-based Authentication

### Computer Vision

- OpenCV
- YOLOv3
- COCO Dataset Labels
- Image Processing
- Object Detection

### Frontend

- HTML5
- CSS3
- JavaScript
- Bootstrap

### Database

- MySQL

### Development Tools

- Git
- GitHub
- Visual Studio Code / PyCharm
- XAMPP

---

## 🧠 How Imagika Works

The basic workflow of the application is:

1. A user creates an account or logs into the application.
2. The server validates the user's credentials.
3. A session is created for the authenticated user.
4. The user uploads an image through the web interface.
5. The uploaded image is stored on the server.
6. The image is processed using OpenCV and YOLOv3.
7. YOLOv3 detects objects present in the image.
8. Bounding boxes and object labels are generated.
9. The processed image is saved.
10. Image information is stored in the MySQL database.
11. The result is displayed to the user.
12. The user can access previously uploaded images through their profile.

---

## 🔍 Object Detection Workflow

```text
User Uploads Image
        ↓
Python Server Receives Image
        ↓
Image Stored in Upload Directory
        ↓
YOLOv3 Model Loads Image
        ↓
OpenCV Processes Image
        ↓
Objects Are Detected
        ↓
Bounding Boxes and Labels Are Generated
        ↓
Processed Image Is Saved
        ↓
Image Information Stored in Database
        ↓
Detection Result Displayed to User
