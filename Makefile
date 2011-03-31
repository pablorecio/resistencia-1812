PREFIX ?= /usr
LIBINSTALLDIR ?= /lib
XDGCONFDIR ?= /etc/xdg

RESISTENCIALIBDIR = $(DESTDIR)$(PREFIX)$(LIBINSTALLDIR)/resistencia1812
RESISTENCIASHAREDIR = $(DESTDIR)$(PREFIX)/share/resistencia1812
RESISTENCIAHOMEDIR = $(DESTDIR)~/.resistencia1812

PACKAGES = resistencia guadaboard libguadalete

all: compile
	@echo "Ready to install..."

pyclips:
	wget http://downloads.sourceforge.net/project/pyclips/pyclips-old/pyclips-old-1.0/pyclips-1.0.6.335.tar.gz 
	tar xvf pyclips-1.0.6.335.tar.gz
	cd pyclips && python setup.py build && sudo python setup.py install && cd ..
	find . -name "pyclips-1.0.6.335.tar.gz" -exec rm -f {} \;
	find . -name "pyclips" -exec rm -rf {} \;

compile:
	python2.6 -m compileall -q $(PACKAGES)
	-python2.6 -O -m compileall -q $(PACKAGES)

make-install-dirs:
	mkdir -p $(DESTDIR)$(PREFIX)/bin
	mkdir -p $(RESISTENCIALIBDIR)
	mkdir -p $(RESISTENCIALIBDIR)/resistencia
	mkdir -p $(RESISTENCIALIBDIR)/resistencia/gui
	mkdir -p $(RESISTENCIALIBDIR)/resistencia/contest
	mkdir -p $(RESISTENCIALIBDIR)/resistencia/tests
	mkdir -p $(RESISTENCIALIBDIR)/guadaboard
	mkdir -p $(RESISTENCIALIBDIR)/libguadalete
	mkdir -p $(RESISTENCIASHAREDIR)
	mkdir -p $(RESISTENCIASHAREDIR)/data
	mkdir -p $(RESISTENCIASHAREDIR)/data/images
	mkdir -p $(RESISTENCIASHAREDIR)/data/glade
	mkdir -p $(RESISTENCIASHAREDIR)/data/fonts
	mkdir -p $(RESISTENCIASHAREDIR)/data/layouts
	mkdir -p $(RESISTENCIASHAREDIR)/data/music
	mkdir -p $(RESISTENCIASHAREDIR)/data/teams
	mkdir -p $(RESISTENCIASHAREDIR)/data/teams/rules
	mkdir -p $(RESISTENCIASHAREDIR)/data/teams/formations
	#mkdir -p $(RESISTENCIASHAREDIR)/data/migrations
	#mkdir -p $(RESISTENCIASHAREDIR)/data/migrations/migration_200907100931
	mkdir -p $(DESTDIR)$(PREFIX)/share/pixmaps
	mkdir -p $(DESTDIR)$(PREFIX)/share/applications
	#mkdir -p $(DESTDIR)$(XDGCONFDIR)/exaile

uninstall:
	rm -f  $(DESTDIR)$(PREFIX)/bin/resistencia1812
	rm -rf $(RESISTENCIALIBDIR)
	rm -rf $(RESISTENCIASHAREDIR)
	rm -rf $(DESTDIR)$(XDGCONFDIR)/resistencia1812
	rm -f $(DESTDIR)$(PREFIX)/share/applications/resistencia1812.desktop
	rm -f $(DESTDIR)$(PREFIX)/share/pixmaps/resistencia1812.png
	rm -rf $(RESISTENCIAHOMEDIR)

install: install-target locale install-locale

install_no_locale: install-target

