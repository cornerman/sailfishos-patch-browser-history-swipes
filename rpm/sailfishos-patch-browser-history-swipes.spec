Name:       sailfishos-patch-browser-history-swipes
BuildArch:  noarch
Summary:    Swipe URL in browser toolbar right/left in order to go back/forward
Version:    0.0.3
Release:    1
Group:      System/Patches
License:    TODO
Source0:    %{name}-%{version}.tar.xz
Requires:   patchmanager
Requires:   sailfish-browser >= 1.15.12

%description
%{summary}

%prep
%setup -q -n %{name}-%{version}

%build

%install
rm -rf %{buildroot}

mkdir -p %{buildroot}/usr/share/patchmanager/patches/%{name}
cp -r patch/* %{buildroot}/usr/share/patchmanager/patches/%{name}

%pre
if [ -d /var/lib/patchmanager/ausmt/patches/%{name} ]; then
/usr/sbin/patchmanager -u %{name} || true
fi

%preun
if [ -d /var/lib/patchmanager/ausmt/patches/%{name} ]; then
/usr/sbin/patchmanager -u %{name} || true
fi

%files
%defattr(-,root,root,-)
%{_datadir}/patchmanager/patches/%{name}
