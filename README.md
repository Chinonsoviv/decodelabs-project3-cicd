
# DecodeLabs Project 3, CI/CD Pipeline with Flask Deployment

A fully automated CI/CD pipeline built with GitHub Actions that deploys a live Flask web application to AWS EC2 on every git push, with zero manual intervention.

## Live Application
http://63.176.162.241

## Tech Stack
- GitHub Actions, CI/CD automation
- Python 3 and Flask, web application
- pytest, automated testing
- AWS EC2 Ubuntu 22.04 LTS, cloud server
- GitHub Secrets, secure credential management
- WSL Ubuntu, local development environment

## Pipeline Stages
1. Build and Test, installs dependencies and runs automated pytest tests
2. Deploy to EC2, SSHs into AWS EC2, pulls latest code, restarts Flask server

## Author
Chinonso Vivian Ojeri, Cloud and DevOps Engineer
- Portfolio: chinonsocloudsec.online
- GitHub: github.com/Chinonsoviv
- LinkedIn: linkedin.com/in/chinonso-vivian-ojeri
EOF
