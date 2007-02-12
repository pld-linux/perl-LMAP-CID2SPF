#
# Conditional build:
%bcond_without	tests	# do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define		pdir	LMAP
%define		pnam	CID2SPF
Summary:	LMAP::CID2SPF - Caller-ID to SPF record Perl conversion module
Summary(pl.UTF-8):   LMAP::CID2SPF - moduł Perla do konwersji Caller-ID na rekord SPF
Name:		perl-LMAP-CID2SPF
Version:	0.9
Release:	1
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.baschny.de/spf/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	d0c31d773d840c859b582990137b0b5a
URL:		http://spf.pobox.com/
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
%if %{with tests}
BuildRequires:	perl-Test-Simple
BuildRequires:	perl-XML-Parser
%endif
Requires:	perl-XML-Parser
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This module may be used to convert Microsoft Caller-ID records to SPF
records.

%description -l pl.UTF-8
Ten moduł może być używany do konwersji rekordów Microsoft Caller-ID
na rekordy SPF.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

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
%doc README
%attr(755,root,root) %{_bindir}/*
%dir %{perl_vendorlib}/LMAP
%{perl_vendorlib}/LMAP/*.pm
%{_mandir}/man3/*
