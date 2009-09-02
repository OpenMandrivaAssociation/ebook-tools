Name:           ebook-tools
Summary:        Tools for accessing and converting various ebook file formats
Version:        0.1.1
Release:        %mkrel 2
Url:            http://sourceforge.net/projects/ebook-tools
License:        MIT
Group:          Publishing
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
Source0:        %{name}-%{version}.tar.gz
Patch0:         ebook-tools-0.1.1-fix-lib.patch
BuildRequires:  kde4-macros
BuildRequires:  libxml2-devel
BuildRequires:  libzip-devel

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

%if %mdkversion < 200900
%post -n %libepub -p /sbin/ldconfig
%endif
%if %mdkversion < 200900
%postun -n %libepub -p /sbin/ldconfig
%endif

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

%build
%cmake_kde4
%make

%install
cd build
make DESTDIR=%buildroot install

%clean
%{__rm} -rf "%{buildroot}"
