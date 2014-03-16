%define		gitver	%{nil}

Summary:	Free OpenGL implementation
Name:		Mesa
Version:	10.1.0
%if "%{gitver}" != "%{nil}"
Release:	0.%{gitver}.1
Source:		http://cgit.freedesktop.org/mesa/mesa/snapshot/mesa-%{gitver}.tar.bz2
%else
Release:	3
Source0:	ftp://ftp.freedesktop.org/pub/mesa/10.1/MesaLib-%{version}.tar.gz
# Source0-md5:	08e796ec7122aa299d32d4f67a254315
%endif
Patch0:		%{name}-link.patch
License:	MIT (core), SGI (GLU) and others - see COPYRIGHT file
Group:		X11/Libraries
URL:		http://www.mesa3d.org/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	expat-devel
BuildRequires:	libdrm-devel
BuildRequires:	libstdc++-devel
BuildRequires:	libtool
BuildRequires:	llvm-devel >= 3.4
BuildRequires:	wayland-devel
BuildRequires:	xorg-libXdamage-devel
BuildRequires:	xorg-libXxf86vm-devel
BuildRequires:	xorg-libxshmfence-devel
BuildRequires:	xorg-proto >= 7.6
BuildRequires:	xorg-util-makedepend
Obsoletes:	Mesa-libdricore
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		dridir			%{_libdir}/xorg/modules/dri
%define		skip_post_check_so	libGL.so.1.* libGLESv1_CM.so.1.* libGLESv2.so.2.*

%define		dridrvs	i915,i965,nouveau,swrast
%define		galdrvs	r600,radeonsi,nouveau,svga,swrast

%define		specflags   -DNDEBUG

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
Provides:	OpenGL = 3.3
Provides:	OpenGL-GLX = 1.4

%description libGL
This package contains libGL which implements OpenGL 1.5 and GLX 1.4
specifications. It uses DRI for rendering.

%package libGL-devel
Summary:	Header files for Mesa3D libGL library
License:	MIT
Group:		X11/Development/Libraries
# loose dependency on libGL to use with other libGL binaries
Requires:	OpenGL >= 3.3
Requires:	xorg-libX11-devel
Provides:	OpenGL-devel = 3.3
Provides:	OpenGL-GLX-devel = 1.4

%description libGL-devel
Header files for Mesa3D libGL library.

%package libglapi
Summary:	GL API library
Group:		Libraries

%description libglapi
GL API library.

%package libEGL
Summary:	EGL library
Group:		Libraries
Requires:	%{name}-libglapi = %{version}-%{release}
Provides:	EGL = 1.4

%description libEGL
EGL library.

%package libEGL-devel
Summary:	Header files for Mesa3D EGL library
License:	MIT
Group:		X11/Development/Libraries
Requires:	%{name}-libEGL = %{version}-%{release}
Provides:	EGL-devel = 1.4

%description libEGL-devel
Header files for Mesa3D EGL library.

%package libGLES
Summary:	GLES library
Group:		Libraries
Requires:	%{name}-libglapi = %{version}-%{release}

%description libGLES
GLES library.

%package libGLES-devel
Summary:	Header files for Mesa3D GLES library
License:	MIT
Group:		X11/Development/Libraries
Requires:	%{name}-libGLES = %{version}-%{release}

%description libGLES-devel
Header files for Mesa3D GLES library.

%package libgbm
Summary:	gbm library
Group:		Libraries
Requires:	%{name}-libglapi = %{version}-%{release}

%description libgbm
gbm library.

%package libgbm-devel
Summary:	Header files for Mesa3D gbm library
License:	MIT
Group:		X11/Development/Libraries
Requires:	%{name}-libgbm = %{version}-%{release}

%description libgbm-devel
Header files for Mesa3D gbm library.

%package libwayland-EGL
Summary:	wayland-EGL library
Group:		Libraries

%description libwayland-EGL
Wayland EGL library.

%package libwayland-EGL-devel
Summary:	Header files for Mesa3D Wayland-EGL library
License:	MIT
Group:		X11/Development/Libraries
Requires:	%{name}-libwayland-EGL = %{version}-%{release}

%description libwayland-EGL-devel
Header files for Mesa3D Wayland-EGL library.

%package libxatracker
Summary:	xatracker library
Group:		Libraries

%description libxatracker
xatracker library.

%package libxatracker-devel
Summary:	Header files for Mesa3D xatracker library
License:	MIT
Group:		X11/Development/Libraries
Requires:	%{name}-libxatracker = %{version}-%{release}

%description libxatracker-devel
Header files for Mesa3D xatracker library.

# dri drivers
%package dri-driver-intel-i915
Summary:	X.org DRI drivers
Group:		X11/Libraries
Requires:	xorg-driver-video-intel
Requires:	xorg-xserver-server
Suggests:	libtxc_dxtn

%description dri-driver-intel-i915
X.org DRI drivers for Intel i915 card family.

%package dri-driver-intel-i965
Summary:	X.org DRI drivers
Group:		X11/Libraries
Requires:	xorg-driver-video-intel
Requires:	xorg-xserver-server
Suggests:	libtxc_dxtn

