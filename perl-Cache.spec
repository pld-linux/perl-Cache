#
# Conditional build:
%bcond_without	tests		# do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define	pdir	Cache
Summary:	Cache - the cache interface
Summary(pl):	Cache - interfejs buforuj±cy
Name:		perl-Cache
Version:	2.02
Release:	1
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{version}.tar.gz
# Source0-md5:	47ba7a90a098048c540bb1626b240616
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
cached data in different manners (such as as files on a filesystem, or
in memory).

# %description -l pl
# TODO

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
