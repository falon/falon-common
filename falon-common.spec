%global systemd (0%{?fedora} >= 18) || (0%{?rhel} >= 7)
%global bigname falon-common

Summary: A set of shared object used in many my projects.
Name: FalonCommon
Version: 0.1.3
Release: 3%{?dist}
Group: Development/Libraries
License: Apache-2.0
URL: https://falon.github.io/%{bigname}/
Source0: https://github.com/falon/%{bigname}/archive/master.zip
BuildArch:	noarch

# Required for all versions
Requires: httpd >= 2.4.6
Requires: mod_ssl >= 2.4.6
Requires: php >= 7.1

%description
%{bigname} 
A set of library used in many projects maintained
by Marco Favero. Usually these are only simple
files used in html page for styling, or some js
stored in the /include Document Root.

%clean
rm -rf %{buildroot}/

%prep
%autosetup -n %{bigname}-master


%install

rm -rf rpm/*

# Web HTTPD conf
install -D -m0444 %{bigname}.conf %{buildroot}%{_sysconfdir}/httpd/conf.d/%{bigname}.conf
sed -i 's|\/var\/www\/html\/%{bigname}|%{_datadir}/include|' %{buildroot}%{_sysconfdir}/httpd/conf.d/%{bigname}.conf

# Include dir
mkdir -p %{buildroot}%{_datadir}/include
mkdir -p %{buildroot}%{_datadir}/%{bigname}
install -m0444 ajaxsbmt.js %{buildroot}%{_datadir}/include
install -m0444 checkAll.js %{buildroot}%{_datadir}/include
install -m0444 keymail.js %{buildroot}%{_datadir}/include
install -m0444 pleasewait.gif %{buildroot}%{_datadir}/include
install -m0444 style.css  %{buildroot}%{_datadir}/include
# Docs
install -m0444 LICENSE %{buildroot}%{_datadir}/%{bigname}/LICENSE
install -m0444 README.md %{buildroot}%{_datadir}/%{bigname}/README.md

%files
%{_datadir}/include
%config(noreplace) %{_sysconfdir}/httpd/conf.d/%{bigname}.conf
%license %{_datadir}/%{bigname}/LICENSE
%doc %{_datadir}/%{bigname}/README.md

%changelog
* Mon Jan 08 2021 Marco Favero <marco.favero@csi.it> 0.1.3-3
- Fixed include path

* Fri Jun 12 2020 Marco Favero <marco.favero@csi.it> 0.1.3-2
- The path is now falon-common/ and aliased as /include

* Thu Jan 24 2019 Marco Favero <marco.favero@csi.it> 0.1.3-1
- Added features for "PHP-Cyrus-Restore" project

* Wed Jan 09 2019 Marco Favero <marco.favero@csi.it> 0.1.2-1
- Added keymail.js

* Thu Jan 03 2019 Marco Favero <marco.favero@csi.it> 0.1.1-1
- Added httpd.conf

* Thu Jan 03 2019 Marco Favero <marco.favero@csi.it> 0.1.0-1
- Initial build version
