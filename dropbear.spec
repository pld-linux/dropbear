Summary:	Dropbear - a smallish ssh2 server
Summary(pl):	Dropbear - ma�y serwer ssh2
Name:		dropbear
Version:	0.48.1
Release:	0.1
License:	MIT
Group:		Applications/Networking
Source0:	http://matt.ucc.asn.au/dropbear/releases/%{name}-%{version}.tar.gz
# Source0-md5:	ca8e53a766faec831882831364568421
URL:		http://matt.ucc.asn.au/dropbear/dropbear.html
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	glib2-devel
BuildRequires:	intltool
BuildRequires:	zlib-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This is dropbear, a smallish and friendly ssh2 daemon.

It is currently usable though betaish, requiring work in certain areas
before use in a production environment. If you need a small sshd to
run on a 4 meg laptop, then sure, use it now. But test it thoroughly
before using it somewhere important :)

%description -l pl
To jest dropbear - ma�y i przyjazny demon ssh2.

Jest aktualnie u�ywalny, cho� jest w stanie beta, wymaga pracy w
niekt�rych obszarach przed u�yciem w produkcyjnym �rodowisku. Je�li
potrzebujemy ma�ego sshd do uruchomienia na laptopie z 4MB pami�ci,
mo�na u�ywa� go ju� teraz. Ale przed u�ywaniem do czego� wa�niejszego
trzeba go porz�dnie przetestowa� :)

%prep
%setup -q

%build
%{__glib_gettextize}
%{__intltoolize}
%{__aclocal}
%{__autoconf}
%{__autoheader}
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_mandir}/man8

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

install dropbear{,key}.* $RPM_BUILD_ROOT%{_mandir}/man8

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc CHANGES README SMALL TODO
%attr(755,root,root) %{_bindir}/*
%attr(755,root,root) %{_sbindir}/*
%{_mandir}/man8/*
