%define		gitver	%{nil}

Summary:	Free OpenGL implementation
Name:		Mesa
Version:	10.1.0
%if "%{gitver}" != "%{nil}"
Release:	0.%{gitver}.1
Source:		http://cgit.freedesktop.org/mesa/mesa/snapshot/mesa-%{gitver}.tar.bz2
%else
Release:	1
Source0:	ftp://ftp.freedesktop.org/pub/mesa/10.1/MesaLib-%{version}.tar.gz
# Source0-md5:	08e796ec7122aa299d32d4f67a254315
%endif
License:	MIT (core), SGI (GLU) and others - see COPYRIGHT file
Group:		X11/Libraries
URL:		http://www.mesa3d.org/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	expat-devel
BuildRequires:	libdrm-devel
BuildRequires:	libstdc++-devel
BuildRequires:	libtool
BuildRequires:	llvm-devel
BuildRequires:	xorg-libXdamage-devel
BuildRequires:	xorg-libXxf86vm-devel
BuildRequires:	xorg-libxshmfence-devel
BuildRequires:	xorg-proto >= 7.6
BuildRequires:	xorg-util-makedepend
Obsoletes:	Mesa-libdricore
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		dridir			%{_libdir}/xorg/modules/dri
%define		skip_post_check_so	libGL.so.1.*

%description
Mesa is a 3-D graphics library with an API which is very similar to
that of OpenGL(R). To the extent that Mesa utilizes the OpenGL command
syntax or state machine, it is being used with authorization from
Silicon Graphics, Inc. However, the author does not possess an OpenGL
license from SGI, and makes no claim that Mesa is in any way a
compatible replacement for OpenGL or associated with SGI.

%package libGL
Summary:	Free Mesa3D implementation of libGL OpenGL library
License:	MIT
Group:		X11/Libraries
Requires:	%{name}-libglapi = %{version}-%{release}
Provides:	OpenGL = 2.1
# reports version 1.3, but supports glXGetProcAddress() from 1.4
Provides:	OpenGL-GLX = 1.4

%description libGL
This package contains libGL which implements OpenGL 1.5 and GLX 1.4
specifications. It uses DRI for rendering.

%package libGL-devel
Summary:	Header files for Mesa3D libGL library
License:	MIT
Group:		X11/Development/Libraries
# loose dependency on libGL to use with other libGL binaries
Requires:	OpenGL >= 1.5
Requires:	xorg-libX11-devel
Provides:	OpenGL-devel = 2.1
Provides:	OpenGL-GLX-devel = 1.4

%description libGL-devel
Header files for Mesa3D libGL library.

%package libglapi
Summary:	GL API library
Group:		Libraries

%description libglapi
GL API library.

%package libXvMCsoftpipe
Summary:	XvMCsoftpipe library
Group:		Libraries

%description libXvMCsoftpipe
XvMCsoftpipe library.

%package dri-driver-intel-i915
Summary:	X.org DRI drivers
Group:		X11/Libraries
Requires:	xorg-driver-video-intel
Requires:	xorg-xserver-server

%description dri-driver-intel-i915
X.org DRI drivers for Intel i915 card family.

%package dri-driver-intel-i965
Summary:	X.org DRI drivers
Group:		X11/Libraries
Requires:	xorg-driver-video-intel
Requires:	xorg-xserver-server

%description dri-driver-intel-i965
X.org DRI drivers for Intel i965 card family.

%package dri-driver-swrast
Summary:	X.org DRI drivers
Group:		X11/Libraries
Requires:	xorg-xserver-server

%description dri-driver-swrast
X.org DRI software rasterizer driver.

%prep
%if "%{gitver}" != "%{nil}"
%setup -qn mesa-%{gitver}
%else
%setup -q
%endif

%build
%{__libtoolize}
%{__aclocal} -I m4
%{__autoconf}
%{__automake}
%configure \
	--disable-egl			\
	--disable-silent-rules		\
	--enable-dri3			\
	--enable-gallium-llvm		\
	--enable-glx-tls		\
	--enable-texture-float		\
	--enable-xa			\
	--with-dri-driverdir=%{dridir}	\
	--with-dri-drivers="i915,i965"	\
	--with-gallium-drivers="swrast"
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

# clean up
%{__rm} $RPM_BUILD_ROOT%{_includedir}/GL/{wglext,wmesa}.h
%{__rm} $RPM_BUILD_ROOT%{_libdir}/libglapi.so
%{__rm} $RPM_BUILD_ROOT%{_libdir}/lib*.la
%{__rm} $RPM_BUILD_ROOT%{dridir}/*.la

%if 0
%check
# 5 test failing
%{__make} check
%endif

%clean
rm -rf $RPM_BUILD_ROOT

%post	libGL -p /usr/sbin/ldconfig
%postun	libGL -p /usr/sbin/ldconfig

%post	libglapi -p /usr/sbin/ldconfig
%postun	libglapi -p /usr/sbin/ldconfig

%files libGL
%defattr(644,root,root,755)
%doc docs/{*.html,GL3.txt}
%attr(755,root,root) %ghost %{_libdir}/libGL.so.1
%attr(755,root,root) %{_libdir}/libGL.so.*.*
# symlink for binary apps which fail to conform Linux OpenGL ABI
# (and dlopen libGL.so instead of libGL.so.1)
%attr(755,root,root) %{_libdir}/libGL.so

%dir %{dridir}
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/drirc

%files libGL-devel
%defattr(644,root,root,755)
#%doc docs/*.spec
%dir %{_includedir}/GL
%dir %{_includedir}/GL/internal
%{_includedir}/GL/gl.h
%{_includedir}/GL/gl_mangle.h
%{_includedir}/GL/glext.h
%{_includedir}/GL/glx.h
%{_includedir}/GL/glx_mangle.h
%{_includedir}/GL/glxext.h
%{_includedir}/GL/internal/dri_interface.h
%{_pkgconfigdir}/dri.pc
%{_pkgconfigdir}/gl.pc

%files libglapi
%defattr(644,root,root,755)
%attr(755,root,root) %ghost %{_libdir}/libglapi.so.0
%attr(755,root,root) %{_libdir}/libglapi.so.*.*

%files dri-driver-intel-i915
%defattr(644,root,root,755)
%attr(755,root,root) %{dridir}/i915_dri.so

%files dri-driver-intel-i965
%defattr(644,root,root,755)
%attr(755,root,root) %{dridir}/i965_dri.so

%files dri-driver-swrast
%defattr(644,root,root,755)
%attr(755,root,root) %{dridir}/swrast_dri.so

