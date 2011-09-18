Name:           perl-DBD-SQLite
Version:        1.27
Release:        3%{?dist}
Summary:        Self Contained RDBMS in a DBI Driver

Group:          Development/Libraries
License:        GPL+ or Artistic
URL:            http://search.cpan.org/dist/DBD-SQLite/
Source0:        http://search.cpan.org/CPAN/authors/id/A/AD/ADAMK/DBD-SQLite-%{version}.tar.gz
Patch0:         perl-DBD-SQLite-bz543982.patch
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

# if sqlite >= 3.1.3 then
#   perl-DBD-SQLite uses the external library
# else
#   perl-DBD-SQLite is self-contained (uses the sqlite local copy)
BuildRequires:  sqlite-devel
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(Test::More) >= 0.42
BuildRequires:  perl(File::Spec) >= 0.82
# Prevent bug #443495
BuildRequires:  perl(DBI) >= 1.607

Requires:       perl(:MODULE_COMPAT_%(eval "`%{__perl} -V:version`"; echo $version))

%{?perl_default_filter}

%description
SQLite is a public domain RDBMS database engine that you can find at
http://www.hwaci.com/sw/sqlite/.

Rather than ask you to install SQLite first, because SQLite is public domain,
DBD::SQLite includes the entire thing in the distribution. So in order to get
a fast transaction capable RDBMS working for your perl project you simply have
to install this module, and nothing else.


%prep
%setup -q -n DBD-SQLite-%{version}
%patch0 -p1

%build
CFLAGS="$RPM_OPT_FLAGS" %{__perl} Makefile.PL INSTALLDIRS=vendor
make %{?_smp_mflags} OPTIMIZE="$RPM_OPT_FLAGS"


%install
rm -rf $RPM_BUILD_ROOT
make pure_install PERL_INSTALL_ROOT=$RPM_BUILD_ROOT
find $RPM_BUILD_ROOT -type f \( -name .packlist -o \
		-name '*.bs' -size 0 \) -exec rm -f {} ';'
find $RPM_BUILD_ROOT -depth -type d -empty -exec rmdir {} ';'
%{_fixperms} $RPM_BUILD_ROOT/*


%check
make test


%clean
rm -rf $RPM_BUILD_ROOT


%files
%defattr(-,root,root,-)
%doc Changes README
%{perl_vendorarch}/auto/*
%{perl_vendorarch}/DBD/
%{_mandir}/man3/*.3pm*


%changelog
* Mon Jan 11 2010 Marcela Mašláňová <mmaslano@redhat.com> - 1.27-3
- 543982 change Makefile.PL to compile with system sqlite
- Resolves: rhbz#543948

* Mon Dec  7 2009 Stepan Kasal <skasal@redhat.com> - 1.27-2
- rebuild against perl 5.10.1

* Wed Nov 25 2009 Stepan Kasal <skasal@redhat.com> 1.27-1
- new upstream version

* Fri Sep 11 2009 Chris Weyl <cweyl@alumni.drew.edu> - 1.25-4
- Filtering errant private provides

* Sat Jul 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.25-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Wed Jun 10 2009 Stepan Kasal <skasal@redhat.com> 1.25-2
- rebuild against DBI 1.609

* Fri May 29 2009 Chris Weyl <cweyl@alumni.drew.edu> 1.25-1
- 1.25 needed for DBIx::Class 0.08103
- auto-update to 1.25 (by cpan-spec-update 0.01)
- added a new br on perl(File::Spec) (version 0.82)
- altered br on perl(Test::More) (0 => 0.42)
- added a new br on perl(DBI) (version 1.57)

* Mon Apr 20 2009 Marcela Maslanova <mmaslano@redhat.com> 1.23-1
- update to the latest version

* Thu Feb 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.14-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Mon Jun  2 2008 Marcela Maslanova <mmaslano@redhat.com> 1.14-8

* Wed Mar 19 2008 Chris Weyl <cweyl@alumni.drew.edu> 1.14-7
- reenable tests

* Tue Mar 18 2008 Chris Weyl <cweyl@alumni.drew.edu> 1.14-6
- apply sanity patches derived from RT#32100

* Wed Feb 27 2008 Tom "spot" Callaway <tcallawa@redhat.com> - 1.14-5.1
- Rebuild for perl 5.10 (again)

* Tue Feb 19 2008 Fedora Release Engineering <rel-eng@fedoraproject.org> - 1.14-4.1
- Autorebuild for GCC 4.3

* Sun Jan 20 2008 Tom "spot" Callaway <tcallawa@redhat.com> 1.14-3.1
- tests disabled, due to x86_64 failures

* Tue Jan 15 2008 Tom "spot" Callaway <tcallawa@redhat.com> 1.14-3
- rebuild for new perl

* Wed Dec 19 2007 Steven Pritchard <steve@kspei.com> 1.14-2
- Fix find option order.
- Use fixperms macro instead of our own chmod incantation.

* Mon Dec 10 2007 Robin Norwood <rnorwood@redhat.com> - 1.14-1
- Update to latest upstream version: 1.14
- Remove patch - no longer needed.

* Mon Oct 15 2007 Tom "spot" Callaway <tcallawa@redhat.com> - 1.12-2.1
- correct license tag
- add BR: perl(ExtUtils::MakeMaker)

* Thu Sep 14 2006 Jose Pedro Oliveira <jpo at di.uminho.pt> - 1.12-2
- Rebuild for FC6.

* Tue Apr 11 2006 Jose Pedro Oliveira <jpo at di.uminho.pt> - 1.12-1
- Update to 1.12.

* Wed Apr  5 2006 Jose Pedro Oliveira <jpo at di.uminho.pt> - 1.11-4
- Patch to build with system sqlite 3.3.x (#183530).
- Patch to avoid type information segv (#187873).

* Thu Mar  9 2006 Jose Pedro Oliveira <jpo at di.uminho.pt> - 1.11-3
- DBD::SQLite fails to build with the current FC-5 sqlite version (3.3.3);
  see bugzilla entry #183530.
  Forcing package rebuild with the included version of sqlite (3.2.7).

* Sat Feb 18 2006 Jose Pedro Oliveira <jpo at di.uminho.pt> - 1.11-2
- Rebuild for FC5 (perl 5.8.8).

* Fri Dec  2 2005 Jose Pedro Oliveira <jpo at di.uminho.pt> - 1.11-1
- Update to 1.11.

* Fri Dec  2 2005 Jose Pedro Oliveira <jpo at di.uminho.pt> - 1.10-1
- Update to 1.10.

* Fri Jul 29 2005 Jose Pedro Oliveira <jpo at di.uminho.pt> - 1.09-2
- Build requirement added: sqlite-devel.
- Doc file added: Changes.

* Fri Jul 29 2005 Jose Pedro Oliveira <jpo at di.uminho.pt> - 1.09-1
- Update to 1.09.
- This new version can use an external SQLite library (>= 3.1.3).

* Sun Jun 12 2005 Jose Pedro Oliveira <jpo at di.uminho.pt> - 1.08-2
- temporary maintainership.

* Sat Jun 11 2005 Michael A. Peters <mpeters@mac.com> 1.08-1.1
- minor changes for initial cvs checkin (removed tabs, better url in
- url tag and description tag)

* Tue Apr 12 2005 Michael A. Peters <mpeters@mac.com> 1.08-1
- created initial spec file from Fedora spectemplate-perl.spec
