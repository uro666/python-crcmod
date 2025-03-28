%global debug_package %{nil}
%define oname crcmod

Name:     python-%{oname}
Version:  1.7
Release:  6
Epoch:    0
Summary:  Creates functions that efficiently compute CRC's using table lookup
URL:      https://crcmod.sourceforge.net/
License:  MIT
Group:    Development/Python
Source0:  http://sourceforge.net/projects/crcmod/files/crcmod/crcmod-%{versio}/crcmod-%{version}.tar.gz
Patch0:   crcmod-1.7-setuptools.patch
BuildSystem:  python

BuildRequires:  python
BuildRequires:  pkgconfig(python3)
BuildRequires:  python%{pyver}dist(setuptools)

%description
Create functions that efficiently compute the Cyclic Redundancy Check 
(CRC) using table lookup.

Features:

    * Create Python functions for computing the CRC. If the optional 
      extension module is installed, the calculations are preformed 
      using fast C code.
    * Create instances of the Crc class that support the interface 
      used by the md5 and sha modules in the Python standard library.
    * Generate C/C++ code that can be incorporated in another project.
    * Any generator polynomial producing 8, 16, 32, or 64 bit CRCs is 
      allowed.
    * Forward and bit-reverse algorithms are supported.

%prep
%autosetup -p1 -n %{oname}-%{version}

%build
export CFLAGS="%{optflags}"
%py_build

%install
%py3_install

# disabled selftest on abf.
#%%check
#%%{__python} -m crcmod.test

%files
%defattr(-,root,root,0755)
%doc README changelog
%{_libdir}/python%{py_ver}/site-packages/*
