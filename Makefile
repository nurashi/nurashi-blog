venv:
	@echo "Creating virtual environment..."
	@python3 -m venv venv
	@echo "Virtual environment created."

sample-pg-service:
	@echo "Adding database service to the pg_service.conf file..."
	@echo "[pg_nurashi_service] 
	       host=localhost
	       user=postgres
	       dbname=nurashi_blog
	       port=5432" >> ~/.pg_service.conf
	@echo "Sample pg_service file created."

sample-pg-pass:
	@echo "Creating sample pg_pass file..."
	@echo "localhost:5432:nurashi_blog:postgres:PASSWORD" > .pg_pass
	@echo "Sample pg_pass file created."
	@echo "Replace PASSWORD with your database password."

run:
	@echo "Running the application..."
	@source venv/bin/activate && python3 manage.py runserver
