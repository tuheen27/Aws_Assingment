# AWS DevOps Course Assignment

## Simple Flask Web Application

### Assignment Overview
This is a simple web application created for the AWS DevOps Course assignment. The project demonstrates basic web application development, containerization, and AWS cloud deployment concepts covered in the course.

### Project Description
This Flask application serves a simple web interface and provides JSON data through an API endpoint. It showcases fundamental concepts of web development, API creation, and cloud service integration that are essential for modern DevOps practices.

### Features
- **Web Interface**: Clean HTML frontend accessible at root URL
- **REST API**: JSON data endpoint at `/data` route
- **AWS Deployment Ready**: Configured to be deployed on AWS services
- **DevOps Pipeline Compatible**: Can be integrated with CI/CD workflows

### Technologies Used
- **Backend**: Python 3 with Flask framework
- **Frontend**: HTML, CSS, and JavaScript
- **Deployment**: Ready for AWS cloud services
- **Architecture**: RESTful API design

## Project Setup

### Prerequisites
- Python 3.6 or higher
- pip (Python package manager)
- AWS account (for deployment)

### Local Development Setup
1. **Clone the repository**
   ```bash
   git clone https://github.com/tuheen27/Aws_Assingment.git
   cd Aws_Assingment
   ```

2. **Install required packages**
   ```bash
   pip install -r requirements.txt
   ```

3. **Run the application**
   ```bash
   python simple_app.py
   ```

4. **Access the application**
   - Web Interface: http://localhost:5000
   - JSON Data API: http://localhost:5000/data

## AWS Deployment Instructions

This application can be deployed to AWS using multiple approaches covered in the DevOps course:

### EC2 Deployment
1. Launch an EC2 instance with Amazon Linux 2
2. Install Python and dependencies
3. Clone this repository to the instance
4. Configure security groups to allow HTTP traffic (port 80/5000)
5. Run the application

### Container Deployment (ECS/ECR)
1. Create a Dockerfile to containerize the application
2. Build and push the container image to Amazon ECR
3. Create an ECS cluster and task definition
4. Deploy the container to ECS

### Serverless Deployment
1. Convert the application to use AWS Lambda and API Gateway
2. Package the application with necessary dependencies
3. Deploy using AWS SAM or Serverless Framework

