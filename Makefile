
main: run

create_venv:
	virtualenv -p python3 .venv


install_packages:
	.venv/bin/pip3 install -r requirements.txt

init: create_venv install_packages

run:
	docker-compose up -d

clean:
	docker-compose down -v
