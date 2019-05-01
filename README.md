# Conda Repo Server

Simple and not secured conda repo server

Send files via post request to e.g. http://conda-repo.local/upload/channelname/linux-64
The files will be served from http://conda-repo.local/conda/channelname/linux-64 and conda index will be run on this channel to provide conda repository files.