#
# Conditional build:
%bcond_with	rsh	# set remote shell command to rsh instead of ssh (old behaviour)
%bcond_without	tests	# do not perform "make test"
#
Summary:	Program for efficient remote updates of files
Summary(es):	Programa para actualizar archivos remotos de forma eficiente
Summary(ko):	네트워크를 통한 파일동기화를 위한 프로그램
Summary(pl):	Program do wydajnego zdalnego uaktualniania plik�w
Summary(pt_BR):	Programa para atualizar arquivos remotos de forma eficiente
Summary(ru):	眺逑怒袴� 켈� 步팍客�肋逑� 臘죈턱卦하 苟卦隆턱�� 팁奸窘
Summary(uk):	眺逑怒皐 켈� 탬탸燉肋逑� 屢컴죈턱逑� 鷗窘謙鑛� 팁奸┹
Summary(zh_CN):	[繫祇]눈渴묏야
Summary(zh_TW):	[놉게]$(B6G?iㆅ(c(B
Name:		rsync
Version:	2.6.7
Release:	1
License:	GPL
Group:		Networking/Utilities
Source0:	http://rsync.samba.org/ftp/rsync/%{name}-%{version}.tar.gz
# Source0-md5:	fb51636c719e789244d5d4423cf157ac
Source1:	%{name}.inet
Source2:	%{name}.init
Source3:	%{name}.sysconfig
Source4:	%{name}d.logrotate
Patch0:		%{name}-config.patch
Patch1:		%{name}-man.patch
URL:		http://rsync.samba.org/
BuildRequires:	autoconf >= 2.52
BuildRequires:	automake
BuildRequires:	acl-devel
BuildRequires:	openssl-devel
BuildRequires:	popt-devel
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
Rsync는 원격 호스트 파일을 매우 빨리 동기화하는데 신뢰할만한
알고리즘을 사용한다. Rsync는 파일의 전체를 보내는 것 대신에 네트웍을
통해 파일의 다른 부분만을 전송하기 때문에 빠르다. Rsync는 강력한 미러
프로세스 혹은 rcp 커멘드를 통한 더 우수한 대체용으로써 사용된다. rsync
알고리즘을 묘사하는 기술적인 내용은 이 꾸러미에 포함되어 있다.

%description -l pl
Rsync jest zamiennikiem programu rcp z bardziej rozbudowan� sk쿪dni�
polece�. Program ten u퓓wa efektywnego algorytmu "rsync" w czasie
komunikacji i transportu plik�w do systemu zdalnego. Dokumentacja
techniczna nowego algorytmu zosta쿪 r�wnie� do낢czona do pakietu.

%description -l pt_BR
O rsync � um substituto mais r�pido e flex�vel para o rcp permitindo
sincroniza豫o de arquivos ou diret�rios via rede de forma r�pida e
eficiente entre diferentes m�quinas transferindo somente as diferen�as
entre estes diret�rios de forma compactada. Ele n�o precisa que
nenhuma das m�quinas tenha uma c�pia do que est� na outra.

Um relat�rio t�cnico descrevendo o algoritmo usado pelo rsync est�
dispon�vel neste pacote.

%description -l ru
rsync - 卜� 쫏謙� 쬔戇怒� � 핀쫀죙 죈茫텀适燉陸 rcp, 饉璞驅記北�
쬔戇論� � 步팍客�肋藍 饉 鞫卦北炚� � 瑙撞錄죌 膽燉 譚洸碌炚憫촁�
팁奸窘 �俓 個讀卿하� 适 怒蜜�奢謨 皐排适� 檎旽� 斤瑙컨司 冬景蓋
怒蜜�司� 考靈� 炚苽 � 蓋辜瑙幢�碌陸鑛鳩 慄컵. 眺� 卜鳩 遝淪膿턱卦 壙
苟拿죤턍忘�, 師苟� 謳适 皐排适 �考訣 � 膽쫓 蓋筋� 冬하, 師� 텁潼 适
켠朗銶 皐排壙.

%description -l uk
rsync - 쳔 伯�콕� 讀 핑良閘防 죈茫텀适燉陸 rcp, 麒� 憫쩨拍텡邏 伯�켄�
讀 탬탸燉肋� 饉 屢켑郡턱括 켓 瑙撞錄┹ 考瑙輦 譚洸碌過憫챈� 팁奸┹ 司
個讀卿푠� 适 娘剝�� 皐排适� 焙騎鳩 斤瑙컨誹 俓北 屢켐┧卦戇탱 稽� 炚苽
� 蓋辜瑙遝陸卦鼓 慄칡. 眺� 쵤鳩� 博綾┦ 壙 苟窘'拿蓋凜, 粉� 謳适
皐排适 皐訣 � 膽쩨 蓋揆� 冬하, 粉 � 适 ┧魃� 皐排過.

%package -n rsyncd-inetd
Summary:	Files necessary to run rsync in daemon mode
Summary(pl):	Pliki niezb�dne do uruchomienia rsynca w trybie serwera
Group:		Networking/Daemons
PreReq:		rc-inetd
Requires:	%{name} = %{version}-%{release}
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
Rsync jest zamiennikiem programu rcp z bardziej rozbudowan� sk쿪dni�
polece�. Program ten u퓓wa efektywnego algorytmu "rsync" w czasie
komunikacji i transportu plik�w do systemu zdalnego. Dokumentacja
techniczna nowego algorytmu zosta쿪 r�wnie� do낢czona do pakietu.

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
Rsync jest zamiennikiem programu rcp z bardziej rozbudowan� sk쿪dni�
polece�. Program ten u퓓wa efektywnego algorytmu "rsync" w czasie
komunikacji i transportu plik�w do systemu zdalnego. Dokumentacja
techniczna nowego algorytmu zosta쿪 r�wnie� do낢czona do pakietu.

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
