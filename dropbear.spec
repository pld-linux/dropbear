Summary:	Dropbear - a smallish ssh 2 server
Name:		dropbear
Version:	0.30
Release:	0.1
License:	GPL
Group:		Applications/Networking
Source0:	http://matt.ucc.asn.au/dropbear/%{name}-%{version}.tar.bz2
URL:		http://matt.ucc.asn.au/dropbear/dropbear.html
BuildRequires:	zlib-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This is dropbear, a smallish and friendly ssh2 daemon.

It is currently usable though betaish, requiring work in certain areas
before use in a production environment. If you need a small sshd to
run on a 4 meg laptop, then sure, use it now. But test it thoroughly
before using it somewhere important :)

%prep
%setup -q

%build
rm -f missing
%{__gettextize}
%{__aclocal}
%{__autoconf}
%{__autoheader}
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -D dropbear $RPM_BUILD_ROOT%{_sbindir}/dropbear
install dropbearkey $RPM_BUILD_ROOT%{_sbindir}/dropbearkey

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc CHANGES README
%attr(755,root,root) %{_sbindir}/*
