%define name vips
%define version 7.10.21
%define release %mkrel 6

%define lib_major 10
%define lib_name  %mklibname %{name} %{lib_major}
%define lib_name_orig lib%{name}

Summary: Image processing system
Name: %{name}
Version: %{version}
Release: %{release}
License: LGPL
Group: Video
URL: http://www.vips.ecs.soton.ac.uk/index.php
Source0: %{name}-%{version}.tar.bz2
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root
BuildRequires: glib2-devel 
BuildRequires: pango-devel
BuildRequires: png-devel
BuildRequires: jpeg-devel 
BuildRequires: tiff-devel
BuildRequires: fftw3-devel 
BuildRequires: zlib-devel 
BuildRequires: imagemagick-devel
BuildRequires: perl(XML::Parser)

%description
VIPS is a free image processing system. It aims to be about half-way between
Photoshop and Excel: it is very bad at retouching photographs, but very handy 
for the many other imaging tasks that programs like Photoshop get used for. 
It is good with large images (images larger than the amount of RAM in your 
machine), and for working with colour.

%files -f %{name}7.lang
%defattr(-,root,root,-)
%doc README COPYING AUTHORS NEWS TODO
%{_bindir}/*
%{_datadir}/%{name}

#--------------------------------------------------------------------

%package -n %{lib_name}
Summary:        Main library for vips
Group:          System/Libraries
Provides:       %{name} = %{version}-%{release}

%description -n %{lib_name}
This package contains the library needed to run programs dynamically
linked with vips.

%if %mdkversion < 200900
%post -n %{lib_name} -p /sbin/ldconfig
%endif
%if %mdkversion < 200900
%postun -n %{lib_name} -p /sbin/ldconfig
%endif

%files -n %{lib_name}
%defattr(-,root,root,-)
%{_libdir}/*.so.*

#--------------------------------------------------------------------

%package -n %{lib_name}-devel
Summary:        VIPS devel files
Group:          Development/Other
Provides:       %{lib_name_orig}-devel = %{version}-%{release}
Provides:       %{name}-devel = %{version}-%{release}
Requires:	%{lib_name} = %{version}
%define _requires_exceptions  devel\(libpathplan\)\\|devel\(libgvgd\)\\|devel\(libcdt\)\\|devel\(libgraph\)\\|devel\(libgvc\)

%description -n %{lib_name}-devel
This package contains the headers that programmers will need to develop
applications which will use vips.

%files -n %{lib_name}-devel
%defattr(-,root,root,-)
%{_libdir}/libvips*.so
%defattr(644,root,root,755)
%{_includedir}/*
%{_libdir}/libvips*.a
%{_libdir}/libvips*.la
%doc %{_defaultdocdir}/%{name}
%{_libdir}/pkgconfig/*
%{_mandir}/man?/*

#--------------------------------------------------------------------

%prep
%setup -q

%build
%configure
%make

%install
rm -rf $RPM_BUILD_ROOT
%makeinstall
rm -fr $RPM_BUILD_ROOT/%{_datadir}/locale/malkovich
%find_lang %{name}7

%clean
rm -rf $RPM_BUILD_ROOT


