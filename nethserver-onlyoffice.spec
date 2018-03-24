Name: nethserver-onlyoffice
Version: 0.0.1
Release: 3%{?dist}
Summary: Onlyoffice document server for NethServer
License: GPL
Source0: %{name}-%{version}.tar.gz
BuildArch: noarch
BuildRequires: nethserver-devtools
Requires: nethserver-postgresql,nethserver-redis,nethserver-nginx,onlyoffice-documentserver
Requires: rabbitmq-server,supervisor,rh-php71-php-cli

%description
Onlyoffice document server for for NethServer, a web based document editor server

%prep
%setup -q

%build
%{makedocs}
perl createlinks

%install
rm -rf %{buildroot}
(cd root ; find . -depth -print | cpio -dump %{buildroot})
%{genfilelist} %{buildroot} > %{name}-%{version}-%{release}-filelist


%files -f %{name}-%{version}-%{release}-filelist
%defattr(-,root,root)
%dir %{_nseventsdir}/%{name}-update


%changelog
* Mon Apr 02 2018 Markus Neuberger <dev@markusneuberger.at> - 0.0.1-3
- check if database exists - thanks to @dnutan
- check if nextcloud exists - thanks to @dnutan
- tidy up conf action
- remove documentserver script
- make documentserver updates possible
- use json import instead of templating defaults.json
* Tue Mar 20 2018 Markus Neuberger <dev@markusneuberger.at> - 0.0.1-2
- Secure access via JWT token - thanks to @dnutan
- autoinstall of onlyoffice nextcloud app - thanks to @danb35
- allow self-signed cert - thanks to @flatspin
- add host db prop
* Sat Mar 10 2018 Markus Neuberger <dev@markusneuberger.at> - 0.0.1-1
- First release
- Add requires
- Setup documentserver and nginx
