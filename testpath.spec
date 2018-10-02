#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : testpath
Version  : 0.4.2
Release  : 17
URL      : https://files.pythonhosted.org/packages/06/30/9a7e917066d851d8b4117e85794b5f14516419ea714a8a2681ec6aa8a981/testpath-0.4.2.tar.gz
Source0  : https://files.pythonhosted.org/packages/06/30/9a7e917066d851d8b4117e85794b5f14516419ea714a8a2681ec6aa8a981/testpath-0.4.2.tar.gz
Summary  : Test utilities for code working with files and commands
Group    : Development/Tools
License  : BSD-3-Clause
Requires: testpath-license = %{version}-%{release}
Requires: testpath-python = %{version}-%{release}
Requires: testpath-python3 = %{version}-%{release}
BuildRequires : buildreq-distutils3
BuildRequires : python3-dev

%description
Testpath is a collection of utilities for Python code working with files and commands.

%package license
Summary: license components for the testpath package.
Group: Default

%description license
license components for the testpath package.


%package python
Summary: python components for the testpath package.
Group: Default
Requires: testpath-python3 = %{version}-%{release}

%description python
python components for the testpath package.


%package python3
Summary: python3 components for the testpath package.
Group: Default
Requires: python3-core

%description python3
python3 components for the testpath package.


%prep
%setup -q -n testpath-0.4.2

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1538522315
python3 setup.py build

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/testpath
cp LICENSE %{buildroot}/usr/share/package-licenses/testpath/LICENSE
python3 -tt setup.py build  install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----

%files
%defattr(-,root,root,-)

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/testpath/LICENSE

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
