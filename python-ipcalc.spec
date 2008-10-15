%define		module ipcalc
Summary:	IP subnet calculator
Summary(pl.UTF-8):	kalkulator podsieci IP
Name:		python-%{module}
Version:	0.1
Release:	0.1
License:	MIT License
Group:		Libraries/Python
Source0:	http://tehmaze.com/asset/code/python/%{module}-%{version}.tar.bz2
# Source0-md5:	9a445fc643b49ddb8a11160cfae2eb00
URL:		http://tehmaze.com/code/python/ipcalc/
BuildRequires:	python-devel >= 1:2.5
BuildRequires:	python-setuptools
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.174
%pyrequires_eq	python-modules
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This module allows you to perform IP subnet calculations, there is
support for both IPv4 and IPv6 CIDR notation.

%description -l pl.UTF-8
Ten moduł pozwala na kalkulacje podsieci IP, wspiera notację CIDR
zarówno dla IPv4 jak i IPv6.

%prep
%setup -q -n %{module}-%{version}

%build
%{__python} setup.py build

%install
rm -rf $RPM_BUILD_ROOT
%{__python} setup.py install \
	--optimize=2 \
	--root $RPM_BUILD_ROOT

%py_postclean

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{py_sitescriptdir}/*.py[co]
%{py_sitescriptdir}/*.egg-info
