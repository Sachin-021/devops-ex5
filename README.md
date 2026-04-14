pipeline {
    agent any

    environment {
        STREAMLIT_SUPPRESS_PROMPT = 'true'
    }

    stages {

        stage('Clone Repo') {
            steps {
                git branch: 'main', url: 'https://github.com/Sachin-021/devops-ex5.git'
            }
        }

        stage('Install Dependencies') {
            steps {
                bat "python -m venv venv"
                bat "call venv\\Scripts\\activate && pip install -r requirements.txt"
            }
        }

        stage('Run Streamlit App') {
            steps {
                bat "call venv\\Scripts\\activate && streamlit run streamlit_app.py --server.headless true"
            }
        }
    }
}