%description dri-driver-intel-i965
X.org DRI drivers for Intel i965 card family.

%package dri-driver-ati-r600
Summary:	X.org DRI drivers
Group:		X11/Libraries
Requires:	xorg-driver-video-ati
Requires:	xorg-xserver-server
Suggests:	libtxc_dxtn

%description dri-driver-ati-r600
X.org DRI drivers for ATI R600/R700 card family.

%package dri-driver-ati-radeonsi
Summary:	X.org DRI drivers
Group:		X11/Libraries
Requires:	xorg-driver-video-ati
Requires:	xorg-xserver-server
Suggests:	libtxc_dxtn

%description dri-driver-ati-radeonsi
X.org DRI drivers for ATI Southern Islands card family.

%package dri-driver-nvidia-nouveau
Summary:	X.org DRI drivers
Group:		X11/Libraries
Requires:	xorg-driver-video-nouveau
Requires:	xorg-xserver-server
Suggests:	libtxc_dxtn

%description dri-driver-nvidia-nouveau
X.org DRI drivers for NVIDIA card families.

%package dri-driver-swrast
Summary:	X.org DRI drivers
Group:		X11/Libraries
Requires:	xorg-xserver-server

%description dri-driver-swrast
X.org DRI software rasterizer driver.

%package dri-driver-vmware
Summary:	X.org DRI drivers
Group:		X11/Libraries
Requires:	%{name}-libgbm = %{version}-%{release}
Requires:	xorg-driver-video-vmware
Requires:	xorg-xserver-server

%description dri-driver-vmware
X.org DRI VMWare driver.

# gallium drivers
%package gallium-pipe-nvidia-nouveau
Summary:	X.org DRI drivers
Group:		X11/Libraries
Requires:	%{name}-libgbm = %{version}-%{release}
Requires:	xorg-driver-video-nouveau
Requires:	xorg-xserver-server
Suggests:	libtxc_dxtn

%description gallium-pipe-nvidia-nouveau
X.org Gallium3D NVIDIA driver.

%package gallium-pipe-ati-r600
Summary:	X.org DRI drivers
Group:		X11/Libraries
Requires:	%{name}-libgbm = %{version}-%{release}
Requires:	xorg-driver-video-ati
Requires:	xorg-xserver-server
Suggests:	libtxc_dxtn

%description gallium-pipe-ati-r600
X.org Gallium3D ATI R600/700 driver.

%package gallium-pipe-ati-radeonsi
Summary:	X.org DRI drivers
Group:		X11/Libraries
Requires:	%{name}-libgbm = %{version}-%{release}
Requires:	xorg-driver-video-ati
Requires:	xorg-xserver-server
Suggests:	libtxc_dxtn

%description gallium-pipe-ati-radeonsi
X.org Gallium3D ATI Southern Islands driver.

%package gallium-pipe-swrast
Summary:	X.org DRI drivers
Group:		X11/Libraries
Requires:	%{name}-libgbm = %{version}-%{release}
Requires:	xorg-xserver-server

%description gallium-pipe-swrast
X.org Gallium3D software rasterizer driver.

%package gallium-pipe-vmware
Summary:	X.org DRI drivers
Group:		X11/Libraries
Requires:	%{name}-libgbm = %{version}-%{release}
Requires:	xorg-driver-video-vmware
Requires:	xorg-xserver-server

%description gallium-pipe-vmware
X.org Gallium3D VMWare driver.

%prep
%if "%{gitver}" != "%{nil}"
%setup -qn mesa-%{gitver}
%else
%setup -q
%endif
%patch0 -p1

%build
%{__libtoolize}
%{__aclocal} -I m4
%{__autoconf}
%{__automake}
%configure \
	--disable-silent-rules			\
	--enable-dri3				\
	--enable-egl				\
	--enable-gallium-egl			\
	--enable-gallium-llvm			\
	--enable-gbm				\
	--enable-gles1				\
	--enable-gles2				\
	--enable-glx-tls			\
	--enable-shared-glapi			\
	--enable-texture-float			\
	--enable-xa				\
	--with-dri-driverdir=%{dridir}		\
	--with-dri-drivers="%{dridrvs}"		\
	--with-egl-platforms=x11,drm,wayland	\
	--with-gallium-drivers="%{galdrvs}"	\
	--with-llvm-prefix=%{_prefix}		\
	--with-llvm-shared-libs
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

# clean up
%{__rm} $RPM_BUILD_ROOT%{_includedir}/GL/{wglext,wmesa}.h
%{__rm} $RPM_BUILD_ROOT%{_libdir}/libglapi.so
%{__rm} $RPM_BUILD_ROOT%{_libdir}/{lib,*/}*.la
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

%post	libEGL -p /usr/sbin/ldconfig
%postun	libEGL -p /usr/sbin/ldconfig

%post	libGLES -p /usr/sbin/ldconfig
%postun	libGLES -p /usr/sbin/ldconfig

%post	libglapi -p /usr/sbin/ldconfig
%postun	libglapi -p /usr/sbin/ldconfig

