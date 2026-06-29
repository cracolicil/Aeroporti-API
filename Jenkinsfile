pipeline{
    agent{
        node{
            label 'python'
        }
    }

    environment{
        PYTHON_VERSION = "3.13"
        VIRTUAL_ENV = "venv"
        API_KEY = "chiave"
    }

    stages{
        stage('Checkout'){
            steps{
                echo 'Gathering code from version control'
		        git branch: 'main', url: 'https://github.com/cracolicil/Aeroporti-API.git'
            }
        }
        stage('Setup Environment'){
            steps{
                sh '''
                    python${PYTHON_VERSION} -m venv ${VIRTUAL_ENV}
                    . ${VIRTUAL_ENV}/bin/activate
                '''
            }
        }
        stage('Install dependencies'){
            steps{
                sh '''
                    . ${VIRTUAL_ENV}/bin/activate
                    pip install --no-cache-dir -r requirements.txt
                '''
            }
        }
        stage('Test'){
            steps{
                sh '''
                    . ${VIRTUAL_ENV}/bin/activate
                    export api_key=${API_KEY}
                    python -m pytest tests/test_airport.py --junitxml=${WORKSPACE}/test_report.xml
                '''
            }
            post{
                always{
                    archiveArtifacts artifacts: 'test_report.xml', allowEmptyArchive: true
                }
        }
        }
        stage('Deploy'){
            steps{
                echo 'Deploying...'
            }
        }
    }
}