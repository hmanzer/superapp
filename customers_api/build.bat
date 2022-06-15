set DOCKER_REPO=gcr.io/sacred-sol-210014/cusapi
set BUILD_NUMBER=0.0.1
docker build -t %DOCKER_REPO%:%BUILD_NUMBER% .


REM mysql container doesn't require any building, all tables etc are built as part of sqlalchemy/python modules.
REM mysql container only requires user/password/database/root password. The database is created as part of setup.
REM python creates the table on startup without a script.