Summary:	Program for efficient remote updates of files.
Summary(pl):	Program efektywnego modyfikowania plików na zdalnym komputerze.
Name:		rsync
Version:	2.3.1
Release:	1
Copyright:	GPL
Group:		Applications/Networking
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
CFLAGS="$RPM_OPT_FLAGS" LDFLAGS="-s" \
./configure \
	--prefix=/usr
make 

%install
rm -rf $RPM_BUILD_ROOT

make install prefix=$RPM_BUILD_ROOT/usr

strip $RPM_BUILD_ROOT/usr/bin/rsync

gzip -9nf $RPM_BUILD_ROOT/usr/man/man*/* \
	README

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README
%attr(755,root,root) /usr/bin/rsync
/usr/man/man[15]/*

%changelog
* Fri Mar 19 1999 Tomasz K³oczko <kloczek@rudy.mif.pg.gda.pl>
  [2.3.0-1]
- added gzipping man pages,
- removed man group from man pages.

* Sat Nov 08 1998 Wojtek ¦lusarczyk <wojtek@shadow.eu.org>
  [2.2.0-1d]
- translation modified for pl,
- minor changes.

* Fri Sep 18 1998 Tomasz K³oczko <kloczek@rudy.mif.pg.gda.pl>
  [2.1.1-1]
- added -q %setup parameter,
- changed Buildroot to /tmp/%%{name}-%%{version}-root,
- added using %%{name} and %%{version} in Source,
- added using $RPM_OPT_FLAGS during compile,
- added full %attr description in %files.

* Thu Jun 18 1998 Douglas N. Arnold <dna@math.psu.edu>
Upgrade to rsync version 2.0.18

* Sat May 16 1998 John H Terpstra <jht@aquasoft.com.au>
  Upgraded to Rsync 2.0.6
    -new feature anonymous rsync

* Mon Apr  6 1998 Douglas N. Arnold <dna@math.psu.edu>
Upgrade to rsync version 1.7.2.

* Sun Mar  1 1998 Douglas N. Arnold <dna@math.psu.edu>
Built 1.6.9-1 based on the 1.6.3-2 spec file of John A. Martin.
Changes from 1.6.3-2 packaging: added latex and dvips commands
to create tech_report.ps.

* Mon Aug 25 1997 John A. Martin <jam@jamux.com>
Built 1.6.3-2 after finding no rsync-1.6.3-1.src.rpm although there
was an ftp://ftp.redhat.com/pub/contrib/alpha/rsync-1.6.3-1.alpha.rpm
showing no packager nor signature but giving 
"Source RPM: rsync-1.6.3-1.src.rpm".

Changes from 1.6.2-1 packaging: added '$RPM_OPT_FLAGS' to make, strip
to '%build', removed '%prefix'.

* Thu Apr 10 1997 Michael De La Rue <miked@ed.ac.uk>
rsync-1.6.2-1 packaged.  (This entry by jam to credit Michael for the
previous package(s).)
