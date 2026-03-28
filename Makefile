run: ##@App Run the app locally (debug mode).
	uv run python app.py

login: ##@Heroku Login to Heroku CLI.
	heroku login

deploy: ##@Heroku Deploy to Heroku.
	git push heroku main

help: ##@Miscellaneous Show this help.
	@echo -e "Usage: make [target] ...\n"
	@perl -e '$(HELP_FUN)' $(MAKEFILE_LIST)

HELP_FUN = \
    %help; while(<>){push@{$$help{$$2//'options'}},[$$1,$$3] \
    if/^([\w-_]+)\s*:.*\#\#(?:@(\w+))?\s(.*)$$/}; \
    print"\033[33m$$_:\033[0m\n", map"  \033[1;94m$$_->[0]\033[0m".(" "x(20-length($$_->[0])))."$$_->[1]\n",\
    @{$$help{$$_}},"\n" for keys %help; \

.PHONY: run login deploy help
