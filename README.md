# Conda Repo Server

Simple and not secured conda repo server

Send files via post request to e.g. http://conda-repo.local/upload/channelname/linux-64
The files will be served from http://conda-repo.local/conda/channelname/linux-64 and conda index will be run on this channel to provide conda repository files.

According to an idea presented in https://stefan.sofa-rockers.org/2019/04/18/python-packaging-gitlab-conda/#set-up-gitlab-and-a-conda-repo-server