# Detect operating system in Makefile.
# Author: He Tao
# Date: 2015-05-30
THIS_DIR := $(dir $(abspath $(firstword $(MAKEFILE_LIST))))source/
VERSION := 1.4
ifeq ($(OS),Windows_NT) 
all:: windows
	@echo ready
else
UNAME_S := $(shell uname -s)
ifeq ($(UNAME_S),Linux)
ifneq ("$wildcard /usr/bin/dpkg-deb", "") 
all:: debian
	@echo ready 
else 
all:: linux
	@echo ready
endif
endif
endif

windows:
	@python ./make/make.py $(THIS_DIR)
	@pyinstaller --log-level DEPRECATION ./make/make.spec
	
linux:
	@python3 ./make/make.py $(THIS_DIR)
	@pyinstaller --log-level DEPRECATION ./make/make.spec

debian: linux
	@cp ./dist/pyadvent ./make/ADVENT_pckg/usr/bin/ 
	@cp -r ./make/ADVENT_pckg ~/ADVENT_pckg #needed to wsl
	@dpkg-deb --build ~/ADVENT_pckg
	@cp ~/ADVENT_pckg.deb ./dist/pyadvent.deb
	@rm -r ~/ADVENT_pckg
	@rm ~/ADVENT_pckg.deb
