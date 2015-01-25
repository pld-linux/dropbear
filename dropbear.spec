# TODO
# - enable pam, see also https://bugs.debian.org/cgi-bin/bugreport.cgi?bug=533525 (1-2 solvable, 3 needs code)
#
# Conditional build:
%bcond_with	pam		# PAM authentication support

Summary:	Dropbear - a smallish ssh2 server
Summary(pl.UTF-8):	Dropbear - mały serwer ssh2
Name:		dropbear
Version:	0.53
Release:	0.1
License:	MIT
Group:		Applications/Networking
Source0:	http://matt.ucc.asn.au/dropbear/releases/%{name}-%{version}.tar.bz2
# Source0-md5:	b6df80b05b6b7d03f6b232917b677d5d
URL:		http://matt.ucc.asn.au/dropbear/dropbear.html
BuildRequires:	autoconf >= 2.50
BuildRequires:	automake
BuildRequires:	zlib-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This is dropbear, a smallish and friendly ssh2 daemon.

It is currently usable though betaish, requiring work in certain areas
before use in a production environment. If you need a small sshd to
run on a 4 meg laptop, then sure, use it now. But test it thoroughly
before using it somewhere important :)

%description -l pl.UTF-8
To jest dropbear - mały i przyjazny demon ssh2.

Jest aktualnie używalny, choć jest w stanie beta, wymaga pracy w
niektórych obszarach przed użyciem w produkcyjnym środowisku. Jeśli
potrzebujemy małego sshd do uruchomienia na laptopie z 4MB pamięci,
można używać go już teraz. Ale przed używaniem do czegoś ważniejszego
trzeba go porządnie przetestować :)

%prep
%setup -q

%build
%{__aclocal}
%{__autoconf}
%{__autoheader}
%configure \
	%{?with_pam:--enable-pam}
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_mandir}/man8
%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

cp -p dropbear{,key}.8 $RPM_BUILD_ROOT%{_mandir}/man8

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc CHANGES README SMALL TODO
%attr(755,root,root) %{_bindir}/dbclient
%attr(755,root,root) %{_bindir}/dropbearconvert
%attr(755,root,root) %{_bindir}/dropbearkey
%attr(755,root,root) %{_sbindir}/dropbear
%{_mandir}/man8/dropbear.8*
%{_mandir}/man8/dropbearkey.8*
