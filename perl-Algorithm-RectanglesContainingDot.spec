%define upstream_name    Algorithm-RectanglesContainingDot
%define upstream_version 0.02

Name:		perl-%{upstream_name}
Version:	%{upstream_version}
Release:	6

Summary:	Find rectangles containing a given dot
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		https://metacpan.org/dist/Algorithm-RectanglesContainingDot
Source0:	https://cpan.metacpan.org/authors/id/S/SA/SALVA/Algorithm-RectanglesContainingDot-%{upstream_version}.tar.gz

BuildRequires:	make
BuildRequires:	perl-devel
BuildRequires:	perl(Test::More)
BuildArch:	noarch

%description
Given a set of rectangles and a set of dots, the algorithm implemented in
this modules finds for every dot, which rectangles contain it.

The algorithm complexity is O(R * log(R) * log(R) + D * log(R)) being R the
number of rectangles and D the number of dots.

Its usage is very simple:

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
perl Makefile.PL INSTALLDIRS=vendor
%make

%check
%make test

%install
%makeinstall_std

%files
%doc README Changes
%{_mandir}/man3/*
%{perl_vendorlib}/*

%changelog
* Sat Apr 16 2011 Funda Wang <fwang@mandriva.org> 0.20.0-2mdv2011.0
+ Revision: 653386
- rebuild for updated spec-helper

* Tue Sep 15 2009 Jérôme Quelin <jquelin@mandriva.org> 0.20.0-1mdv2011.0
+ Revision: 442852
- import perl-Algorithm-RectanglesContainingDot


* Tue Sep 15 2009 cpan2dist 0.02-1mdv
- initial mdv release, generated with cpan2dist
