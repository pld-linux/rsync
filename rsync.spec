Summary:	Program for efficient remote updates of files
Summary(pl.UTF-8):   Program efektywnego modyfikowania plików na zdalnym komputerze
Name:		rsync
Version:	2.5.0
Release:	0
License:	GPL
Group:		Daemons
Group(de):	Server
Group(pl):	Serwery
Source0:	http://rsync.samba.org/ftp/rsync/%{name}-%{version}.tar.gz
Source1:	%{name}.inet
Patch0:		%{name}-config.patch
Patch1:		%{name}-man.patch
Patch2:		%{name}-configure.patch
#Patch3:	http://www.misiek.eu.org/ipv6/%{name}-2.4.5-ipv6-20000821.patch.gz
Patch3:		%{name}-2.4.6-ipv6-20010419.patch.gz
BuildRequires:	autoconf
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

%description -l pl.UTF-8
Rsync jest zamiennikiem programu rcp i jest bardziej rozbudowaną
składnię poleceń. Program ten używa efektywnego algorytmu "rsync" w
czasie komunikacji i transportu plików do systemu zdalnego.
Dokumentacja techniczna nowego algorytmu została również dołączona do
pakietu.

%package -n rsyncd
Summary:	Files necessary to run rsync in daemon mode
Summary(pl.UTF-8):   Pliki niezbędne do uruchomienia rsynca w trybie serwera
Group:		Daemons
Group(de):	Server
Group(pl):	Serwery
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

%description -n rsyncd -l pl.UTF-8
Rsync jest zamiennikiem programu rcp i jest bardziej rozbudowaną
składnię poleceń. Program ten używa efektywnego algorytmu "rsync" w
czasie komunikacji i transportu plików do systemu zdalnego.
Dokumentacja techniczna nowego algorytmu została również dołączona do
pakietu.

%prep
%setup  -q
#%patch0 -p1
#%patch1 -p1
#%patch2 -p1
#%patch3 -p1

%build
autoconf 
%configure
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
