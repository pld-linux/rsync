Summary:	Program for efficient remote updates of files.
Summary(pl):	Program efektywnego modyfikowania plików na zdalnym komputerze.
Name:		rsync
Version:	2.3.2
Release:	2
Copyright:	GPL
Group:		Daemons
Group(pl):	Serwery
Source:		ftp://samba.anu.edu.au/pub/rsync/%{name}-%{version}.tar.gz
Patch0:		rsync-config.patch
Patch1:		rsync-man.patch
Patch2:		rsync-configure.patch
Patch3:		http://www.misiek.eu.org/ipv6/rsync-2.3.2-ipv6-13121999.patch.gz
URL:		http://samba.anu.edu.au/rsync/
BuildRoot:	/tmp/%{name}-%{version}-root

%define _sysconfdir /etc/rsyncd

%description
rsync is a replacement for rcp that has many more features.

rsync uses the "rsync algorithm" which provides a very fast method for
bringing remote files into sync. It does this by sending just the
differences in the files across the link, without requiring that both
sets of files are present at one of the ends of the link beforehand.

A technical report describing the rsync algorithm is included with
this package. 

%description -l pl
Rsync jest zamiennikiem programu rcp i jest bardziej rozbudowan± sk³adniê
poleceñ. Program ten u¿ywa efektywnego algorytmu "rsync" w czasie komunikacji 
i transportu plików do systemu zdalnego. Dokumentacja techniczna nowego 
algorytmu zosta³a równie¿ do³±czona do pakietu.

%prep
%setup  -q
%patch0 -p1
%patch1 -p1
%patch2 -p1
%patch3 -p1

%build
autoconf 
LDFLAGS="-s"; export LDFLAGS

%configure \
	--enable-ipv6

make 

%install
rm -rf $RPM_BUILD_ROOT

make install \
	prefix=$RPM_BUILD_ROOT%{_prefix} \
	mandir=$RPM_BUILD_ROOT%{_mandir} \
	bindir=$RPM_BUILD_ROOT%{_sbindir}

install -d $RPM_BUILD_ROOT/etc/rsyncd

:> $RPM_BUILD_ROOT/etc/rsyncd/rsyncd.conf
:> $RPM_BUILD_ROOT/etc/rsyncd/rsyncd.secrets

gzip -9nf $RPM_BUILD_ROOT%{_mandir}/man*/* README 

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README.gz 
%dir /etc/rsyncd
%attr(640,root,root) %config /etc/rsyncd/rsyncd.conf
%attr(640,root,root) %config /etc/rsyncd/rsyncd.secrets

%attr(755,root,root) %{_sbindir}/*
%{_mandir}/man[15]/*
