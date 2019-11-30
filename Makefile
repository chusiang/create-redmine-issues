
main: run

run:
	docker-compose up -d

clean:
	docker-compose down -v
