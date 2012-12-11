%define oname crcmod

Name:           python-%{oname}
Version:        1.7
Release:        3
Epoch:          0
Summary:        Creates functions that efficiently compute CRC's using table lookup
URL:            http://crcmod.sourceforge.net/
Source0:        http://sourceforge.net/projects/crcmod/files/crcmod/crcmod-%{versio}/crcmod-%{version}.tar.gz
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
%{_bindir}/python setup.py install --root=%{buildroot}

%files
%defattr(-,root,root,0755)
%doc README changelog
%{_libdir}/python%{py_ver}/site-packages/*


%changelog
* Fri Nov 19 2010 Funda Wang <fwang@mandriva.org> 0:1.7-2mdv2011.0
+ Revision: 598983
- rebuild for py2.7

* Sun Sep 12 2010 Guillaume Rousse <guillomovitch@mandriva.org> 0:1.7-1mdv2011.0
+ Revision: 577729
- new version

* Tue Mar 09 2010 Sandro Cazzaniga <kharec@mandriva.org> 0:1.6.1-1mdv2010.1
+ Revision: 516848
- update to 1.6.1

* Mon Jan 11 2010 Guillaume Rousse <guillomovitch@mandriva.org> 0:1.5-1mdv2010.1
+ Revision: 489399
- new version

* Tue Sep 15 2009 Thierry Vignaud <tv@mandriva.org> 0:1.4-5mdv2010.0
+ Revision: 442084
- rebuild

* Fri Aug 01 2008 Thierry Vignaud <tv@mandriva.org> 0:1.4-4mdv2009.0
+ Revision: 259527
- rebuild

* Thu Jul 24 2008 Thierry Vignaud <tv@mandriva.org> 0:1.4-3mdv2009.0
+ Revision: 247397
- rebuild

* Fri Dec 21 2007 Olivier Blin <oblin@mandriva.com> 0:1.4-1mdv2008.1
+ Revision: 136447
- restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request

* Fri Aug 03 2007 David Walluck <walluck@mandriva.org> 0:1.4-1mdv2008.0
+ Revision: 58731
- 1.4


* Tue Jul 25 2006 David Walluck <walluck@mandriva.com> 0:1.3-1mdv2007.0
- release

