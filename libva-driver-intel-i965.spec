%define	libva_ver	2.4.0
Summary:	VA driver for Intel G45 and HD Graphics family older than Broadwell
Summary(pl.UTF-8):	Sterownik VA do kart Intela z rodziny G45 i HD Graphics starszych niż Broadwell
Name:		libva-driver-intel-i965
Version:	2.4.4
Release:	1
License:	MIT
Group:		Libraries
#Source0Download: https://github.com/irql-notlessorequal/intel-vaapi-driver/releases
Source0:	https://github.com/irql-notlessorequal/intel-vaapi-driver/archive/refs/tags/%{version}/intel-vaapi-driver-%{version}.tar.gz
# Source0-md5:	d5b76075800fc6220f265fdf29f2925c
URL:		https://01.org/linuxmedia
BuildRequires:	autoconf >= 2.57
BuildRequires:	automake >= 1:1.9
BuildRequires:	libdrm-devel >= 2.4.52
BuildRequires:	libva-devel >= %{libva_ver}
BuildRequires:	libva-drm-devel >= %{libva_ver}
BuildRequires:	libva-wayland-devel >= %{libva_ver}
BuildRequires:	libva-x11-devel >= %{libva_ver}
BuildRequires:	libtool
BuildRequires:	pkgconfig
# VA-API version, not just package version
BuildRequires:	pkgconfig(libva) >= 1.1.0
# wayland-client
BuildRequires:	wayland-devel >= 1.11.0
BuildRequires:	xorg-lib-libX11-devel
BuildRequires:	xorg-lib-libXext-devel
BuildRequires:	xorg-lib-libXfixes-devel
Requires:	libdrm >= 2.4.52
Requires:	libva >= %{libva_ver}
Requires:	wayland >= 1.11.0
Conflicts:	libva-driver-intel < 25.2.6
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
libva-driver-intel is the VA-API implementation for Intel G45 chipsets
and Intel HD Graphics for Intel Core processor family older than Broadwell.

Supported Platforms:

- G45 (CTG): Cantiga, Intel GMA 4500MHD (GM45)
- ILK (5.x): Ironlake, Intel HD Graphics for 2010 Intel Core processor family
- SNB (6.x): Sandybridge, Intel HD Graphics for 2011 Intel Core processor family
- IVB (7.0): Ivybridge
- HSW (7.5): Haswell
- CHV (8.0 LP): Cherryview/Braswell

also supported by the iHD driver (libva-driver-intel >= 25.2.6) which should be used
- BDW (8.0): Broadwell
- SKL (9.0): Skylake
- KBL (9.5): Kabylake

%description -l pl.UTF-8
libva-driver-intel to implementacja VA-API dla układów Intel G45 oraz
Intel HD Graphics przeznaczonych dla rodziny procesorów Intel Core starszych niż Broadwell.

Wspierane platformy:

- G45 (CTG): Cantiga, Intel GMA 4500MHD (GM45)
- ILK (5.x): Ironlake, Intel HD Graphics for 2010 Intel Core processor family
- SNB (6.x): Sandybridge, Intel HD Graphics for 2011 Intel Core processor family
- IVB (7.0): Ivybridge
- HSW (7.5): Haswell
- CHV (8.0 LP): Cherryview/Braswell

także wspierane przez iHD driver (libva-driver-intel >= 25.2.6), który powinien być używany
- BDW (8.0): Broadwell
- SKL (9.0): Skylake
- KBL (9.5): Kabylake

%prep
%setup -q -n intel-vaapi-driver-%{version}

%build
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
%configure \
	--enable-hybrid-codec \
	--disable-silent-rules

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%{__rm} $RPM_BUILD_ROOT%{_libdir}/libva/dri/*.la

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS NEWS README.md SECURITY.md
%attr(755,root,root) %{_libdir}/libva/dri/i965_drv_video.so
