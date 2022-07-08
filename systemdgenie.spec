Name:           systemdgenie
Version:        master
Release:        1%{?dist}
Summary:        Systemd managment utility

License:        GPLv2+
URL:            https://invent.kde.org/system/%{name}
Source0:        %{url}/-/archive/master/%{name}-master.tar.gz

BuildRequires:  gcc
BuildRequires:  gcc-c++
BuildRequires:  make
BuildRequires:  cmake
BuildRequires:  extra-cmake-modules
BuildRequires:  pkgconfig
BuildRequires:  gettext
BuildRequires:  systemd-devel
BuildRequires:  qt5-qtbase-devel
BuildRequires:  kf5-kauth-devel
BuildRequires:  kf5-kcoreaddons-devel
BuildRequires:  kf5-kcrash-devel
BuildRequires:  kf5-ki18n-devel
BuildRequires:  kf5-rpm-macros
BuildRequires:  kf5-kxmlgui-devel

%description
Systemd managment utility

%prep
%setup -q -n %{name}-master
#% setup -q -n %{name}-%{version}
#% autosetup -p0 -n %{name}-v%{version}

%build
%{cmake_kf5} -DCMAKE_BUILD_TYPE=Release
%cmake_build

#make %{?_smp_mflags}
#% cmake_build

%install
%cmake_install

#% install
#% cmake_install

%files
%license COPYING
%{_bindir}/%{name}

%changelog
* Tue May 31 2016 David Conner 0.99
- First RPM Build
