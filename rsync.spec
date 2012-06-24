Summary:	Program for efficient remote updates of files
Summary(es):	Programa para actualizar archivos remotos de forma eficiente
Summary(pl):	Program do wydajnego zdalnego uaktualniania plik�w
Summary(pt_BR):	Programa para atualizar arquivos remotos de forma eficiente
Summary(ru):	��������� ��� ������������ ���������� ���������� ������
Summary(uk):	�������� ��� ����������� צ��������� ��������� ���̦�
Name:		rsync
Version:	2.5.5
Release:	1
License:	GPL
Group:		Daemons
Source0:	http://rsync.samba.org/ftp/rsync/%{name}-%{version}.tar.gz
Source1:	%{name}.inet
Patch0:		%{name}-config.patch
Patch1:		%{name}-man.patch
BuildRequires:	autoconf
BuildRequires:	popt-devel
URL:		http://samba.anu.edu.au/rsync/
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

%description -l pl
Rsync jest zamiennikiem programu rcp z bardziej rozbudowan�
sk�adni� polece�. Program ten u�ywa efektywnego algorytmu "rsync" w
czasie komunikacji i transportu plik�w do systemu zdalnego.
Dokumentacja techniczna nowego algorytmu zosta�a r�wnie� do��czona do
pakietu.

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

%package -n rsyncd
Summary:	Files necessary to run rsync in daemon mode
Summary(pl):	Pliki niezb�dne do uruchomienia rsynca w trybie serwera
Group:		Daemons
Requires:	%{name}
Requires:	rc-inetd

%description -n rsyncd
rsync is a replacement for rcp that has many more features.

rsync uses the "rsync algorithm" which provides a very fast method for
bringing remote files into sync. It does this by sending just the
differences in the files across the link, without requiring that both
sets of files are present at one of the ends of the link beforehand.

A technical report describing the rsync algorithm is included with
this package.

%description -n rsyncd -l pl
Rsync jest zamiennikiem programu rcp z bardziej rozbudowan�
sk�adni� polece�. Program ten u�ywa efektywnego algorytmu "rsync" w
czasie komunikacji i transportu plik�w do systemu zdalnego.
Dokumentacja techniczna nowego algorytmu zosta�a r�wnie� do��czona do
pakietu.

%prep
%setup  -q
%patch0 -p1
%patch1 -p1

%build
autoconf
%configure \
	--enable-ipv6

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	prefix=$RPM_BUILD_ROOT%{_prefix} \
	mandir=$RPM_BUILD_ROOT%{_mandir} \
	bindir=$RPM_BUILD_ROOT%{_bindir}

install -d $RPM_BUILD_ROOT{%{_sysconfdir},/etc/sysconfig/rc-inetd}

:> $RPM_BUILD_ROOT%{_sysconfdir}/rsyncd.conf
:> $RPM_BUILD_ROOT%{_sysconfdir}/rsyncd.secrets

install %{SOURCE1} $RPM_BUILD_ROOT/etc/sysconfig/rc-inetd/rsyncd

gzip -9nf README

%post -n rsyncd
if [ -f /var/lock/subsys/rc-inetd ]; then
        /etc/rc.d/init.d/rc-inetd restart 1>&2
else
        echo "Type \"/etc/rc.d/init.d/rc-inetd start\" to start inet server" 1>&2
fi

%postun -n rsyncd
if [ "$1" = "0" -a -f /var/lock/subsys/rc-inetd ]; then
	/etc/rc.d/init.d/rc-inetd reload 1>&2
fi

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README.gz
%attr(755,root,root) %{_bindir}/*
%{_mandir}/man1/*

%files -n rsyncd
%defattr(644,root,root,755)
%dir %{_sysconfdir}
%attr(640,root,root) %config(noreplace) %{_sysconfdir}/rsyncd.conf
%attr(640,root,root) %config(noreplace) %{_sysconfdir}/rsyncd.secrets
%attr(640,root,root) /etc/sysconfig/rc-inetd/rsyncd
%{_mandir}/man5/*
