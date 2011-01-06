#
# Conditional build:
%bcond_with	rsh	# set remote shell command to rsh instead of ssh (old behaviour)
%bcond_with	tests	# perform "make test"
#
%ifarch alpha
%undefine	with_tests
%endif
Summary:	Program for efficient remote updates of files
Summary(es.UTF-8):	Programa para actualizar archivos remotos de forma eficiente
Summary(ko.UTF-8):	네트워크를 통한 파일동기화를 위한 프로그램
Summary(pl.UTF-8):	Program do wydajnego zdalnego uaktualniania plików
Summary(pt_BR.UTF-8):	Programa para atualizar arquivos remotos de forma eficiente
Summary(ru.UTF-8):	Программа для эффективного удаленного обновления файлов
Summary(uk.UTF-8):	Програма для ефективного віддаленого оновлення файлів
Summary(zh_CN.UTF-8):	[通讯]传输工具
Summary(zh_TW.UTF-8):	[喙啪]$(B6G?i火(c(B
Name:		rsync
Version:	3.0.7
Release:	3
License:	GPL
Group:		Networking/Utilities
Source0:	http://rsync.samba.org/ftp/rsync/%{name}-%{version}.tar.gz
# Source0-md5:	b53525900817cf1ba7ad3a516ab5bfe9
Source1:	http://rsync.samba.org/ftp/rsync/rsync-patches-%{version}.tar.gz
# Source1-md5:	48222e00a9a75873aee3bfceb2b2aa41
Source2:	%{name}.inet
Source3:	%{name}.init
Source4:	%{name}.sysconfig
Source5:	%{name}d.logrotate
Patch0:		%{name}-config.patch
Patch1:		%{name}-dparam.patch
URL:		http://rsync.samba.org/
BuildRequires:	acl-devel
BuildRequires:	autoconf >= 2.52
BuildRequires:	automake
BuildRequires:	openssl-devel
BuildRequires:	popt-devel
BuildRequires:	rpmbuild(macros) >= 1.318
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

%description -l es.UTF-8
rsync es un substituto más rápido y flexible para rcp que permite la
sincronización de archivos o directorios, vía red, de forma rápida y
eficiente, entre diferentes máquinas transfiriendo solamente las
diferencias entre estos directorios de forma compactada. No necesita
que ninguna de las máquinas tengan una copia de lo que está en la
otra. Está disponible en este paquete, una relación técnica
describiendo el algoritmo usado por el rsync.

%description -l ko.UTF-8
Rsync는 원격 호스트 파일을 매우 빨리 동기화하는데 신뢰할만한
알고리즘을 사용한다. Rsync는 파일의 전체를 보내는 것 대신에 네트웍을
통해 파일의 다른 부분만을 전송하기 때문에 빠르다. Rsync는 강력한 미러
프로세스 혹은 rcp 커멘드를 통한 더 우수한 대체용으로써 사용된다. rsync
알고리즘을 묘사하는 기술적인 내용은 이 꾸러미에 포함되어 있다.

%description -l pl.UTF-8
Rsync jest zamiennikiem programu rcp z bardziej rozbudowaną składnią
poleceń. Program ten używa efektywnego algorytmu "rsync" w czasie
komunikacji i transportu plików do systemu zdalnego. Dokumentacja
techniczna nowego algorytmu została również dołączona do pakietu.

%description -l pt_BR.UTF-8
O rsync é um substituto mais rápido e flexível para o rcp permitindo
sincronização de arquivos ou diretórios via rede de forma rápida e
eficiente entre diferentes máquinas transferindo somente as diferenças
entre estes diretórios de forma compactada. Ele não precisa que
nenhuma das máquinas tenha uma cópia do que está na outra.

Um relatório técnico descrevendo o algoritmo usado pelo rsync está
disponível neste pacote.

%description -l ru.UTF-8
rsync - это более быстрая и гибкая альтернатива rcp, позволяющая
быструю и эффективную по отношению к ресурсам сети синхронизацию
файлов или каталогов на различных машинах путем передачи только
различий между ними в компрессированном виде. При этом совершенно не
обязательно, чтобы одна машина имела у себя копию того, что есть на
другой машине.

%description -l uk.UTF-8
rsync - це швидша та гнучкіша альтернатива rcp, яка забезпечує швидку
та ефективну по відношенню до ресурсів мережі синхронізацію файлів чи
каталогів на різних машинах шляхом передачі лише відмінностей між ними
в компресованому виді. При цьому зовсім не обов'язково, щоб одна
машина мала в себе копію того, що є на іншій машині.

%package -n rsyncd-inetd
Summary:	Files necessary to run rsync in daemon mode
Summary(pl.UTF-8):	Pliki niezbędne do uruchomienia rsynca w trybie serwera
Group:		Networking/Daemons
Requires:	%{name} = %{version}-%{release}
Requires:	rc-inetd
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

%description -n rsyncd-inetd -l pl.UTF-8
Rsync jest zamiennikiem programu rcp z bardziej rozbudowaną składnią
poleceń. Program ten używa efektywnego algorytmu "rsync" w czasie
komunikacji i transportu plików do systemu zdalnego. Dokumentacja
techniczna nowego algorytmu została również dołączona do pakietu.

%package -n rsyncd-standalone
Summary:	Files necessary to run rsync in daemon mode
Summary(pl.UTF-8):	Pliki niezbędne do uruchomienia rsynca w trybie serwera
Group:		Networking/Daemons
Requires(post,preun):	/sbin/chkconfig
Requires:	%{name} = %{version}-%{release}
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

%description -n rsyncd-standalone -l pl.UTF-8
Rsync jest zamiennikiem programu rcp z bardziej rozbudowaną składnią
poleceń. Program ten używa efektywnego algorytmu "rsync" w czasie
komunikacji i transportu plików do systemu zdalnego. Dokumentacja
techniczna nowego algorytmu została również dołączona do pakietu.

%prep
%setup -q -b1
%patch0 -p1
%patch1 -p1

# for compat with previous patched version
patch -p1 -i patches/acls.diff || exit 1
patch -p1 -i patches/xattrs.diff || exit 1
patch -p1 < patches/openssl-support.diff || exit 1

%build
cp -f /usr/share/automake/config.sub .
%{__autoheader}
%{__autoconf}
%configure \
	LIBS="-lcrypto" \
	%{?with_rsh:--with-rsh=rsh} \
	--enable-ipv6 \
	--enable-acl-support \
	--enable-openssl \
	--enable-xattr-support \
	--disable-debug \
	--with-rsyncd-conf=%{_sysconfdir}/rsyncd.conf
%{__make} proto
%{__make}

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_sysconfdir},/etc/{sysconfig/rc-inetd,rc.d/init.d,logrotate.d,env.d},/var/log}

%{__make} install \
	prefix=$RPM_BUILD_ROOT%{_prefix} \
	mandir=$RPM_BUILD_ROOT%{_mandir} \
	bindir=$RPM_BUILD_ROOT%{_bindir}

:> $RPM_BUILD_ROOT/var/log/rsyncd.log
:> $RPM_BUILD_ROOT%{_sysconfdir}/rsyncd.secrets

cat << EOF > $RPM_BUILD_ROOT%{_sysconfdir}/rsyncd.conf
#log file = /var/log/rsyncd.log
EOF

cat << 'EOF' > $RPM_BUILD_ROOT/etc/env.d/CVSIGNORE
#CVSIGNORE=
EOF
cat << 'EOF' > $RPM_BUILD_ROOT/etc/env.d/RSYNC_RSH
#RSYNC_RSH=
EOF
cat << 'EOF' > $RPM_BUILD_ROOT/etc/env.d/RSYNC_PROXY
#RSYNC_PROXY=
EOF
cat << 'EOF' > $RPM_BUILD_ROOT/etc/env.d/RSYNC_PASSWORD
#RSYNC_PASSWORD=
EOF

install %{SOURCE2} $RPM_BUILD_ROOT/etc/sysconfig/rc-inetd/rsyncd
install %{SOURCE3} $RPM_BUILD_ROOT/etc/rc.d/init.d/rsyncd
install %{SOURCE4} $RPM_BUILD_ROOT/etc/sysconfig/rsyncd
install %{SOURCE5} $RPM_BUILD_ROOT/etc/logrotate.d/rsyncd

%clean
rm -rf $RPM_BUILD_ROOT

%post
%env_update

%postun
%env_update

%post -n rsyncd-inetd
%service -q rc-inetd reload

%postun -n rsyncd-inetd
if [ "$1" = "0" ]; then
	%service -q rc-inetd reload
fi

%post -n rsyncd-standalone
/sbin/chkconfig --add rsyncd
%service rsyncd restart "rsync server"

%preun -n rsyncd-standalone
if [ "$1" = "0" ]; then
	%service rsyncd stop
	/sbin/chkconfig --del rsyncd
fi

%files
%defattr(644,root,root,755)
%doc README NEWS OLDNEWS TODO
%config(noreplace,missingok) %verify(not md5 mtime size) /etc/env.d/*
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
