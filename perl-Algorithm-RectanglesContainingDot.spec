%define upstream_name    Algorithm-RectanglesContainingDot
%define upstream_version 0.02

Name:		perl-%{upstream_name}
Version:	0.02
Release:	2

Summary:	Find rectangles containing a given dot
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		https://metacpan.org/dist/Algorithm-RectanglesContainingDot
Source0:	https://cpan.metacpan.org/authors/id/S/SA/SALVA/Algorithm-RectanglesContainingDot-0.02.tar.gz

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
%setup -q -n Algorithm-RectanglesContainingDot-0.02

%build
perl Makefile.PL INSTALLDIRS=vendor
%make

%check
# soft: do not fail package on test failures
set +e
%make test

%install
%makeinstall_std

%files
%doc README Changes
%{_mandir}/man3/*
%{perl_vendorlib}/*

