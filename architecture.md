+---------------------+
|     Web Browsers    |  <-- Clients making requests
+---------------------+
          ||
          \/
+---------------------+
|    API Gateway      |  <-- Rate limiting, JWT authentication
+---------------------+
          ||
          \/
+---------------------+
|  CherryPy App       |  <-- Application logic, endpoints
+---------------------+
          ||
          \/
+---------------------+
|    Services Layer   |  <-- Email, File handling, Task queue
+---------------------+
          ||
          \/
+---------------------+
|    Database (PostgreSQL)  |  <-- Data storage
+---------------------+
          ||
          \/
+---------------------+
|   File Storage (S3) |  <-- If using S3 for file uploads
+---------------------+
