Name:       libxcb
Summary:    A C binding to the X11 protocol
Version:    1.7
Release:    3.3
Group:      System/Libraries
License:    MIT
URL:        http://xcb.freedesktop.org/
Source0:    http://xcb.freedesktop.org/dist/%{name}-%{version}.tar.gz
Requires(post): /sbin/ldconfig
Requires(postun): /sbin/ldconfig
BuildRequires:  pkgconfig(xorg-macros)
BuildRequires:  pkgconfig(pthread-stubs)
BuildRequires:  pkgconfig(xcb-proto)
BuildRequires:  pkgconfig(xau)
BuildRequires:  pkgconfig(xproto)
BuildRequires:  libxslt
BuildRequires:  python-xml, python-devel


%description
Description: %{summary}


%package devel
Summary:    Development files for %{name}
Group:      Development/Libraries
Requires:   %{name} = %{version}-%{release}
Requires:   libpthread-stubs
Requires:   libXau-devel

%description devel
Description: %{summary}

%package doc
Summary:    Documentation for %{name}
Group:      Documentation
Requires:   %{name} = %{version}-%{release}

%description doc
Description: %{summary}


%prep
%setup -q


%build

%reconfigure \
    --disable-build-docs \
    CFLAGS="-D_F_ENABLE_XI2_SENDEVENT_" \
    LDFLAGS="-Wl,--hash-style=both -Wl,--as-needed"
    

make %{?jobs:-j%jobs}

%install
rm -rf %{buildroot}
%make_install 




%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig








%files
%defattr(-,root,root,-)
%{_libdir}/*.so.*


%files devel
%defattr(-,root,root,-)
%{_includedir}/xcb
%{_libdir}/*.so
%{_libdir}/pkgconfig/*.pc

%files doc
%defattr(-,root,root,-)
%{_datadir}/doc/%{name}

