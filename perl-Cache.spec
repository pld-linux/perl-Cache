#
# Conditional build:
%bcond_without	tests		# do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define	pdir	Cache
Summary:	Cache - the cache interface
Summary(pl.UTF-8):	Cache - interfejs buforujący
Name:		perl-Cache
Version:	2.04
Release:	2
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{version}.tar.gz
# Source0-md5:	c64b8dd8f04e101bd20cde0c7c2e3d17
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
%if %{with tests}
BuildRequires:	perl(Date::Parse) >= 2.24
BuildRequires:	perl-DB_File >= 1.72
BuildRequires:	perl-Digest-SHA1 >= 2.01
BuildRequires:	perl-File-NFSLock >= 1.2
BuildRequires:	perl-Heap >= 0.01
BuildRequires:	perl-IO-String >= 1.02
BuildRequires:	perl-Storable >= 1
BuildRequires:	perl-Test-Simple >= 0.45
%endif
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The Cache modules are designed to assist a developer in persisting
data for a specified period of time. Often these modules are used in
web applications to store data locally to save repeated and redundant
expensive calls to remote machines or databases.

The Cache interface is implemented by derived classes that store
cached data in different manners (such as files on a filesystem, or in
memory).

%description -l pl.UTF-8
Moduły Cache są zaprojektowane, aby pomagać programistom w
przechowywaniu danych przez określony okres czasu. Zwykle moduły te są
używane w aplikacjach WWW do lokalnego przechowywania danych w celu
zaoszczędzenia powtarzających się i nadmiarowych drogich wywołań do
zdalnych maszyn lub baz danych.

Interfejs Cache jest zaimplementowany poprzez klasy dziedziczące
przechowujące buforowane dane na różne sposoby (np. w plikach albo w
pamięci).

%prep
%setup -q -n %{pdir}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make}

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes LICENSE README TODO
%{perl_vendorlib}/*.pm
%{perl_vendorlib}/Cache/*
%{_mandir}/man3/*
