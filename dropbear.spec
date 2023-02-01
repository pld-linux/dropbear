# TODO
# - enable pam, see also https://bugs.debian.org/cgi-bin/bugreport.cgi?bug=533525 (1-2 solvable, 3 needs code)
#
# Conditional build:
%bcond_with	pam		# PAM authentication support (most likely incomplete)
%bcond_without	system_libtom	# use system libtommath/libtomcrypt

Summary:	Dropbear - a smallish ssh2 server
Summary(pl.UTF-8):	Dropbear - mały serwer ssh2
Name:		dropbear
Version:	2018.76
Release:	2
License:	MIT and BSD
Group:		Applications/Networking
Source0:	https://matt.ucc.asn.au/dropbear/releases/%{name}-%{version}.tar.bz2
# Source0-md5:	c3912f7fcdcc57c99937e4a79480d2c2
URL:		https://matt.ucc.asn.au/dropbear/dropbear.html
BuildRequires:	autoconf >= 2.59
BuildRequires:	automake
%{?with_system_libtom:BuildRequires:	libtomcrypt-devel >= 1.17-2}
%{?with_pam:BuildRequires:     pam-devel}
BuildRequires:	zlib-devel
%{?with_system_libtom:Requires:	libtomcrypt >= 1.17-2}
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

%{?with_system_libtom:rm -r libtomcrypt libtommath}

%build
%{__aclocal}
%{__autoconf}
%{__autoheader}
export OLDCFLAGS=set # hack for configure to respect our optflags
%configure \
	%{__enable_disable_not system_libtom bundled-libtom} \
	%{?with_pam:--enable-pam}
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_sysconfdir}/%{name}
%{__make} install \
	INSTALL="install -p" \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc CHANGES LICENSE README SMALL
%{_sysconfdir}/%{name}
%attr(755,root,root) %{_bindir}/dbclient
%attr(755,root,root) %{_bindir}/dropbearconvert
%attr(755,root,root) %{_bindir}/dropbearkey
%attr(755,root,root) %{_sbindir}/dropbear
%{_mandir}/man1/dbclient.1*
%{_mandir}/man1/dropbearconvert.1*
%{_mandir}/man1/dropbearkey.1*
%{_mandir}/man8/dropbear.8*
