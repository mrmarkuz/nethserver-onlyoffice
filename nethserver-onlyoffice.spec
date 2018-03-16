Name: nethserver-onlyoffice
Version: 0.0.1
Release: 1%{?dist}
Summary: Onlyoffice document server for NethServer
License: GPL
Source0: %{name}-%{version}.tar.gz
BuildArch: noarch
BuildRequires: nethserver-devtools
Requires: nethserver-postgresql,nethserver-redis,nethserver-nginx
Requires: rabbitmq-server,supervisor,onlyoffice-documentserver

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
* Fri Mar 10 2018 Markus Neuberger <dev@markusneuberger.at> - 0.0.1-1
- First release
- Add requires
- Setup documentserver and nginx
