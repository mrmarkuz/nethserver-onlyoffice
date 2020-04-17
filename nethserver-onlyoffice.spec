Name: nethserver-onlyoffice
Version: 0.0.1
Release: 9%{?dist}
Summary: Onlyoffice document server for NethServer
License: GPL
Source0: %{name}-%{version}.tar.gz
BuildArch: noarch
BuildRequires: nethserver-devtools
Requires: nethserver-postgresql,nethserver-redis,nethserver-nginx,onlyoffice-documentserver
Requires: rabbitmq-server,supervisor,rh-php73-php-cli

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
* Fri Apr 17 2020 Markus Neuberger <dev@markusneuberger.at> - 0.0.1-9
- Use jq instead of npm json - thanks to Klaus Boehme
- Fix php memory error
* Wed Sep 28 2019 Markus Neuberger <dev@markusneuberger.at> - 0.0.1-8
- Add stronger password for working with Webtop - thanks to Klaus Boehme
- Add Webtop support
* Wed Sep 04 2019 Markus Neuberger <dev@markusneuberger.at> - 0.0.1-7
- Change config file and user
* Wed Nov 07 2018 Markus Neuberger <dev@markusneuberger.at> - 0.0.1-6
- Change config file owner to work with versions newer than 5.2 - thanks to giacomo
* Fri Sep 21 2018 Markus Neuberger <dev@markusneuberger.at> - 0.0.1-4
- add RejectUnauthorized prop to make it work with self-signed certs
- remove rabbitmq-server requirement
- change spellchecker port 8080 to 48080 to not conflict with nethserver-tomcat
* Sat Apr 07 2018 Markus Neuberger <dev@markusneuberger.at> - 0.0.1-3
- check if database exists - thanks to @dnutan
- check if nextcloud exists - thanks to @dnutan
- tidy up conf action
- remove documentserver script
- make documentserver updates possible
- use json import instead of templating defaults.json
- remove install errors - thanks to @dnutan
* Tue Mar 20 2018 Markus Neuberger <dev@markusneuberger.at> - 0.0.1-2
- Secure access via JWT token - thanks to @dnutan
- autoinstall of onlyoffice nextcloud app - thanks to @danb35
- allow self-signed cert - thanks to @flatspin
- add host db prop
* Sat Mar 10 2018 Markus Neuberger <dev@markusneuberger.at> - 0.0.1-1
- First release
- Add requires
- Setup documentserver and nginx