install-target: make-install-dirs
	install -m 644 resistencia1812.py $(RESISTENCIALIBDIR)	
	-install -m 644 resistencia/*.py[co] $(RESISTENCIALIBDIR)/resistencia
	install -m 644 resistencia/*.py $(RESISTENCIALIBDIR)/resistencia
	-install -m 644 resistencia/gui/*.py[co] $(RESISTENCIALIBDIR)/resistencia/gui
	install -m 644 resistencia/gui/*.py $(RESISTENCIALIBDIR)/resistencia/gui
	-install -m 644 resistencia/contest/*.py[co] $(RESISTENCIALIBDIR)/resistencia/contest
	install -m 644 resistencia/contest/*.py $(RESISTENCIALIBDIR)/resistencia/contest
	install -m 644 resistencia/tests/*.py $(RESISTENCIALIBDIR)/resistencia/tests
	-install -m 644 guadaboard/*.py[co] $(RESISTENCIALIBDIR)/guadaboard
	install -m 644 guadaboard/*.py $(RESISTENCIALIBDIR)/guadaboard
	-install -m 644 libguadalete/*.py[co] $(RESISTENCIALIBDIR)/libguadalete
	install -m 644 libguadalete/*.py $(RESISTENCIALIBDIR)/libguadalete
	install -m 644 data/images/*.png $(RESISTENCIASHAREDIR)/data/images
	install -m 644 data/glade/*.glade $(RESISTENCIASHAREDIR)/data/glade
	install -m 644 data/layouts/*.xml $(RESISTENCIASHAREDIR)/data/layouts
	install -m 644 data/fonts/*.ttf $(RESISTENCIASHAREDIR)/data/fonts
	install -m 644 data/music/*.ogg $(RESISTENCIASHAREDIR)/data/music
	install -m 644 data/teams/rules/*.clp $(RESISTENCIASHAREDIR)/data/teams/rules
	install -m 644 data/teams/formations/*.clp $(RESISTENCIASHAREDIR)/data/teams/formations
	install -m 644 data/images/resistencia1812.png \
		$(DESTDIR)$(PREFIX)/share/pixmaps/resistencia1812.png
	install -m 644 data/resistencia1812.desktop \
		$(DESTDIR)$(PREFIX)/share/applications/	
	# the printf here is for bsd compat, dont use echo!
	cd $(DESTDIR)$(PREFIX)/bin && \
	 printf "#!/bin/sh\n\
	 exec python $(PREFIX)$(LIBINSTALLDIR)/resistencia1812/resistencia1812.py \
	 --datadir=$(PREFIX)/share/resistencia1812/data --startgui \"\$$@\"" \
	 > resistencia1812 && \
	 chmod 755 resistencia1812

locale:
	cd po && find . -name "*.po" -exec ../tools/compilepo.sh {} \; && cd ..

install-locale:
	for f in `find po -name resistencia1812.mo` ; do \
	  install -d -m 755 \
	    `echo $$f | sed "s|^po|$(DESTDIR)$(PREFIX)/share/locale|" | \
	      xargs dirname` && \
	  install -m 644 $$f \
	    `echo $$f | sed "s|^po|$(DESTDIR)$(PREFIX)/share/locale|"` ; \
	  done

clean:
	-find . -name "*.py[co]" -exec rm -f {} \;
	find . -name "*.class" -exec rm -f {} \;
	find . -name "*.bak" -exec rm -f {} \;
	find . -name "*~" -exec rm -f {} \;
	find . -name "pyclips-1.0.6.335.tar.gz" -exec rm -f {} \;
	find . -name "pyclips" -exec rm -rf {} \;
	find po/* -depth -type d -exec rm -r {} \;

clean-games:
	$(RM) ./data/games/*.txt

pot:
	@echo "[encoding: UTF-8]" > po/POTFILES.in
	find resistencia -name "*.py" >> po/POTFILES.in
	find guadaboard -name "*.py" >> po/POTFILES.in
	find libguadalete -name "*.py" >> po/POTFILES.in
	find data/glade/ -name "*.glade" >> po/POTFILES.in
	python tools/createpot.py

translations:
	python tools/createpot.py compile

potball:
	tar --bzip2 --format=posix -cf resistencia1812-po.tar.bz2 po/ \
	    --transform s/po/./

.PHONY: dist 

dist:
	mkdir -p dist
	rm -rf dist/copy
	bzr co --lightweight ./ dist/copy
	./tools/dist.sh
	rm -rf dist/copy