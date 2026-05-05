pipeline {
    agent any

    options {
        timestamps()
        disableConcurrentBuilds()
    }

    parameters {
        booleanParam(
            name: 'RUN_TESTS',
            defaultValue: true,
            description: 'Run automated tests when a supported project type is detected.'
        )
    }

    environment {
        CI = 'true'
    }

    stages {
        stage('Checkout') {
            steps {
                checkout scm
            }
        }
        stage('Inspect Src') {
            steps {
                script {
                    if (isUnix()) {
                        sh '''
                            pwd
                            ls -la
                            ls -la src
                        '''
                    } else {
                        powershell 'Get-Location; Get-ChildItem -Force; Get-ChildItem -Force src'
                    }
                }
            }
        }
        stage('Build') {
            steps {
                script {
                    if (fileExists('requirements.txt') && fileExists('src')) {
                        if (isUnix()) {
                            sh '''
                                python -m pip install --upgrade pip
                                python -m pip install -r requirements.txt
                                python -m compileall src
                            '''
                        } else {
                            bat '''
                                call python -m pip install --upgrade pip
                                call python -m pip install -r requirements.txt
                                call python -m compileall src
                            '''
                        }
                    } else {
                        error 'This pipeline expects requirements.txt and the src folder.'
                    }
                }
            }
        }
        stage('Test') {
            when {
                expression {
                    return params.RUN_TESTS
                }
            }
            steps {
                script {
                    if (fileExists('src/test_preprocessing.py')) {
                        if (isUnix()) {
                            sh 'python -m unittest discover -s src -p "test_*.py" -v'
                        } else {
                            bat 'call python -m unittest discover -s src -p "test_*.py" -v'
                        }
                    } else {
                        error 'Expected src/test_preprocessing.py for validation.'
                    }
                }
            }
        }
    }

    post {
        always {
            archiveArtifacts(
                artifacts: 'src/**',
                allowEmptyArchive: true
            )
        }
        success {
            echo 'Pipeline completed successfully.'
        }
        failure {
            echo 'Pipeline failed. Review the failed stage in the Jenkins build log.'
        }
    }
}