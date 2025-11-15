%define		module	pyproject_parser
Summary:	Parser for 'pyproject.toml'
Summary(pl.UTF-8):	Parser plików pyproject.toml
Name:		python3-%{module}
Version:	0.13.0
Release:	1
License:	MIT
Group:		Libraries/Python
#Source0Download: https://pypi.org/simple/pyproject-parser/
Source0:	https://files.pythonhosted.org/packages/source/p/pyproject-parser/pyproject_parser-%{version}.tar.gz
# Source0-md5:	50e9c7c9b716aef84e97f4eb8d47922a
URL:		https://pypi.org/project/pyproject-parser/
BuildRequires:	python3-build
BuildRequires:	python3-hatch-requirements-txt
BuildRequires:	python3-hatchling
BuildRequires:	python3-installer
BuildRequires:	python3-modules >= 1:3.6.1
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 2.044
Requires:	python3-modules >= 1:3.6.1
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Parser for 'pyproject.toml'.

%description -l pl.UTF-8
Parser plików pyproject.toml

%prep
%setup -q -n pyproject_parser-%{version}

%build
%py3_build_pyproject

%install
rm -rf $RPM_BUILD_ROOT

%py3_install_pyproject

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc LICENSE README.rst
%attr(755,root,root) %{_bindir}/check-pyproject
%attr(755,root,root) %{_bindir}/pyproject-fmt
%attr(755,root,root) %{_bindir}/pyproject-info
%attr(755,root,root) %{_bindir}/pyproject-parser
%{py3_sitescriptdir}/%{module}
%{py3_sitescriptdir}/%{module}-%{version}.dist-info
