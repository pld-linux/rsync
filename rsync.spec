#
# Conditional build:
%bcond_with	rsh	# set remote shell command to rsh instead of ssh (old behaviour)
%bcond_without	tests	# do not perform "make test"
#
%ifarch alpha
%undefine	with_tests
%endif
Summary:	Program for efficient remote updates of files
Summary(es):	Programa para actualizar archivos remotos de forma eficiente
Summary(ko):	��Ʈ��ũ�� ���� ���ϵ���ȭ�� ���� ���α׷�
Summary(pl):	Program do wydajnego zdalnego uaktualniania plik�w
Summary(pt_BR):	Programa para atualizar arquivos remotos de forma eficiente
Summary(ru):	��������� ��� ������������ ���������� ���������� ������
Summary(uk):	�������� ��� ����������� צ��������� ��������� ���̦�
Summary(zh_CN):	[ͨѶ]���乤��
Summary(zh_TW):	[���]$(B6G?i��(c(B
Name:		rsync
Version:	2.6.9
Release:	1
License:	GPL
Group:		Networking/Utilities
Source0:	http://rsync.samba.org/ftp/rsync/%{name}-%{version}.tar.gz
# Source0-md5:	996d8d8831dbca17910094e56dcb5942
Source1:	%{name}.inet
Source2:	%{name}.init
Source3:	%{name}.sysconfig
Source4:	%{name}d.logrotate
Patch0:		%{name}-config.patch
Patch1:		%{name}-man.patch
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

%description -l es
rsync es un substituto m�s r�pido y flexible para rcp que permite la
sincronizaci�n de archivos o directorios, v�a red, de forma r�pida y
eficiente, entre diferentes m�quinas transfiriendo solamente las
diferencias entre estos directorios de forma compactada. No necesita
que ninguna de las m�quinas tengan una copia de lo que est� en la
otra. Est� disponible en este paquete, una relaci�n t�cnica
describiendo el algoritmo usado por el rsync.

%description -l ko
Rsync�� ���� ȣ��Ʈ ������ �ſ� ���� ����ȭ�ϴµ� �ŷ��Ҹ���
�˰����� ����Ѵ�. Rsync�� ������ ��ü�� ������ �� ��ſ� ��Ʈ����
���� ������ �ٸ� �κи��� �����ϱ� ������ ������. Rsync�� ������ �̷�
���μ��� Ȥ�� rcp Ŀ��带 ���� �� ����� ��ü�����ν� ���ȴ�. rsync
�˰����� �����ϴ� ������� ������ �� �ٷ��̿� ���ԵǾ� �ִ�.

%description -l pl
Rsync jest zamiennikiem programu rcp z bardziej rozbudowan� sk�adni�
polece�. Program ten u�ywa efektywnego algorytmu "rsync" w czasie
komunikacji i transportu plik�w do systemu zdalnego. Dokumentacja
techniczna nowego algorytmu zosta�a r�wnie� do��czona do pakietu.

%description -l pt_BR
O rsync � um substituto mais r�pido e flex�vel para o rcp permitindo
sincroniza��o de arquivos ou diret�rios via rede de forma r�pida e
eficiente entre diferentes m�quinas transferindo somente as diferen�as
entre estes diret�rios de forma compactada. Ele n�o precisa que
nenhuma das m�quinas tenha uma c�pia do que est� na outra.

Um relat�rio t�cnico descrevendo o algoritmo usado pelo rsync est�
dispon�vel neste pacote.

%description -l ru
rsync - ��� ����� ������� � ������ ������������ rcp, �����������
������� � ����������� �� ��������� � �������� ���� �������������
������ ��� ��������� �� ��������� ������� ����� �������� ������
�������� ����� ���� � ����������������� ����. ��� ���� ���������� ��
�����������, ����� ���� ������ ����� � ���� ����� ����, ��� ���� ��
������ ������.

%description -l uk
rsync - �� ������ �� ����˦�� ������������ rcp, ��� ��������դ ������
�� ��������� �� צ�������� �� �����Ӧ� ����֦ ������Φ��æ� ���̦� ��
������Ǧ� �� Ҧ���� ������� ������ ������ަ ���� צ�ͦ������� ͦ� ����
� �������������� ��Ħ. ��� ����� ���Ӧ� �� ����'������, ��� ����
������ ���� � ���� ��Ц� ����, �� � �� ��ۦ� ����Φ.

%package -n rsyncd-inetd
Summary:	Files necessary to run rsync in daemon mode
Summary(pl):	Pliki niezb�dne do uruchomienia rsynca w trybie serwera
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

%description -n rsyncd-inetd -l pl
Rsync jest zamiennikiem programu rcp z bardziej rozbudowan� sk�adni�
polece�. Program ten u�ywa efektywnego algorytmu "rsync" w czasie
komunikacji i transportu plik�w do systemu zdalnego. Dokumentacja
techniczna nowego algorytmu zosta�a r�wnie� do��czona do pakietu.

%package -n rsyncd-standalone
Summary:	Files necessary to run rsync in daemon mode
Summary(pl):	Pliki niezb�dne do uruchomienia rsynca w trybie serwera
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

%description -n rsyncd-standalone -l pl
Rsync jest zamiennikiem programu rcp z bardziej rozbudowan� sk�adni�
polece�. Program ten u�ywa efektywnego algorytmu "rsync" w czasie
komunikacji i transportu plik�w do systemu zdalnego. Dokumentacja
techniczna nowego algorytmu zosta�a r�wnie� do��czona do pakietu.

%prep
%setup -q
patch -s -p1 < patches/acls.diff || exit 1
patch -s -p1 < patches/xattrs.diff || exit 1
%patch0 -p1
%patch1 -p1

%build
cp -f /usr/share/automake/config.sub .
%{__autoheader}
%{__autoconf}
%configure \
	%{?with_rsh:--with-rsh=rsh} \
	--enable-ipv6 \
	--enable-acl-support \
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
log file = /var/log/rsyncd.log
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

install %{SOURCE1} $RPM_BUILD_ROOT/etc/sysconfig/rc-inetd/rsyncd
install %{SOURCE2} $RPM_BUILD_ROOT/etc/rc.d/init.d/rsyncd
install %{SOURCE3} $RPM_BUILD_ROOT/etc/sysconfig/rsyncd
install %{SOURCE4} $RPM_BUILD_ROOT/etc/logrotate.d/rsyncd

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
