%bcond_with check

Name:           micropipenv
Version:        1.0.2
Release:        5%{?dist}
Summary:        A simple wrapper around pip to support Pipenv and Poetry files

License:        LGPLv3+
URL:            https://github.com/thoth-station/%{name}
Source0:        %{url}/archive/v%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  python3-devel
BuildRequires:  python3dist(pip)
BuildRequires:  python3dist(setuptools)
BuildRequires:  python3dist(toml)
%if %{with check}
# For testing
# Most of the test dependencies are not packaged in RHEL but can be pip-installed
BuildRequires:  python3dist(flexmock)
BuildRequires:  python3dist(pytest)
BuildRequires:  python3dist(pytest-timeout)
BuildRequires:  python3dist(pytest-venv)
%endif

%{?python_provide:%python_provide python3-%{name}}

Requires:       python3dist(pip)
Requires:       python3dist(setuptools)
Requires:       python3dist(toml)

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

%check
%if %{with check}
# - skipped tests requires internet
# - skipped check of pip version - micropipenv is coupled with pip and checks
#   if it's using the latest version, but it's being tested upstream with old
#   RHEL versions as well, and if the rest of the test suite is passing, there
#   should not be issues
%pytest -m "not online" -k "not test_check_pip_version"
%endif

%files
%doc README.rst
%license LICENSE*
%{_bindir}/micropipenv
%pycached %{python3_sitelib}/%{name}.py
%{python3_sitelib}/%{name}-%{version}-py*.egg-info/

%changelog
* Mon Aug 09 2021 Mohan Boddu <mboddu@redhat.com> - 1.0.2-5
- Rebuilt for IMA sigs, glibc 2.34, aarch64 flags
  Related: rhbz#1991688

* Fri Apr 16 2021 Mohan Boddu <mboddu@redhat.com> - 1.0.2-4
- Rebuilt for RHEL 9 BETA on Apr 15th 2021. Related: rhbz#1947937

* Mon Mar 01 2021 Charalampos Stratakis <cstratak@redhat.com> - 1.0.2-3
- Disable the test run under RHEL due to missing dependencies
Resolves: rhbz#1932454

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Fri Dec 11 2020 Lumír Balhar <lbalhar@redhat.com> - 1.0.2-1
- Update to 1.0.2 (#1906430)

* Tue Nov 10 2020 Lumír Balhar <lbalhar@redhat.com> - 1.0.1-1
- Update to 1.0.1

* Fri Oct 02 2020 Lumír Balhar <lbalhar@redhat.com> - 1.0.0-1
- Update to 1.0.0 (#1884346)

* Thu Sep 03 2020 Lumír Balhar <lbalhar@redhat.com> - 0.6.0-1
- Update to 0.6.0 (#1875250)

* Thu Jul 30 2020 Lumír Balhar <lbalhar@redhat.com> - 0.5.1-1
- Update to 0.5.1 (#1859995)

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

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
