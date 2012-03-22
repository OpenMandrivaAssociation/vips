%define major		15
%define libname		%mklibname %{name} %{major}
%define develname	%mklibname %{name} -d

Summary:	Image processing system
Name:		vips
Version:	7.28.2
Release:	1
License:	LGPLv2+
Group:		Video
URL:		http://www.vips.ecs.soton.ac.uk/index.php
Source0:	http://www.vips.ecs.soton.ac.uk/supported/current/%{name}-%{version}.tar.gz
BuildRequires:	glib2-devel 
BuildRequires:	pango-devel
BuildRequires:	png-devel
BuildRequires:	jpeg-devel 
BuildRequires:	tiff-devel
BuildRequires:	fftw3-devel 
BuildRequires:	zlib-devel 
BuildRequires:	OpenEXR-devel
BuildRequires:	lcms-devel
BuildRequires:	libexif-devel
BuildRequires:	oil-devel
BuildRequires:	graphicsmagick-devel
BuildRequires:	python-devel
BuildRequires:	swig
BuildRequires:	gtk-doc
BuildRequires:	perl(XML::Parser)
BuildRequires:	openslide-devel
BuildRequires:	matio-devel
BuildRequires:	cfitsio-devel
BuildRequires:	libv4l-devel

%description
VIPS is a free image processing system. It aims to be about half-way between
Photoshop and Excel: it is very bad at retouching photographs, but very handy 
for the many other imaging tasks that programs like Photoshop get used for. 
It is good with large images (images larger than the amount of RAM in your 
machine), and for working with color.

%package -n %{libname}
Summary:	Shared libraries for vips
Group:		System/Libraries

%description -n %{libname}
This package contains the library needed to run programs dynamically
linked with vips.

%package -n %{develname}
Summary:	Development headers and library for vips
Group:		Development/Other
Provides:	%{name}-devel = %{EVRD}
Requires:	%{libname} = %{version}
Obsoletes:	%{mklibname vips 10 -d}
%define _requires_exceptions  devel\(libpathplan\)\\|devel\(libgvgd\)\\|devel\(libcdt\)\\|devel\(libgraph\)\\|devel\(libgvc\)

%description -n %{develname}
This package contains the headers that programmers will need to develop
applications which will use vips.

%package -n python-%{name}
Summary:	Python support for the VIPS image processing library
Group:		Development/Python
Requires:	%{name} = %{version}-%{release}
%py_requires -d
%rename %{name}-python

%description -n python-%{name}
The %{name}-python package contains Python support for VIPS.

%prep
%setup -q

%build
# Build against GraphicsMagick: it's a better choice for this kind of
# usage, and anyway it works with underlinking protection,
# whereas ImageMagick does not - AdamW 2008/07
#./bootstrap.sh
%configure2_5x \
	--with-magickpackage=GraphicsMagick \
	--disable-static
%make

%install
%makeinstall_std

rm -fr %{buildroot}/%{_datadir}/locale/malkovich
%find_lang %{name}7

%files -f %{name}7.lang
%defattr(-,root,root,-)
#doc README AUTHORS NEWS TODO
%{_bindir}/*


%files -n %{libname}
%defattr(-,root,root,-)
%{_libdir}/*.so.%{major}*


%files -n %{develname}
%defattr(-,root,root,-)
%{_libdir}/libvips*.so
%defattr(644,root,root,755)
%{_includedir}/*
%doc %{_defaultdocdir}/%{name}
%{_libdir}/pkgconfig/*
%{_mandir}/man?/*
%{_datadir}/gtk-doc/html/libvips/


%files -n python-%{name}
%defattr(-,root,root,-)
%{python_sitearch}/vipsCC
