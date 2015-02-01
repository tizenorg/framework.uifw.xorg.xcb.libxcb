Name:    libxcb
Summary: A C binding to the X11 protocol
Version: 1.8.1
Release: 1
Group:   System/Libraries
License: MIT
URL:     http://xcb.freedesktop.org/
Source0: http://xcb.freedesktop.org/dist/%{name}-%{version}.tar.gz

BuildRequires:  xorg-x11-xutils-dev
BuildRequires:  libpthread-stubs
BuildRequires:  libXau-devel
BuildRequires:  pkgconfig(xproto)
BuildRequires:  xcb-proto >= 1.6
BuildRequires:  libxslt
BuildRequires:  python
BuildRequires:  python-xml

Requires(post):   /sbin/ldconfig
Requires(postun): /sbin/ldconfig

%description
Description: %{summary}
The X protocol C-language Binding (XCB) is a replacement for Xlib featuring a
small footprint, latency hiding, direct access to the protocol, improved
threading support, and extensibility.

%package devel
Summary: Development files for %{name}
Group:   Development/Libraries

BuildRequires: libXau-devel

Requires: %{name} = %{version}-%{release}
Requires: libpthread-stubs

%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%package        doc
Summary:        Documentation for %{name}
Group:          Documentation
BuildArch:	noarch

%description    doc
The %{name}-doc package contains documentation for the %{name} library.

%prep
%setup -q

%build

./autogen.sh
%reconfigure \
    --disable-build-docs \
    LDFLAGS="${LDFLAGS} -Wl,--hash-style=both -Wl,--as-needed"

# Call make instruction with smp support
make %{?jobs:-j%jobs}

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/license
cp -af COPYING %{buildroot}/usr/share/license/%{name}
%make_install

rm -f $RPM_BUILD_ROOT/%{_libdir}/libxcb-xprint.so*
rm -f $RPM_BUILD_ROOT/%{_includedir}/xcb/xprint.h

find $RPM_BUILD_ROOT -name '*.la' -delete

%remove_docs


%clean
rm -rf $RPM_BUILD_ROOT

%post -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files
%defattr(-,root,root,-)
%{_libdir}/libxcb.so.1*
%{_libdir}/libxcb-*
/usr/share/license/%{name}

%files devel
%defattr(-,root,root,-)
%{_includedir}/xcb
%{_libdir}/*.so
%{_libdir}/pkgconfig/*.pc

#%files doc
#%defattr(-,root,root,-)
#%{_datadir}/doc/%{name}