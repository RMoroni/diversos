#!/bin/bash
function install_requirements {
    apt -y update
    # apt -y upgrade
    apt -y install python3-pip
    pip3 install --user -r requirements.txt
    # apt -y install postgresql postgresql-contrib
    # su postgres
    # psql
    # \q
}
# CONFIG DB: https://airflow.apache.org/docs/apache-airflow/2.2.1/howto/set-up-database.html
# function run {    
#     case $1 in 
#     "build") build ;;
#     *) echo "Invalid option" ;;
#     esac
# }

# if [ "$*" != "" ]; then
#     execute "$*"
# else
#     echo "Choose what to do: "
#     select option in "build" "run" "build and run"
#     do
#     run "${option}"
#     break
#     done
# fi
install_requirements

# init airflow
# airflow standalone

airflow db init

airflow users create \
    --username ryuk \
    --firstname Ryuk \
    --lastname Shinigami \
    --role Admin \
    --email rodrigomoroni@hotmail.com
    --password kira

airflow webserver --port 8080

airflow scheduler

docker run -it --network=host 0f778fa22e4c bash