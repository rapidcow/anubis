prefix = /usr/local
systemd_prefix = ${prefix}/lib/systemd/system
# XDG_CONFIG_HOME is usually ${HOME}/.config
# alas, i am not sure if systemd looks at XDG_CONFIG_HOME...
# systemd.unit(5) says ~/.config/systemd/user without any variables
systemd_local_prefix = ${XDG_CONFIG_HOME}/systemd/user
GO = /usr/bin/env go

help:
	@echo "= more Makefile for anubis"
	@echo "make install             install binary + config"
	@echo "make install-local          ... with test config"
	@echo "make install-systemd     install systemd unit"
	@echo "make install-systemd-local  ... ditto"
	@echo
	@echo "= Make variables"
	@echo 'Your $${prefix} is ${prefix}'
	@echo 'Your $${MAKE} is ${MAKE}'

install: ${prefix}/bin/anubis ${prefix}/etc/anubis/nginx.env
install-local: ${prefix}/bin/anubis ${prefix}/etc/anubis/local.env

${prefix}/bin/anubis: ../var/anubis
	install -m755 -d ${prefix}/bin
	install -m755 ../var/anubis $@

${prefix}/etc/anubis/nginx.env: etc/anubis/nginx.env
	install -m755 -d ${prefix}/etc/anubis
	install -m644 etc/anubis/nginx.env $@
${prefix}/etc/anubis/local.env: etc/anubis/local.env
	install -m755 -d ${prefix}/etc/anubis
	install -m644 etc/anubis/local.env $@

../var/anubis:
	@# Should run make build -> assets -> deps in that order
	${MAKE} -C .. assets
	cd .. && $(GO) build -o ./var/anubis -ldflags "-X 'github.com/TecharoHQ/anubis.Version=$$(git describe --tags)'" ./cmd/anubis
	cd .. && $(GO) build -o ./var/robots2policy -ldflags "-X 'github.com/TecharoHQ/anubis.Version=$$(git describe --tags)'" ./cmd/robots2policy
	@echo "Anubis $$(git describe --tags) is now built to ./var/anubis"

install-systemd: ${systemd_prefix}/anubis@.service
install-systemd-local: ${systemd_local_prefix}/anubis-local.service

${systemd_prefix}/anubis@.service: lib/systemd/system/anubis@.service
	install -m755 -d ${systemd_prefix}
	install -m644 lib/systemd/system/anubis@.service $@
${systemd_local_prefix}/anubis-local.service: lib/systemd/system/anubis-local.service
	install -m755 -d ${systemd_local_prefix}
	sed 's:~/:${HOME}/:' < lib/systemd/system/anubis-local.service > $@ && chmod 644 $@

clean:
	git clean -fdx ..
