prefix = /usr/local

help:
	@echo "= more Makefile for anubis"
	@echo "make install             install binary + config"
	@echo "make install-systemd     install systemd unit"
	@echo
	@echo "= Make variables"
	@echo 'Your $${prefix} is ${prefix}'
	@echo 'Your $${MAKE} is ${MAKE}'

install: ${prefix}/bin/anubis ${prefix}/etc/anubis/nginx.env

${prefix}/bin/anubis: ../var/anubis
	install -m755 ../var/anubis $@

${prefix}/etc/anubis/nginx.env: etc/anubis/nginx.env
	install -m644 etc/anubis/nginx.env $@

../var/anubis:
	# Should run make build -> assets -> deps in that order
	${MAKE} -C .. build

install-systemd: ${prefix}/lib/systemd/system/anubis@.service

${prefix}/lib/systemd/system/anubis@.service: lib/systemd/system/anubis@.service
	install -m644 lib/systemd/system/anubis@.service $@

clean:
	git clean -fdx ..
