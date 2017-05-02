Name     : testpath
Version  : 0.3
Release  : 2
URL      : https://pypi.python.org/packages/fe/53/301852a341e1f5cc82f9987d28595fb04ef2d9869a4efa2d379d207b2b77/testpath-0.3-py2.py3-none-any.whl
Source0  : https://pypi.python.org/packages/fe/53/301852a341e1f5cc82f9987d28595fb04ef2d9869a4efa2d379d207b2b77/testpath-0.3-py2.py3-none-any.whl
Summary  : No detailed summary available
Group    : Development/Tools
License  : MIT
BuildRequires : python3-dev
BuildRequires : pip

%description
No detailed description available

%prep

%build
export LANG=C
export SOURCE_DATE_EPOCH=1486351168

%install
rm -rf %{buildroot}
pip3 install --no-deps  --root %{buildroot} %{SOURCE0}
for i in `find %{buildroot} -name "*.so" `; do rm $i; done

%files
%defattr(-,root,root,-)
/usr/lib/python3.6/site-packages
