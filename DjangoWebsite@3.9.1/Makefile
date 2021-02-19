# Specify alias
# -t is name of image tag
# Have to specify path to directory where docker file is located (its in same dir)
# $(options) is a variable name
build:	
	docker build --force-rm $(options) -t hackershack-website-tutorial:latest .

# Build dev image
build-prod:
	$(MAKE) build options="--target production"

# up starts up services
compose-start:
	docker-compose up --remove-orphans $(options)

# stop docker compose services from running. Control ^C keeps images running remove containers
compose-stop:
	docker-compose down --remove-orphans $(options)

# CLI tool "run", runs any arbitary command in one of the services that are running in the compose file, will run parents services that that service is dependent on
# service name is website
# we can insert any cmd, aka make compose-manage-py cmd=makemigrations
compose-manage-py:
	docker-compose run --rm $(options) website python manage.py $(cmd) 