%global  kf_version 6.6.0

Name: kf6-prison
Version: 6.6.0
Release: 0%{?dist}
Summary: KDE Frameworks Library to read and write QR codes

License: LGPLv2+
URL:     https://invent.kde.org/frameworks/prison
Source0: %{name}-%{version}.tar.bz2

BuildRequires:  cmake
BuildRequires:  kf6-extra-cmake-modules >= %{majmin_ver_kf6}
BuildRequires:  kf6-rpm-macros
BuildRequires:  make

BuildRequires: kf6-kconfig-devel >= %{majmin_ver_kf6}

# Required:

BuildRequires: pkgconfig(libqrencode)
BuildRequires: doxygen

BuildRequires: qt6-qtbase-devel
BuildRequires: qt6-qttools-devel

# Optional:
#BuildRequires: qt6-qtmultimedia-devel
#BuildRequires: qt6-qtdeclarative-devel
BuildRequires: pkgconfig(Qt6Gui)
BuildRequires: pkgconfig(Qt6Multimedia)
BuildRequires: pkgconfig(Qt6Qml)
BuildRequires: pkgconfig(Qt6Quick)

# Recommended:
BuildRequires: pkgconfig(zxing)
BuildRequires: pkgconfig(libdmtx)

Requires(post): /sbin/ldconfig
Requires(postun): /sbin/ldconfig

%description
%{summary}.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name} = %{version}-%{release}
%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%package        doc
Summary:        Developer Documentation files for %{name}
BuildArch:      noarch
%description    doc
Developer Documentation files for %{name} for use with KDevelop or QtCreator.

%prep
%autosetup -n %{name}-%{version}/upstream -p1

%build
%cmake_kf6
%cmake_build

%install
%cmake_install

%post -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files
%license LICENSES/*
%{_kf6_libdir}/libKF6PrisonScanner.so.*
%{_kf6_libdir}/libKF6Prison.so.*
%{_kf6_qmldir}/org/kde/prison/
%{_kf6_datadir}/qlogging-categories6/*categories

%files devel
%{_kf6_includedir}/Prison/
%{_kf6_includedir}/PrisonScanner/
%{_kf6_libdir}/cmake/KF6Prison/
%{_kf6_libdir}/libKF6PrisonScanner.so
%{_kf6_libdir}/libKF6Prison.so
%{_qt6_docdir}/*.tags

%files doc
%{_qt6_docdir}/*.qch
