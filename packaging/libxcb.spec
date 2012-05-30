Name:       libxcb
Summary:    A C binding to the X11 protocol
Version: 1.7
Release:    0
Group:      System/Libraries
License:    MIT
URL:        http://xcb.freedesktop.org/
Source0:    http://xcb.freedesktop.org/dist/%{name}-%{version}.tar.gz
Source1001: packaging/libxcb.manifest 
Requires(post): /sbin/ldconfig
Requires(postun): /sbin/ldconfig
BuildRequires:  pkgconfig(xorg-macros)
BuildRequires:  pkgconfig(pthread-stubs)
BuildRequires:  pkgconfig(xcb-proto)
BuildRequires:  pkgconfig(xau)
BuildRequires:  pkgconfig(xproto)
BuildRequires:  libxslt
BuildRequires:  python
BuildRequires:  python-xml


%description
Description: %{summary}


%package devel
Summary:    Development files for %{name}
Group:      Development/Libraries
Requires:   %{name} = %{version}-%{release}
Requires:   libpthread-stubs
BuildRequires:  pkgconfig(xau)

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
cp %{SOURCE1001} .

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
%manifest libxcb.manifest
%defattr(-,root,root,-)
%{_libdir}/*.so.*


%files devel
%manifest libxcb.manifest
%defattr(-,root,root,-)
%{_includedir}/xcb
%{_libdir}/*.so
%{_libdir}/pkgconfig/*.pc

%files doc
%manifest libxcb.manifest
%defattr(-,root,root,-)
%{_datadir}/doc/%{name}
