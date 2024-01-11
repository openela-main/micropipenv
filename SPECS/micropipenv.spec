%bcond_with check

Name:           micropipenv
Version:        1.0.2
Release:        1%{?dist}
Summary:        A simple wrapper around pip to support Pipenv and Poetry files

License:        LGPLv3+
URL:            https://github.com/thoth-station/%{name}
Source0:        %{url}/archive/v%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  python3-devel
BuildRequires:  python3-pip
BuildRequires:  python3-setuptools
BuildRequires:  python3-pytoml
%if %{with check}
# For testing
# Most of the test dependencies are not packaged in RHEL but can be pip-installed
BuildRequires:  python3dist(flexmock)
BuildRequires:  python3dist(pytest)
BuildRequires:  python3dist(pytest-timeout)
BuildRequires:  python3dist(pytest-venv)
%endif

%{?python_provide:%python_provide python3-%{name}}

Requires:       python3-pip
Requires:       python3-setuptools
Requires:       python3-pytoml

%description
A lightweight wrapper for pip to support Pipenv and Poetry lock files or
converting them to pip-tools compatible output.

%prep
%autosetup -n %{name}-%{version}
# Remove shebang line from the module
sed -i '1{\@^#!/usr/bin/env python@d}' %{name}.py

%build
%py3_build

%install
%py3_install
# Switch pip executable from pip to pip3.6
sed -i 's/_PIP_BIN = os.getenv("MICROPIPENV_PIP_BIN", "pip")/_PIP_BIN = os.getenv("MICROPIPENV_PIP_BIN", "pip3.6")/' %{buildroot}%{python3_sitelib}/micropipenv.py

%check
%if %{with check}
# - skipped tests requires internet
# - skipped check of pip version - micropipenv is coupled with pip and checks
#   if it's using the latest version, but it's being tested upstream with old
#   RHEL versions as well, and if the rest of the test suite is passing, there
#   should not be issues
%{python3} -m pytest tests -m "not online" -k "not test_check_pip_version"
%endif

%files
%doc README.rst
%license LICENSE*
%{_bindir}/micropipenv
%{python3_sitelib}/%{name}.py
%{python3_sitelib}/__pycache__/%{name}*.pyc
%{python3_sitelib}/%{name}-%{version}-py*.egg-info/

%changelog
* Fri Dec 11 2020 Lumír Balhar <lbalhar@redhat.com> - 1.0.2-1
- Update to 1.0.2 to fix tests
Resolves: rhbz#1849096

* Mon Nov 02 2020 Tomas Orsava <torsava@redhat.com> - 1.0.0-1
- Update to 1.0.0
- Resolves: rhbz#1849096

* Mon Sep 07 2020 Tomas Orsava <torsava@redhat.com> - 0.6.0-1
- Update to 0.6.0
- Resolves: rhbz#1849096

* Fri Jul 17 2020 Lumír Balhar <lbalhar@redhat.com> - 0.4.0-2
- Initial RHEL8 packaging
- Resolves: rhbz#1849096

* Thu Jul 09 2020 Lumír Balhar <lbalhar@redhat.com> - 0.4.0-1
- Update to 0.4.0 (#1854424)

* Mon Jun 15 2020 Lumír Balhar <lbalhar@redhat.com> - 0.3.0-1
- Update to 0.3.0 (#1846944)

* Fri Jun 05 2020 Miro Hrončok <mhroncok@redhat.com> - 0.2.0-2
- Correct the license tag (GPLv3+ to LGPLv3+)
- Include the actual LICENSE files in the package

* Thu Jun 04 2020 Lumír Balhar <lbalhar@redhat.com> - 0.2.0-1
- Update to 0.2.0 (#1838278, #1841641)

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 0.1.6-2
- Rebuilt for Python 3.9

* Tue May 05 2020 Lumír Balhar <lbalhar@redhat.com> - 0.1.6-1
- Update to 0.1.6 (#1831328)

* Tue Apr 07 2020 Lumír Balhar <lbalhar@redhat.com> - 0.1.5-1
- Update to 0.1.5 (#1821807)

* Thu Mar 12 2020 Lumír Balhar <lbalhar@redhat.com> - 0.1.4-1
- Initial package.