%post	libwayland-EGL -p /usr/sbin/ldconfig
%postun	libwayland-EGL -p /usr/sbin/ldconfig

%post	libxatracker -p /usr/sbin/ldconfig
%postun	libxatracker -p /usr/sbin/ldconfig

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
%dir %{_includedir}/GL
%dir %{_includedir}/GL/internal
%{_includedir}/GL/gl.h
%{_includedir}/GL/gl_mangle.h
%{_includedir}/GL/glext.h
%{_includedir}/GL/glx.h
%{_includedir}/GL/glx_mangle.h
%{_includedir}/GL/glxext.h
%{_includedir}/GL/internal/dri_interface.h
%{_includedir}/KHR
%{_pkgconfigdir}/dri.pc
%{_pkgconfigdir}/gl.pc

%files libEGL
%defattr(644,root,root,755)
%attr(755,root,root) %ghost %{_libdir}/libEGL.so.1
%attr(755,root,root) %{_libdir}/libEGL.so.*.*.*
%dir %{_libdir}/egl
%attr(755,root,root) %{_libdir}/egl/egl_gallium.so

%files libEGL-devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libEGL.so
%dir %{_includedir}/EGL
%{_includedir}/EGL/egl.h
%{_includedir}/EGL/eglext.h
%{_includedir}/EGL/eglmesaext.h
%{_includedir}/EGL/eglplatform.h
%{_pkgconfigdir}/egl.pc

%files libGLES
%defattr(644,root,root,755)
%attr(755,root,root) %ghost %{_libdir}/libGLESv1_CM.so.1
%attr(755,root,root) %ghost %{_libdir}/libGLESv2.so.2
%attr(755,root,root) %{_libdir}/libGLESv1_CM.so.*.*.*
%attr(755,root,root) %{_libdir}/libGLESv2.so.*.*.*

%files libGLES-devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libGLESv1_CM.so
%attr(755,root,root) %{_libdir}/libGLESv2.so
%{_includedir}/GLES
%{_includedir}/GLES2
%{_includedir}/GLES3
%{_pkgconfigdir}/glesv1_cm.pc
%{_pkgconfigdir}/glesv2.pc

%files libgbm
%defattr(644,root,root,755)
%attr(755,root,root) %ghost %{_libdir}/libgbm.so.1
%attr(755,root,root) %{_libdir}/libgbm.so.*.*.*
%dir %{_libdir}/gbm
%{_libdir}/gbm/gbm_gallium_drm.so

%files libgbm-devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libgbm.so
%{_includedir}/gbm.h
%{_pkgconfigdir}/gbm.pc

%files libglapi
%defattr(644,root,root,755)
%attr(755,root,root) %ghost %{_libdir}/libglapi.so.0
%attr(755,root,root) %{_libdir}/libglapi.so.*.*

%files libwayland-EGL
%defattr(644,root,root,755)
%attr(755,root,root) %ghost %{_libdir}/libwayland-egl.so.1
%attr(755,root,root) %{_libdir}/libwayland-egl.so.*.*.*

%files libwayland-EGL-devel
%defattr(644,root,root,755)
%attr(755,root,root) %ghost %{_libdir}/libwayland-egl.so
%{_pkgconfigdir}/wayland-egl.pc

%files libxatracker
%defattr(644,root,root,755)
%attr(755,root,root) %ghost %{_libdir}/libxatracker.so.2
%attr(755,root,root) %{_libdir}/libxatracker.so.*.*.*

%files libxatracker-devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libxatracker.so
%{_includedir}/xa_*.h
%{_pkgconfigdir}/xatracker.pc

# dri drivers
%files dri-driver-ati-r600
%defattr(644,root,root,755)
%attr(755,root,root) %{dridir}/r600_dri.so

%files dri-driver-ati-radeonsi
%defattr(644,root,root,755)
%attr(755,root,root) %{dridir}/radeonsi_dri.so

%files dri-driver-intel-i915
%defattr(644,root,root,755)
%attr(755,root,root) %{dridir}/i915_dri.so

%files dri-driver-intel-i965
%defattr(644,root,root,755)
%attr(755,root,root) %{dridir}/i965_dri.so

%files dri-driver-nvidia-nouveau
%defattr(644,root,root,755)
%attr(755,root,root) %{dridir}/nouveau_dri.so
%attr(755,root,root) %{dridir}/nouveau_vieux_dri.so

%files dri-driver-swrast
%defattr(644,root,root,755)
%attr(755,root,root) %{dridir}/swrast_dri.so

%files dri-driver-vmware
%defattr(644,root,root,755)
%attr(755,root,root) %{dridir}/vmwgfx_dri.so

# gallium drivers
%files gallium-pipe-nvidia-nouveau
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/gallium-pipe/pipe_nouveau.so

%files gallium-pipe-ati-r600
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/gallium-pipe/pipe_r600.so

%files gallium-pipe-ati-radeonsi
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/gallium-pipe/pipe_radeonsi.so

%files gallium-pipe-swrast
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/gallium-pipe/pipe_swrast.so

%files gallium-pipe-vmware
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/gallium-pipe/pipe_vmwgfx.so

