%define major   0
%define libepub %mklibname epub %{major}
%define devepub %mklibname epub -d

Summary:	Tools for accessing and converting various ebook file formats
Name:		ebook-tools
Version:	0.2.2
Release:	12
License:	MIT
Group:		Publishing
Url:		http://sourceforge.net/projects/ebook-tools
Source0:	%{name}-%{version}.tar.gz
Patch1:		ebook-tools-0.1.1-libzip2.patch

BuildRequires:	kde4-macros
BuildRequires:	libzip-devel
BuildRequires:	pkgconfig(libxml-2.0)
Suggests:	clit

%description
Tools for accessing and converting various ebook file formats

%package -n %{libepub}
Summary:	KDE shared library
Group:		System/Libraries

%description -n %{libepub}
%{name} library.

%package -n %{devepub}
Summary:	Devel stuff for %{name}
Group:		Development/KDE and Qt
Requires:	%{libepub} = %{version}-%{release}
Provides:	%{name}-devel = %{version}-%{release}
Obsoletes:	ebook-tools-devel < 0.2.1-2

%description -n %{devepub}
This package contains header files needed if you wish to build applications
based on %{name}

%prep
%setup -q
%apply_patches

%build
%cmake_kde4
%make

%install
%makeinstall_std -C build

%files
%{_kde_bindir}/einfo
%{_kde_bindir}/lit2epub

%files -n %{libepub}
%{_kde_libdir}/libepub.so.%{major}*

%files -n %{devepub}
%{_kde_includedir}/*.h
%{_kde_libdir}/libepub.so

