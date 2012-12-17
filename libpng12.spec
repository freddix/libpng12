Summary:	PNG library
Name:		libpng12
Version:	1.2.50
Release:	1
Epoch:		2
License:	distributable
Group:		Libraries
Source0:	http://download.sourceforge.net/libpng/libpng-%{version}.tar.xz
# Source0-md5:	a3e00fccbfe356174ab515b5c00641c7
Patch0:		%{name}-pngminus.patch
Patch1:		%{name}-opt.patch
Patch2:		%{name}-norpath.patch
Patch3:		%{name}-export_old.patch
Patch4:		%{name}-revert.patch
Patch5:		%{name}-apng.patch
URL:		http://www.libpng.org/pub/png/libpng.html
BuildRequires:	zlib-devel
Provides:       libpng = %{epoch}:%{version}-%{release}
Provides:	libpng.so.3
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The PNG library is a collection of routines used to create and
manipulate PNG format graphics files. The PNG format was designed as a
replacement for GIF, with many improvements and extensions.

%package devel
Summary:	Header files for libpng
Group:		Development/Libraries
Requires:	%{name} = %{epoch}:%{version}-%{release}
Provides:       libpng-devel = %{epoch}:%{version}-%{release}

%description devel
The header files are only needed for development of programs using the
PNG library.

%package static
Summary:	Static png library
Group:		Development/Libraries
Requires:	%{name}-devel = %{epoch}:%{version}-%{release}
Provides:       libpng-devel = %{epoch}:%{version}-%{release}

%description static
Static ppng library.

%package progs
Summary:	libpng utility programs
Group:		Applications/Graphics

%description progs
This package contains utility programs to convert PNG files to and
from PNM files.

%prep
%setup -qn libpng-%{version}
%patch0 -p1
%patch1 -p1
%patch2 -p1
%patch3 -p1
%patch4 -p1
%patch5 -p0

%build
%{__libtoolize}
%{__aclocal}
%{__autoheader}
%{__automake}
%{__autoconf}
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_libdir},%{_mandir}/man{3,5}} \
	$RPM_BUILD_ROOT%{_pkgconfigdir}

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

# parts provided by libpng >= 1.4.x
%{__rm} $RPM_BUILD_ROOT%{_bindir}/libpng-config \
	$RPM_BUILD_ROOT%{_includedir}/png*.h \
	$RPM_BUILD_ROOT%{_libdir}/libpng.{la,so,a} \
	$RPM_BUILD_ROOT%{_pkgconfigdir}/libpng.pc
%{__rm} -r $RPM_BUILD_ROOT%{_mandir}/man[35]

%clean
rm -rf $RPM_BUILD_ROOT

%post   -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc ANNOUNCE CHANGES KNOWNBUG README LICENSE
%attr(755,root,root) %ghost %{_libdir}/libpng12.so.0
%attr(755,root,root) %{_libdir}/libpng*.so.*.*.*
%attr(755,root,root) %{_libdir}/libpng.so.3

%files devel
%defattr(644,root,root,755)
%doc *.txt
%attr(755,root,root) %{_bindir}/libpng12-config
%attr(755,root,root) %{_libdir}/libpng12.so
%{_includedir}/libpng12
%{_libdir}/libpng12.la
%{_pkgconfigdir}/libpng12.pc

%files static
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libpng*.a

