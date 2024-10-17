%define major   0
%define libepub %mklibname epub %{major}
%define devepub %mklibname epub -d

Summary:	Tools for accessing and converting various ebook file formats
Name:		ebook-tools
Version:	0.2.2
Release:	19
License:	MIT
Group:		Publishing
Url:		https://sourceforge.net/projects/ebook-tools
Source0:	%{name}-%{version}.tar.gz
# https://bugs.kde.org/show_bug.cgi?id=406116
# https://sourceforge.net/p/ebook-tools/bugs/8/
# https://bugsfiles.kde.org/attachment.cgi?id=119785
Patch0:		ebook-tools-fix-baloo-crash.patch
Patch1:		ebook-tools-0.1.1-libzip2.patch

BuildRequires:	cmake(ECM)
BuildRequires:	pkgconfig(libzip)
BuildRequires:	pkgconfig(libxml-2.0)
BuildRequires:	pkgconfig(zlib)
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
%autosetup -p1

%build
%cmake_kde5
%ninja_build

%install
%ninja_install -C build

%files
%{_bindir}/einfo
%{_bindir}/lit2epub

%files -n %{libepub}
%{_libdir}/libepub.so.%{major}*

%files -n %{devepub}
%{_includedir}/*.h
%{_libdir}/libepub.so
