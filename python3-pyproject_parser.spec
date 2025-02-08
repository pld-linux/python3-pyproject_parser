%define		module	pyproject_parser
Summary:	Parser for 'pyproject.toml'
Name:		python3-%{module}
Version:	0.11.1
Release:	1
License:	MIT
Group:		Libraries/Python
Source0:	https://pypi.debian.net/pyproject-parser/pyproject-parser-%{version}.tar.gz
# Source0-md5:	316169c265142c30cce9524cc4bcc07e
URL:		https://pypi.org/project/pyproject_parser/
BuildRequires:	python3-build
BuildRequires:	python3-installer
BuildRequires:	python3-modules >= 1:3.2
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 2.044
Requires:	python3-modules >= 1:3.2
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Parser for 'pyproject.toml'.

%prep
%setup -q -n pyproject-parser-%{version}

sed -i -e 's#<=67.1.0,##g' pyproject.toml

%build
%py3_build_pyproject

%install
rm -rf $RPM_BUILD_ROOT

%py3_install_pyproject

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README.rst
%attr(755,root,root) %{_bindir}/check-pyproject
%attr(755,root,root) %{_bindir}/pyproject-fmt
%attr(755,root,root) %{_bindir}/pyproject-info
%attr(755,root,root) %{_bindir}/pyproject-parser
%{py3_sitescriptdir}/%{module}
%{py3_sitescriptdir}/%{module}-%{version}.dist-info
