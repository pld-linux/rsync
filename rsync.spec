Summary:	Program for efficient remote updates of files.
Summary(pl):	Program efektywnego modyfikowania plików na zdalnym komputerze.
Name:		rsync
Version:	2.3.1
Release:	3
Copyright:	GPL
Group:		Applications/Networking
Group(pl):	Aplikacje/Sieciowe
Source:		ftp://samba.anu.edu.au/pub/rsync/%{name}-%{version}.tar.gz
URL:		http://samba.anu.edu.au/rsync/
BuildRoot:	/tmp/%{name}-%{version}-root

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
%setup -q

%build
autoconf
CFLAGS="$RPM_OPT_FLAGS" LDFLAGS="-s" \
./configure %{_target_platform} \
	--prefix=%{_prefix}
make 

%install
rm -rf $RPM_BUILD_ROOT

make install prefix=$RPM_BUILD_ROOT/usr

strip $RPM_BUILD_ROOT%{_bindir}/rsync

gzip -9nf $RPM_BUILD_ROOT%{_mandir}/man*/* \
	README

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README
%attr(755,root,root) %{_bindir}/rsync
%{_mandir}/man[15]/*

%changelog
* Wed Jun  9 1999 Tomasz K³oczko <kloczek@rudy.mif.pg.gda.pl>
  [2.3.1-3]
- based on spec from RH contrib (witten by Douglas N. Arnold
  <dna@math.psu.edu>),
- pl translation by Wojtek ¦lusarczyk <wojtek@shadow.eu.org>,
- spec rewrited by PLD team.
