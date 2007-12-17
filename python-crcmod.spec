%define oname crcmod

Name:           python-%{oname}
Version:        1.4
Release:        %mkrel 1
Epoch:          0
Summary:        Creates functions that efficiently compute CRC's using table lookup
URL:            http://crcmod.sourceforge.net/
Source0:        http://crcmod.sourceforge.net/download/%{oname}-%{version}.tar.gz
License:        MIT
Group:          Development/Python
BuildRequires:  python-devel

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
%setup -q -n %{oname}-%{version}

%build
CFLAGS="%{optflags}" %{_bindir}/python setup.py build

%install
%{__rm} -rf %{buildroot}
%{_bindir}/python setup.py install --root=%{buildroot}

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-,root,root,0755)
%doc README changelog
%{_libdir}/python%{pyver}/site-packages/*
