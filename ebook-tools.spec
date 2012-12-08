Name:           ebook-tools
Summary:        Tools for accessing and converting various ebook file formats
Version:        0.1.1
Release:        %mkrel 9
Url:            http://sourceforge.net/projects/ebook-tools
License:        MIT
Group:          Publishing
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
Source0:        %{name}-%{version}.tar.gz
Patch0:         ebook-tools-0.1.1-fix-lib.patch
Patch1:		ebook-tools-0.1.1-libzip2.patch
BuildRequires:  kde4-macros
BuildRequires:  libxml2-devel
BuildRequires:  libzip-devel
Suggests:       clit

%description
Tools for accessing and converting various ebook file formats

%files
%defattr(-,root,root)
%{_kde_bindir}/einfo
%{_kde_bindir}/lit2epub

#-----------------------------------------------------------------------------

%define libepub_major 0
%define libepub %mklibname epub %{libepub_major}

%package -n %libepub
Summary: KDE 4 library
Group: System/Libraries

%description -n %libepub
%name library.

%files -n %libepub
%defattr(-,root,root)
%_kde_libdir/libepub.so.%{libepub_major}*

#--------------------------------------------------------------------
%package devel
Summary: Devel stuff for %name
Group: Development/KDE and Qt
Requires:  %libepub = %version-%release

%description  devel
This package contains header files needed if you wish to build applications
based on %name

%files devel
%defattr(-,root,root)
%{_kde_includedir}/*.h
%{_kde_libdir}/libepub.so

#-----------------------------------------------------------------------------

%prep
%setup -q 
%patch0 -p1 -b .fix-lib
%patch1 -p0 -b .zip

%build
%cmake_kde4
%make

%install
cd build
make DESTDIR=%buildroot install

%clean
%{__rm} -rf "%{buildroot}"


%changelog
* Tue May 03 2011 Funda Wang <fwang@mandriva.org> 0.1.1-7mdv2011.0
+ Revision: 664577
- build with latest zip

  + Oden Eriksson <oeriksson@mandriva.com>
    - mass rebuild
    - rebuilt against libzip.so.2

* Thu Dec 02 2010 Oden Eriksson <oeriksson@mandriva.com> 0.1.1-5mdv2011.0
+ Revision: 605093
- rebuild

  + Ahmad Samir <ahmadsamir@mandriva.org>
    - suggest clit, ebook-tools uses it, but it's not in the official repos, so a
      suggests.

* Tue Mar 16 2010 Oden Eriksson <oeriksson@mandriva.com> 0.1.1-3mdv2010.1
+ Revision: 522569
- rebuilt for 2010.1

* Wed Sep 02 2009 Christophe Fergeau <cfergeau@mandriva.com> 0.1.1-2mdv2010.0
+ Revision: 424376
- rebuild

* Sun Mar 22 2009 Herton Ronaldo Krzesinski <herton@mandriva.com.br> 0.1.1-1mdv2009.1
+ Revision: 360533
- Updated to version 0.1.1
- Rediffed fix-lib patch.

  + Thierry Vignaud <tv@mandriva.org>
    - rebuild early 2009.0 package (before pixel changes)

* Thu Jun 12 2008 Helio Chissini de Castro <helio@mandriva.com> 0.1.0-2mdv2009.0
+ Revision: 218529
- Is a kde4 app

  + Pixel <pixel@mandriva.com>
    - do not call ldconfig in %%post/%%postun, it is now handled by filetriggers

* Tue May 06 2008 Nicolas Lécureuil <nlecureuil@mandriva.com> 0.1.0-1mdv2009.0
+ Revision: 202232
- Fix buildRequires
- Fix subpackage order
- Fix Requires
  Add Group
- import ebook-tools


