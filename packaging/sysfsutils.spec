Name:           sysfsutils
Summary:        System Utilities Package / Libsysfs
License:        LGPL-2.1+
Group:          System/Libraries
Version:        2.1.0
Release:        0
Url:            http://linux-diag.sourceforge.net
Source:         http://aleron.dl.sourceforge.net/sourceforge/linux-diag/%{name}-%{version}.tar.gz
Source2:        baselibs.conf
Source1001: 	sysfsutils.manifest
Provides:       libsysfs

%description
This package's purpose is to provide a library for interfacing with the
kernel's sys filesystem mounted at /sys. The library was an attempt to
create a stable interface to sysfs, but it failed. It is still provided
for the current users, but no new software should use this library.

%package devel
Summary:        Development files for libsysfs
Group:          Development/Libraries/C and C++
Requires:       %{name} = %{version}

%description devel
Libsysfs' purpose is to provide a library for interfacing with the
kernel's sys filesystem mounted at /sys. The library was an attempt to
create a stable interface to sysfs, but it failed. It is still provided
for the current users, but no new software should use this library.

This package contains the development files for libsysfs.

%prep
%setup -q
cp %{SOURCE1001} .

%build
%configure --disable-static --with-pic
%{__make} %{?_smp_mflags}

%install
%make_install
# don't install the tools
rm -f %{buildroot}/%{_bindir}/dlist_test
rm -f %{buildroot}/%{_bindir}/get_device
rm -f %{buildroot}/%{_bindir}/get_driver
rm -f %{buildroot}/%{_bindir}/get_module
rm -f %{buildroot}/%{_bindir}/testlibsysfs

%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig

%files
%manifest %{name}.manifest
%license COPYING
%defattr(-,root,root)
/usr/bin/systool
%{_mandir}/man1/systool.1.gz
%{_libdir}/libsysfs.so.*
%doc README 

%files devel
%manifest %{name}.manifest
%defattr(-,root,root)
%dir %{_includedir}/sysfs
%{_includedir}/sysfs/libsysfs.h
%{_includedir}/sysfs/dlist.h
%{_libdir}/libsysfs.so

%changelog
