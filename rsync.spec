#
# Conditional build:
%bcond_with	rsh	# set remote shell command to rsh instead of ssh (old behaviour)
#
Summary:	Program for efficient remote updates of files
Summary(es):	Programa para actualizar archivos remotos de forma eficiente
Summary(ko):	³×Æ®¿öÅ©¸¦ ÅëÇÑ ÆÄÀÏµ¿±âÈ­¸¦ À§ÇÑ ÇÁ·Î±×·¥
Summary(pl):	Program do wydajnego zdalnego uaktualniania plików
Summary(pt_BR):	Programa para atualizar arquivos remotos de forma eficiente
Summary(ru):	ðÒÏÇÒÁÍÍÁ ÄÌÑ ÜÆÆÅËÔÉ×ÎÏÇÏ ÕÄÁÌÅÎÎÏÇÏ ÏÂÎÏ×ÌÅÎÉÑ ÆÁÊÌÏ×
Summary(uk):	ðÒÏÇÒÁÍÁ ÄÌÑ ÅÆÅËÔÉ×ÎÏÇÏ ×¦ÄÄÁÌÅÎÏÇÏ ÏÎÏ×ÌÅÎÎÑ ÆÁÊÌ¦×
Summary(zh_CN):	[Í¨Ñ¶]´«Êä¹¤¾ß
Summary(zh_TW):	[³ñ°Ô]$(B6G?i¤õ(c(B
Name:		rsync
Version:	2.6.5
Release:	1
License:	GPL
Group:		Daemons
Source0:	http://rsync.samba.org/ftp/rsync/%{name}-%{version}.tar.gz
# Source0-md5:	3691cdf1540d0649ba679edce6bae8fc
Source1:	%{name}.inet
Source2:	%{name}.init
Source3:	%{name}.sysconfig
Source4:	%{name}d.logrotate
Patch0:		%{name}-config.patch
Patch1:		%{name}-man.patch
BuildRequires:	autoconf >= 2.52
BuildRequires:	automake
BuildRequires:	popt-devel
URL:		http://rsync.samba.org/
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_sysconfdir	/etc/rsyncd

%description
rsync is a replacement for rcp that has many more features.

rsync uses the "rsync algorithm" which provides a very fast method for
bringing remote files into sync. It does this by sending just the
differences in the files across the link, without requiring that both
sets of files are present at one of the ends of the link beforehand.

A technical report describing the rsync algorithm is included with
this package.

%description -l es
rsync es un substituto más rápido y flexible para rcp que permite la
sincronización de archivos o directorios, vía red, de forma rápida y
eficiente, entre diferentes máquinas transfiriendo solamente las
diferencias entre estos directorios de forma compactada. No necesita
que ninguna de las máquinas tengan una copia de lo que está en la
otra. Está disponible en este paquete, una relación técnica
describiendo el algoritmo usado por el rsync.

%description -l ko
Rsync´Â ¿ø°Ý È£½ºÆ® ÆÄÀÏÀ» ¸Å¿ì »¡¸® µ¿±âÈ­ÇÏ´Âµ¥ ½Å·ÚÇÒ¸¸ÇÑ
¾Ë°í¸®ÁòÀ» »ç¿ëÇÑ´Ù. Rsync´Â ÆÄÀÏÀÇ ÀüÃ¼¸¦ º¸³»´Â °Í ´ë½Å¿¡ ³×Æ®¿÷À»
ÅëÇØ ÆÄÀÏÀÇ ´Ù¸¥ ºÎºÐ¸¸À» Àü¼ÛÇÏ±â ¶§¹®¿¡ ºü¸£´Ù. Rsync´Â °­·ÂÇÑ ¹Ì·¯
ÇÁ·Î¼¼½º È¤Àº rcp Ä¿¸àµå¸¦ ÅëÇÑ ´õ ¿ì¼öÇÑ ´ëÃ¼¿ëÀ¸·Î½á »ç¿ëµÈ´Ù. rsync
¾Ë°í¸®ÁòÀ» ¹¦»çÇÏ´Â ±â¼úÀûÀÎ ³»¿ëÀº ÀÌ ²Ù·¯¹Ì¿¡ Æ÷ÇÔµÇ¾î ÀÖ´Ù.

%description -l pl
Rsync jest zamiennikiem programu rcp z bardziej rozbudowan± sk³adni±
poleceñ. Program ten u¿ywa efektywnego algorytmu "rsync" w czasie
komunikacji i transportu plików do systemu zdalnego. Dokumentacja
techniczna nowego algorytmu zosta³a równie¿ do³±czona do pakietu.

%description -l pt_BR
O rsync é um substituto mais rápido e flexível para o rcp permitindo
sincronização de arquivos ou diretórios via rede de forma rápida e
eficiente entre diferentes máquinas transferindo somente as diferenças
entre estes diretórios de forma compactada. Ele não precisa que
nenhuma das máquinas tenha uma cópia do que está na outra.

Um relatório técnico descrevendo o algoritmo usado pelo rsync está
disponível neste pacote.

%description -l ru
rsync - ÜÔÏ ÂÏÌÅÅ ÂÙÓÔÒÁÑ É ÇÉÂËÁÑ ÁÌØÔÅÒÎÁÔÉ×Á rcp, ÐÏÚ×ÏÌÑÀÝÁÑ
ÂÙÓÔÒÕÀ É ÜÆÆÅËÔÉ×ÎÕÀ ÐÏ ÏÔÎÏÛÅÎÉÀ Ë ÒÅÓÕÒÓÁÍ ÓÅÔÉ ÓÉÎÈÒÏÎÉÚÁÃÉÀ
ÆÁÊÌÏ× ÉÌÉ ËÁÔÁÌÏÇÏ× ÎÁ ÒÁÚÌÉÞÎÙÈ ÍÁÛÉÎÁÈ ÐÕÔÅÍ ÐÅÒÅÄÁÞÉ ÔÏÌØËÏ
ÒÁÚÌÉÞÉÊ ÍÅÖÄÕ ÎÉÍÉ × ËÏÍÐÒÅÓÓÉÒÏ×ÁÎÎÏÍ ×ÉÄÅ. ðÒÉ ÜÔÏÍ ÓÏ×ÅÒÛÅÎÎÏ ÎÅ
ÏÂÑÚÁÔÅÌØÎÏ, ÞÔÏÂÙ ÏÄÎÁ ÍÁÛÉÎÁ ÉÍÅÌÁ Õ ÓÅÂÑ ËÏÐÉÀ ÔÏÇÏ, ÞÔÏ ÅÓÔØ ÎÁ
ÄÒÕÇÏÊ ÍÁÛÉÎÅ.

%description -l uk
rsync - ÃÅ Û×ÉÄÛÁ ÔÁ ÇÎÕÞË¦ÛÁ ÁÌØÔÅÒÎÁÔÉ×Á rcp, ÑËÁ ÚÁÂÅÚÐÅÞÕ¤ Û×ÉÄËÕ
ÔÁ ÅÆÅËÔÉ×ÎÕ ÐÏ ×¦ÄÎÏÛÅÎÎÀ ÄÏ ÒÅÓÕÒÓ¦× ÍÅÒÅÖ¦ ÓÉÎÈÒÏÎ¦ÚÁÃ¦À ÆÁÊÌ¦× ÞÉ
ËÁÔÁÌÏÇ¦× ÎÁ Ò¦ÚÎÉÈ ÍÁÛÉÎÁÈ ÛÌÑÈÏÍ ÐÅÒÅÄÁÞ¦ ÌÉÛÅ ×¦ÄÍ¦ÎÎÏÓÔÅÊ Í¦Ö ÎÉÍÉ
× ËÏÍÐÒÅÓÏ×ÁÎÏÍÕ ×ÉÄ¦. ðÒÉ ÃØÏÍÕ ÚÏ×Ó¦Í ÎÅ ÏÂÏ×'ÑÚËÏ×Ï, ÝÏÂ ÏÄÎÁ
ÍÁÛÉÎÁ ÍÁÌÁ × ÓÅÂÅ ËÏÐ¦À ÔÏÇÏ, ÝÏ ¤ ÎÁ ¦ÎÛ¦Ê ÍÁÛÉÎ¦.

%package -n rsyncd-inetd
Summary:	Files necessary to run rsync in daemon mode
Summary(pl):	Pliki niezbêdne do uruchomienia rsynca w trybie serwera
Group:		Daemons
PreReq:		rc-inetd
Requires:	%{name}
Provides:	rsyncd
Obsoletes:	rsyncd
Obsoletes:	rsyncd-standalone

%description -n rsyncd-inetd
rsync is a replacement for rcp that has many more features.

rsync uses the "rsync algorithm" which provides a very fast method for
bringing remote files into sync. It does this by sending just the
differences in the files across the link, without requiring that both
sets of files are present at one of the ends of the link beforehand.

A technical report describing the rsync algorithm is included with
this package.

%description -n rsyncd-inetd -l pl
Rsync jest zamiennikiem programu rcp z bardziej rozbudowan± sk³adni±
poleceñ. Program ten u¿ywa efektywnego algorytmu "rsync" w czasie
komunikacji i transportu plików do systemu zdalnego. Dokumentacja
techniczna nowego algorytmu zosta³a równie¿ do³±czona do pakietu.

%package -n rsyncd-standalone
Summary:	Files necessary to run rsync in daemon mode
Summary(pl):	Pliki niezbêdne do uruchomienia rsynca w trybie serwera
Group:		Daemons
Requires(post,preun):	/sbin/chkconfig
Requires:	%{name}
Provides:	rsyncd
Obsoletes:	rsyncd
Obsoletes:	rsyncd-inetd

%description -n rsyncd-standalone
rsync is a replacement for rcp that has many more features.

rsync uses the "rsync algorithm" which provides a very fast method for
bringing remote files into sync. It does this by sending just the
differences in the files across the link, without requiring that both
sets of files are present at one of the ends of the link beforehand.

A technical report describing the rsync algorithm is included with
this package.

%description -n rsyncd-standalone -l pl
Rsync jest zamiennikiem programu rcp z bardziej rozbudowan± sk³adni±
poleceñ. Program ten u¿ywa efektywnego algorytmu "rsync" w czasie
komunikacji i transportu plików do systemu zdalnego. Dokumentacja
techniczna nowego algorytmu zosta³a równie¿ do³±czona do pakietu.

%prep
%setup -q
%patch0 -p1
%patch1 -p1

%build
cp -f %{_datadir}/automake/config.sub .
%{__autoconf}
%configure \
	%{?with_rsh:--with-rsh=rsh} \
	--enable-ipv6 \
	--disable-debug \
	--with-rsyncd-conf=%{_sysconfdir}/rsyncd.conf

%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT/etc/env.d

%{__make} install \
	prefix=$RPM_BUILD_ROOT%{_prefix} \
	mandir=$RPM_BUILD_ROOT%{_mandir} \
	bindir=$RPM_BUILD_ROOT%{_bindir}

install -d $RPM_BUILD_ROOT{%{_sysconfdir},/etc/{sysconfig/rc-inetd,rc.d/init.d,logrotate.d},/var/log}

:> $RPM_BUILD_ROOT/var/log/rsyncd.log
:> $RPM_BUILD_ROOT%{_sysconfdir}/rsyncd.secrets

cat << EOF > $RPM_BUILD_ROOT%{_sysconfdir}/rsyncd.conf
log file = /var/log/rsyncd.log
EOF

cat << EOF > $RPM_BUILD_ROOT/etc/env.d/CVSIGNORE
#CVSIGNORE=
EOF
cat << EOF > $RPM_BUILD_ROOT/etc/env.d/RSYNC_RSH
#RSYNC_RSH=
EOF
cat << EOF > $RPM_BUILD_ROOT/etc/env.d/RSYNC_PROXY
#RSYNC_PROXY=
EOF
cat << EOF > $RPM_BUILD_ROOT/etc/env.d/RSYNC_PASSWORD
#RSYNC_PASSWORD=
EOF

install %{SOURCE1} $RPM_BUILD_ROOT/etc/sysconfig/rc-inetd/rsyncd
install %{SOURCE2} $RPM_BUILD_ROOT/etc/rc.d/init.d/rsyncd
install %{SOURCE3} $RPM_BUILD_ROOT/etc/sysconfig/rsyncd
install %{SOURCE4} $RPM_BUILD_ROOT/etc/logrotate.d/rsyncd

%clean
rm -rf $RPM_BUILD_ROOT

%post -n rsyncd-inetd
if [ -f /var/lock/subsys/rc-inetd ]; then
	/etc/rc.d/init.d/rc-inetd restart 1>&2
else
	echo "Type \"/etc/rc.d/init.d/rc-inetd start\" to start inet server" 1>&2
fi

%postun -n rsyncd-inetd
if [ "$1" = "0" -a -f /var/lock/subsys/rc-inetd ]; then
	/etc/rc.d/init.d/rc-inetd reload 1>&2
fi

%post -n rsyncd-standalone
/sbin/chkconfig --add rsyncd
if [ -f /var/lock/subsys/rsyncd ]; then
	/etc/rc.d/init.d/rsyncd restart 1>&2
else
	echo "Type \"/etc/rc.d/init.d/rsyncd start\" to start rsync server" 1>&2
fi

%preun -n rsyncd-standalone
if [ "$1" = "0" ]; then
	if [ -f /var/lock/subsys/rsyncd ]; then
		/etc/rc.d/init.d/rsyncd stop 1>&2
	fi
	/sbin/chkconfig --del rsyncd
fi

%files
%defattr(644,root,root,755)
%doc README NEWS OLDNEWS TODO
%attr(644,root,root) %config(noreplace,missingok) %verify(not md5 mtime size) /etc/env.d/*
%attr(755,root,root) %{_bindir}/*
%{_mandir}/man1/*

%files -n rsyncd-inetd
%defattr(644,root,root,755)
%dir %{_sysconfdir}
%attr(640,root,root) %config(noreplace) %{_sysconfdir}/rsyncd.conf
%attr(640,root,root) %config(noreplace) %{_sysconfdir}/rsyncd.secrets
%attr(640,root,root) %config(noreplace) %verify(not md5 mtime size) /etc/logrotate.d/rsyncd
%attr(640,root,root) %config(noreplace) %verify(not md5 mtime size) /etc/sysconfig/rc-inetd/rsyncd
%attr(640,root,root) %ghost /var/log/rsyncd.log
%{_mandir}/man5/*

%files -n rsyncd-standalone
%defattr(644,root,root,755)
%dir %{_sysconfdir}
%attr(640,root,root) %config(noreplace) %{_sysconfdir}/rsyncd.conf
%attr(640,root,root) %config(noreplace) %{_sysconfdir}/rsyncd.secrets
%attr(640,root,root) %config(noreplace) %verify(not md5 mtime size) /etc/sysconfig/rsyncd
%attr(640,root,root) %config(noreplace) %verify(not md5 mtime size) /etc/logrotate.d/rsyncd
%attr(640,root,root) %ghost /var/log/rsyncd.log
%attr(754,root,root) /etc/rc.d/init.d/rsyncd
%{_mandir}/man5/*
