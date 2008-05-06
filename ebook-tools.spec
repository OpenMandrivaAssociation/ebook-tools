Name:           ebook-tools
Summary:        Tools for accessing and converting various ebook file formats
Version:        0.1.0
Release:        %mkrel 1
Url:            http://sourceforge.net/projects/ebook-tools
License:        MIT
Group:          Publishing
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
Source0:        %{name}-%{version}.tar.gz
Patch0:         ebook-tools-0.1.0-fix-lib.patch

%description
Tools for accessing and converting various ebook file formats

%files
%defattr(-,root,root)
%{_bindir}/einfo
%{_bindir}/lit2epub

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
%{_includedir}/*.h
%{_libdir}/libepub.so

#-----------------------------------------------------------------------------

%define libepub_major 0
%define libepub %mklibname epub %{libepub_major}

%package -n %libepub
Summary: KDE 4 library
Group: System/Libraries

%description -n %libepub
%name library.

%post -n %libepub -p /sbin/ldconfig
%postun -n %libepub -p /sbin/ldconfig

%files -n %libepub
%defattr(-,root,root)
%_kde_libdir/libepub.so.%{libepub_major}*

#--------------------------------------------------------------------


%prep
%setup -q 
%patch0 -p0

%build
%cmake_kde4
%make

%install
cd build
make DESTDIR=%buildroot install

%clean
%{__rm} -rf "%{buildroot}"
