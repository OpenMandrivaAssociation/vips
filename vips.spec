%define major 37
%define libname %mklibname %{name} %{major}
%define libcc %mklibname %{name}CC %{major}
%define devname %mklibname %{name} -d
%define gimajor 8.0
%define girname %mklibname vips-gir %{gimajor}

Summary:	Image processing system
Name:		vips
Version:	7.38.1
Release:	1
License:	LGPLv2+
Group:		Video
Url:		http://www.vips.ecs.soton.ac.uk/index.php
Source0:	http://www.vips.ecs.soton.ac.uk/supported/current/%{name}-%{version}.tar.gz
BuildRequires:	gtk-doc
BuildRequires:	swig
BuildRequires:	jpeg-devel
BuildRequires:	perl(XML::Parser)
BuildRequires:	pkgconfig(cfitsio)
BuildRequires:	pkgconfig(fftw3)
BuildRequires:	pkgconfig(glib-2.0)
BuildRequires:	pkgconfig(gobject-introspection-1.0)
BuildRequires:	pkgconfig(GraphicsMagick)
BuildRequires:	pkgconfig(lcms)
BuildRequires:	pkgconfig(libexif)
BuildRequires:	pkgconfig(liboil-0.3)
BuildRequires:	pkgconfig(libpng)
BuildRequires:	pkgconfig(libtiff-4)
BuildRequires:	pkgconfig(libv4l1)
BuildRequires:	pkgconfig(matio)
BuildRequires:	pkgconfig(OpenEXR)
BuildRequires:	pkgconfig(openslide)
BuildRequires:	pkgconfig(orc-0.4)
BuildRequires:	pkgconfig(pango)
BuildRequires:	pkgconfig(pangoft2)
BuildRequires:	pkgconfig(python)
BuildRequires:	pkgconfig(zlib)

%description
VIPS is a free image processing system. It aims to be about half-way between
Photoshop and Excel: it is very bad at retouching photographs, but very handy 
for the many other imaging tasks that programs like Photoshop get used for. 
It is good with large images (images larger than the amount of RAM in your 
machine), and for working with color.

%files -f %{name}7.38.lang
%{_bindir}/*

#----------------------------------------------------------------------------

%package -n %{libname}
Summary:	Shared libraries for vips
Group:		System/Libraries

%description -n %{libname}
This package contains the library needed to run programs dynamically
linked with vips.

%files -n %{libname}
%{_libdir}/lib%{name}.so.%{major}*

#----------------------------------------------------------------------------

%package -n %{libcc}
Summary:	Shared libraries for vips
Group:		System/Libraries

%description -n %{libcc}
This package contains the library needed to run programs dynamically
linked with vips.

%files -n %{libcc}
%{_libdir}/lib%{name}CC.so.%{major}*

#----------------------------------------------------------------------------

%package -n %{girname}
Summary:	GObject Introspection interface description for %{name}
Group:		System/Libraries
Requires:	%{libname} = %{EVRD}
Requires:	%{libcc} = %{EVRD}

%description -n %{girname}
GObject Introspection interface description for %{name}.

%files -n %{girname}
%{_libdir}/girepository-1.0/Vips-%{gimajor}.typelib

#----------------------------------------------------------------------------

%package -n %{devname}
Summary:	Development headers and library for vips
Group:		Development/Other
Requires:	%{libname} = %{EVRD}
Requires:	%{libcc} = %{EVRD}
Requires:	%{girname} = %{EVRD}
Provides:	%{name}-devel = %{EVRD}

%description -n %{devname}
This package contains the headers that programmers will need to develop
applications which will use vips.

%files -n %{devname}
%{_libdir}/libvips*.so
%{_includedir}/*
%doc %{_defaultdocdir}/%{name}
%{_libdir}/pkgconfig/*
%{_mandir}/man?/*
%{_datadir}/gtk-doc/html/libvips/
%{_datadir}/gir-1.0/Vips-%{gimajor}.gir

#----------------------------------------------------------------------------

%package -n python-%{name}
Summary:	Python support for the VIPS image processing library
Group:		Development/Python
Requires:	%{name} = %{version}-%{release}
%rename %{name}-python

%description -n python-%{name}
The %{name}-python package contains Python support for VIPS.

%files -n python-%{name}
%{python_sitearch}/vipsCC

#----------------------------------------------------------------------------

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

%find_lang %{name}7.38

